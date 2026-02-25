from crewai import Task
from .agents import financial_analyst

analyze_financial_document = Task(
    description="""
    Analyze the financial document at {file_path}.
    
    User Query: {query}
    
    Provide:
    1. Revenue trends
    2. Profitability insights
    3. Risk analysis
    4. Investment outlook
    
    Base conclusions strictly on document data.
    """,
    expected_output="Structured financial analysis report.",
    agent=financial_analyst,
)
