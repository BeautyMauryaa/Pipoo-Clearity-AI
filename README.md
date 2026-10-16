# Clarity AI — Career Clarity & Focus Platform

Clarity AI is a work-in-progress platform exploring how people can get clearer about career direction, skills, and what to focus on next. The repository contains a Next.js frontend and a FastAPI backend foundation.

> **Status:** Active development. The landing page and backend foundation are in place, but some API workflows, integrations, and deployment details are still being completed. This is not presented as a production-ready application.

## What’s in the repository

- **Frontend:** Landing page built with Next.js and React, with reusable sections for the problem, solution, workflow, audience, and calls to action.
- **Backend:** FastAPI application with API routing for authentication, onboarding, workspace, tasks, and history.
- **Persistence:** MongoDB integration using Motor/PyMongo.
- **Security foundation:** JWT configuration and CORS middleware.
- **API docs:** FastAPI Swagger UI and ReDoc.

## Tech stack

| Area | Technologies |
|---|---|
| Frontend | Next.js, React, Tailwind CSS |
| Backend | Python, FastAPI, Uvicorn |
| Database | MongoDB, Motor, PyMongo |
| Authentication | JWT, Passlib/Bcrypt |
| Validation & configuration | Pydantic, python-dotenv |
| Containers | Docker Compose files are provided; see the setup notes below |

## Project structure

```text
Pipoo-Clearity-AI/
├── backend/
│   ├── app/
│   │   ├── core/       # Configuration and database connection
│   │   └── routes/     # API routers
│   ├── requirements.txt
│   ├── Dockerfile
│   └── README.md
├── frontend/
│   ├── app/            # Next.js app routes and page components
│   ├── components/
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## Run locally

### 1. Start the backend

You need Python 3.10+ and access to a MongoDB instance. From the repository root:

```bash
cd backend
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**
```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install dependencies and prepare the environment:

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and replace the placeholder values. Then run:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend URLs:
- Health check: [http://localhost:8000/health](http://localhost:8000/health)
- API docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### 2. Start the frontend

Open a second terminal from the repository root:

```bash
cd frontend
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

## Environment and security

- Keep credentials in local `.env` files; do not commit them.
- Use a unique, long random value for `JWT_SECRET_KEY`. Never use the placeholder from `.env.example` in a real deployment.
- Set `DEBUG=false` outside local development.
- For containers, configure `MONGODB_URL` to a MongoDB address reachable from the backend container. A host machine's `localhost` is not the same as the container's `localhost`.

## Current next steps

- Complete and verify the frontend-to-backend workflows.
- Add automated tests for core API behavior.
- Review authentication, CORS, and production configuration.
- Verify the Docker setup in a clean environment before relying on it for deployment.

## Author

**Beauty Mauryaa (Nova)** · [GitHub](https://github.com/BeautyMauryaa)
