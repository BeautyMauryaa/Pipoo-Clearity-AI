# Clarity AI Backend

FastAPI backend for the Clarity AI career-clarity and focus platform. This service is under active development; not every planned workflow is complete yet.

## Stack

- FastAPI + Uvicorn
- MongoDB via Motor/PyMongo
- Pydantic and python-dotenv for configuration
- JWT-based authentication foundation

## Run locally

Requires Python 3.10+ and a MongoDB instance.

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   **Windows PowerShell:** `.\.venv\Scripts\Activate.ps1`  
   **macOS/Linux:** `source .venv/bin/activate`

2. Install packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and set your MongoDB URL and a unique random JWT secret. For local development, the example values assume MongoDB is available on your machine.

4. Start the API from the `backend/` directory:

   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

## Useful endpoints

- Root/health status: [http://localhost:8000/health](http://localhost:8000/health)
- Interactive API docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Configuration

See `.env.example` for the configuration keys read by the backend:

- `MONGODB_URL` and `DATABASE_NAME` — database connection
- `JWT_SECRET_KEY` — signing secret; replace the example with a strong, unique value
- `FRONTEND_URL` — frontend URL
- `DEBUG` — use `false` outside local development

Do not commit your actual `.env` file or real credentials.

## Development status

The application has route modules for authentication, onboarding, workspace, tasks, and history. Complete and test each workflow before treating the backend as production-ready.
