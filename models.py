from pydantic import BaseModel

class FinancialAnalysis(BaseModel):
    revenue_summary: str
    profitability_analysis: str
    risk_assessment: str
    investment_outlook: str
