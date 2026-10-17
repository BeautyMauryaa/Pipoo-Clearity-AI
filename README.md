# Pipoo-Clearity-AI — Career Clarity & Focus Platform

Pipoo-Clearity-AI is a work-in-progress platform for helping people organize their career direction, skills, and next steps. It brings together a Next.js frontend and a FastAPI backend foundation.

> **Status:** In active development. The codebase includes the frontend, API routes, authentication foundations, workspace/task flows, and MongoDB integration. End-to-end workflows and production readiness still need to be verified; this project is not presented as production-ready.

## What it aims to support

- **Career onboarding:** Capture a user's goals and context.
- **Workspaces:** Organize the experience around a user's working context.
- **Tasks and focus:** Provide a structure for planning and tracking next steps.
- **History:** Keep a record of relevant activity.
- **Authentication and access control:** Backend foundations for authenticated access.

These describe the project's intended workflows. Check the implementation and current API behavior before assuming every flow is complete.

## Tech stack

| Layer | Technologies |
|---|---|
| Frontend | Next.js, React, Tailwind CSS |
| Backend | Python, FastAPI, Uvicorn |
| Database | MongoDB, Motor, PyMongo |
| Authentication | JWT, Passlib/Bcrypt |
| Configuration and validation | Pydantic, python-dotenv |
| Local development | Docker, Docker Compose |

## Repository structure

```text
Pipoo-Clearity-AI/
├── frontend/          # Next.js application
├── backend/
│   ├── app/
│   │   ├── core/      # Configuration, security, and database setup
│   │   ├── models/    # Data models
│   │   ├── routes/    # API endpoints
│   │   └── services/  # Business logic
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## Run locally

### Requirements

- Python 3.10+
- Node.js and npm
- A MongoDB instance (local or hosted)
- Docker Desktop, if using Docker Compose

### 1. Configure the backend

From the repository root:

```bash
cd backend
python -m venv .venv
```

Activate the environment.

**Windows PowerShell**
```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and set the values for your environment. Use your own MongoDB connection string and a strong, private JWT secret. Never commit real credentials.

Start the backend from the `backend/` directory:

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

- API health check: [http://localhost:8000/health](http://localhost:8000/health)
- Interactive API docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### 2. Configure the frontend

Open a second terminal at the repository root:

```bash
cd frontend
npm install
npm run dev
```

Then open [http://localhost:3000](http://localhost:3000).

Configure any frontend API base URL using the environment variable expected by the frontend code. Confirm that it points to your local backend during local development.

### 3. Docker Compose

A Compose file is included, but verify its environment variables, service health, and volume/network configuration in your own environment before relying on it.

## Security notes

- Keep real secrets in local environment files; do not commit them.
- Do not use placeholder JWT secrets in deployments.
- Restrict CORS to the origins you actually use outside local development.
- Review authentication, authorization, and data ownership checks before exposing the API publicly.

## Next steps

- Verify the main frontend-to-backend user journeys.
- Add automated tests for authentication, onboarding, workspaces, and task APIs.
- Validate database persistence and access-control behavior.
- Test Docker Compose from a clean environment.
- Document a demo or screenshots once the current UI and workflows are ready.

## Author

**Beauty Mauryaa (Nova)** · [GitHub](https://github.com/BeautyMauryaa)
