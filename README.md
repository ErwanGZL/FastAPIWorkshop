# Workshop FastAPI WebServer

This is a small server app presenting a todo list interface to a `sqlite` database.

**Using:**
- `FastAPI`
- `Jinja2`
- `Sqlite3`

## Start

### Activate the virtual environment
```console copy
python -m venv .venv
source .venv/bin/activate
```

### Install the dependencies
```console copy
pip install -r requirements.txt
```

### Start the server

```console copy
uvicorn app.main:app --reload
```
Checkout on http://localhost:8000 (default port)
