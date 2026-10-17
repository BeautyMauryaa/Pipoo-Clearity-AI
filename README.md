# Pipoo Clearity AI

**An open-source career clarity and focus platform.**

Pipoo Clearity AI is a work-in-progress project exploring how people can organize their career direction, skills, goals, and next steps in one place. This repository contains a web application with a Next.js frontend and a FastAPI backend.

> **Project status:** Active development. The repository includes frontend and backend foundations for authentication, onboarding, workspaces, tasks, and history. End-to-end behavior and production readiness still need verification; not every workflow should be assumed complete.

## What this project is

Pipoo Clearity AI is the career clarity platform in this repository. It is separate from any other project that may use a similar name. It is **not** the Python desktop voice assistant.

## Current scope

The codebase includes foundations for:

- **Career onboarding** — capture user goals and context.
- **Workspaces** — organize a user's planning environment.
- **Tasks and focus** — structure next steps and task tracking.
- **Activity history** — access relevant previous activity.
- **Authentication and access control** — backend foundations for authenticated access.

These are the areas represented in the code. Check each workflow in the current implementation before assuming it is fully integrated or production-ready.

## Tech stack

| Layer | Technologies |
|---|---|
| Frontend | Next.js, React, Tailwind CSS |
| Backend | Python, FastAPI, Uvicorn |
| Database | MongoDB, Motor, PyMongo |
| Authentication | JWT, Passlib/Bcrypt |
| Validation and configuration | Pydantic, python-dotenv |
| Local development | Docker, Docker Compose |

## Repository structure

```text
Pipoo-Clearity-AI/
├── frontend/              # Next.js application
├── backend/
│   ├── app/
│   │   ├── core/          # Configuration, security, database setup
│   │   ├── models/        # Data models
│   │   ├── routes/        # API endpoints
│   │   └── services/      # Business logic
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## Getting started

### Prerequisites

- Python 3.10 or newer
- Node.js and npm
- Access to a MongoDB instance (local or hosted)
- Docker Desktop, if you want to use Docker Compose

### 1. Set up the backend

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

Install the dependencies:

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and set the values for your environment, including your MongoDB connection string and a strong, private JWT secret. Keep real credentials out of Git.

Start the API from the `backend/` directory:

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

- API health check: [http://localhost:8000/health](http://localhost:8000/health)
- Interactive API documentation: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### 2. Set up the frontend

Open a second terminal at the repository root:

```bash
cd frontend
npm install
npm run dev
```

Then open [http://localhost:3000](http://localhost:3000).

Configure the frontend's API base URL using the environment variable expected by the code, and point it to your local backend during development.

### 3. Docker Compose

A Compose file is included. Review its environment variables, service configuration, networking, and volumes for your own environment before relying on it. In particular, `localhost` inside a container is not the same as the host machine.

## Open source

Pipoo Clearity AI is published as an open-source project under the repository's **MIT License**.

Contributions, bug reports, and practical suggestions are welcome. Before opening a pull request:

1. Open an issue or describe the change you want to make.
2. Keep changes focused and explain the reason for them.
3. Test the affected flow and include reproduction steps for bug fixes.
4. Never include API keys, database credentials, tokens, personal data, or real `.env` files.

By contributing, you agree that your contributions will be provided under the project's MIT License.

## Security and responsible use

- Store secrets in local environment files or a secure secret manager.
- Do not use placeholder secrets in a deployed environment.
- Restrict CORS to trusted origins outside local development.
- Review authentication, authorization, and user-data ownership checks before exposing the API publicly.
- If you discover a security issue, avoid posting exploitable details publicly; contact the repository owner privately first.

## Current development priorities

- Verify frontend-to-backend user journeys end to end.
- Add automated tests for authentication, onboarding, workspaces, and task APIs.
- Validate database persistence and authorization behavior.
- Test Docker Compose from a clean environment.
- Document a demo or screenshots once the current UI and workflows are ready.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Author

**Beauty Mauryaa (Nova)** · [GitHub](https://github.com/BeautyMauryaa)
