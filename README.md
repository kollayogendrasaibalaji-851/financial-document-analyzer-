Financial Document Analyzer – Debug Fix & Production Upgrade
📌 Project Overview

This project is an AI-powered Financial Document Analyzer built using CrewAI and FastAPI.

The original codebase contained architectural, dependency, and import-related issues.
This version includes all debug fixes and production-level improvements.

🐛 Bugs Identified & Fixes
1. Missing tools.py

Issue: ModuleNotFoundError: No module named 'app.tools'

Fix: Recreated tools.py inside the app package and corrected imports.

2. Incorrect Import Structure

Issue: Package imports failed when running directly.

Fix: Used python -m app.main and proper package-based imports.

3. Missing Dependencies

Issue: fastapi and python-multipart were not installed.

Fix: Added required dependencies to requirements.txt.

4. Server Not Starting

Issue: Running python app/main.py did not start the server.

Fix: Used uvicorn app.main:app --reload.

⚙️ Setup Instructions
Clone the Repository
git clone <your-repo-link>
cd financial-document-analyzer
Create Virtual Environment
python -m venv venv
venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Run the Application
uvicorn app.main:app --reload

Open in browser:

http://127.0.0.1:8000/docs

📡 API Documentation
POST /analyze

POST /analyze

Analyzes an uploaded financial document using CrewAI agents and returns structured financial insights.

📥 Request

Content-Type: multipart/form-data

Form Field:

Field Name	Type	Required	Description
file	File (PDF / TXT)	Yes	Financial document to analyze
📝 Example Request (Swagger UI)

Upload:

A PDF financial statement
OR

A .txt file containing financial data

Example text file content:

Company: ABC Ltd
Revenue: $2,000,000
Expenses: $1,200,000
Net Profit: $800,000
Assets: $5,000,000
Liabilities: $2,000,000
📤 Example Response
{
  "company": "ABC Ltd",
  "revenue": 2000000,
  "expenses": 1200000,
  "net_profit": 800000,
  "risk_assessment": "Low Risk",
  "financial_summary": "The company shows strong profitability with healthy asset coverage."
}
⚙️ Internal Processing Flow

File is uploaded via FastAPI.

File content is extracted and parsed.

CrewAI agents:

Financial Analyst Agent

Risk Assessment Agent

Summary Agent

Structured output is generated.

Results are returned as JSON.

(Optional) Stored in database.

🔍 How to Test

Start the server:

uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000/docs

Use the /analyze endpoint.

Upload a sample financial document.

Click Execute.

🚀 Bonus Features

Celery worker integration for background processing

Database support for storing analysis results

Clean project structure for scalability
