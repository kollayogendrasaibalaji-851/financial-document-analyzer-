from celery import Celery
from crewai import Crew, Process
from .agents import financial_analyst
from .tasks import analyze_financial_document
from .database import SessionLocal, AnalysisResult

celery = Celery(
    "financial_worker",
    broker="redis://localhost:6379/0"
)

@celery.task
def process_document(query, file_path, filename):
    crew = Crew(
        agents=[financial_analyst],
        tasks=[analyze_financial_document],
        process=Process.sequential
    )

    result = crew.kickoff({
        "query": query,
        "file_path": file_path
    })

    db = SessionLocal()
    db_result = AnalysisResult(
        filename=filename,
        query=query,
        result=str(result)
    )
    db.add(db_result)
    db.commit()
    db.close()

    return str(result)
