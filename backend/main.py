from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Interview Trainer API"}


tasks = [
    {
        "id": 1,
        "title": "Two Sum",
        "difficulty": "easy"
    },
    {
        "id": 2,
        "title": "Palindrome",
        "difficulty": "easy"
    }
]


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_tasks(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": "Task not found"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
