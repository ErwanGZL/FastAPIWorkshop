import sqlite3
from pathlib import Path

from fastapi import Body, FastAPI, Form, Request
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=str(Path(__file__).resolve().parent / "static")),
    name="static",
)

templates = Jinja2Templates(
    directory=str(Path(__file__).resolve().parent / "templates")
)

db = sqlite3.connect("todo.db")

# Check if table 'tasks' exists and create it if it doesn't
cursor = db.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks'")
if not cursor.fetchone():
    cursor.execute(
        "CREATE TABLE tasks (id INTEGER PRIMARY KEY, name TEXT NOT NULL, done BOOLEAN NOT NULL DEFAULT 0)"
    )
    db.commit()


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    tasks = db.execute("SELECT * FROM tasks").fetchall()
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "todolist": tasks,
        },
    )


@app.post("/task/new", response_class=RedirectResponse)
async def create_task(request: Request, task_name: str = Form(...)):
    # Add the new task to the database
    cursor = db.cursor()
    cursor.execute("INSERT INTO tasks (name) VALUES (?)", (task_name,))
    db.commit()

    # Redirect to the index page
    return RedirectResponse("/", status_code=303)


@app.post("/task/delete")
async def delete_task(task_id: int = Body(embed=True)):
    # Delete the task from the database
    cursor = db.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    db.commit()

    # Return a success message
    return {"message": "Task deleted successfully"}


@app.post("/task/toggle")
async def toggle_task(task_id: int = Body(embed=True)):
    # Toggle the task in the database
    cursor = db.cursor()
    cursor.execute("UPDATE tasks SET done = NOT done WHERE id=?", (task_id,))
    db.commit()

    # Return a success message
    return {"message": "Task toggled successfully"}
