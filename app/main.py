from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import json

app = FastAPI(
    title="Modern Python Web App",
    description="A high-performance web application built with FastAPI",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")

class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False
    created_at: str = datetime.now().isoformat()

class Stats(BaseModel):
    total_tasks: int
    completed_tasks: int
    pending_tasks: int
    completion_rate: float

tasks_db: List[Task] = [
    Task(id=1, title="Build FastAPI Application", description="Create a modern web app with FastAPI", completed=True),
    Task(id=2, title="Design Beautiful UI", description="Implement responsive design with Tailwind CSS", completed=True),
    Task(id=3, title="Add API Endpoints", description="Create RESTful API with CRUD operations", completed=False),
    Task(id=4, title="Deploy to Production", description="Deploy the application for public access", completed=False),
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    stats = get_stats()
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "tasks": tasks_db,
            "stats": stats,
            "current_year": datetime.now().year
        }
    )

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(
        "about.html",
        {
            "request": request,
            "current_year": datetime.now().year
        }
    )

@app.get("/api/tasks", response_model=List[Task])
async def get_tasks():
    return tasks_db

@app.get("/api/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    return {"error": "Task not found"}

@app.post("/api/tasks", response_model=Task)
async def create_task(task: Task):
    tasks_db.append(task)
    return task

@app.put("/api/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db[i] = updated_task
            return updated_task
    return {"error": "Task not found"}

@app.delete("/api/tasks/{task_id}")
async def delete_task(task_id: int):
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(i)
            return {"message": "Task deleted successfully"}
    return {"error": "Task not found"}

@app.get("/api/stats", response_model=Stats)
async def get_statistics():
    return get_stats()

def get_stats() -> Stats:
    total = len(tasks_db)
    completed = sum(1 for task in tasks_db if task.completed)
    pending = total - completed
    rate = (completed / total * 100) if total > 0 else 0
    
    return Stats(
        total_tasks=total,
        completed_tasks=completed,
        pending_tasks=pending,
        completion_rate=round(rate, 1)
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
