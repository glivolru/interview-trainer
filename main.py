from fastapi import FastAPI

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
