import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, LLM
from .tools import FinancialDocumentTool

llm = LLM(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Provide evidence-based financial analysis strictly from the uploaded document: {query}",
    backstory=(
        "You are an experienced financial analyst specializing in financial "
        "statements, corporate reporting, and risk analysis. "
        "You never fabricate information."
    ),
    verbose=True,
    memory=True,
    tools=[FinancialDocumentTool()],
    llm=llm,
    max_iter=3,
    allow_delegation=False
)
