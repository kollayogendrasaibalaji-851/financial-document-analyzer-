from fastapi import FastAPI, UploadFile, File, Form
import os
import uuid

from .celery_worker import process_document

app = FastAPI(title="Financial Document Analyzer")

@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    query: str = Form("Analyze this document")
):
    file_id = str(uuid.uuid4())
    os.makedirs("data", exist_ok=True)
    file_path = f"data/{file_id}.pdf"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    task = process_document.delay(query, file_path, file.filename)

    return {
        "status": "processing",
        "task_id": task.id
    }
