from crewai.tools import BaseTool
from pydantic import BaseModel
from typing import Type
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class FinancialDocumentInput(BaseModel):
    document_text: str


class FinancialDocumentTool(BaseTool):
    name: str = "Financial Document Analyzer Tool"
    description: str = (
        "Analyzes financial documents and provides summary, "
        "risk assessment, and key insights."
    )
    args_schema: Type[BaseModel] = FinancialDocumentInput

    def _run(self, document_text: str) -> str:
        try:
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a financial analyst AI."
                    },
                    {
                        "role": "user",
                        "content": f"""
                        Analyze the following financial document.

                        Provide:
                        1. Summary
                        2. Key Financial Insights
                        3. Risk Factors
                        4. Recommendations

                        Document:
                        {document_text}
                        """
                    }
                ],
                temperature=0.3
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"Error analyzing document: {str(e)}"