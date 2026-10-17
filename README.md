# Pipoo Clearity AI ✨

A career clarity and focus platform I'm building to help turn goals into clearer next steps.

## 🤝 Want to build this together?

This is an open-source project, and I'd genuinely love for it to grow with ideas from other students and developers.

Have an idea that could make the project more useful? Want to try a feature, improve the UI, debug something, learn a new stack, or just build alongside someone who's also learning? **You're welcome here.** You don't need to be an expert or have a perfect first contribution. We can learn, experiment, review each other's work, fix bugs, and improve the project together.

📩 **Email me:** [beautymaurya9142@gmail.com](mailto:beautymaurya9142@gmail.com)

A quick note about your idea or the part you'd like to work on is enough. You can also open a GitHub issue to suggest a feature or report a bug.

## 💡 What is Pipoo Clearity AI?

Career planning can get messy: you have goals, skills you want to learn, tasks to finish, and lots of possible next steps. This project explores bringing that work into one place, so users can organize their direction and turn broad goals into manageable actions.

The current codebase has a **Next.js web frontend** and a **FastAPI backend** with MongoDB integration. It's still a work in progress, so some areas may be incomplete or need more testing. I'm building and improving it step by step, and that's part of the reason I'm opening it up to collaboration.

> **Important:** This repository is the career clarity web platform. It is separate from any other project that shares the name “Pipoo Clearity AI,” including a Python desktop assistant. The projects are unrelated and their code and features are not shared.

## 🧭 Current direction

The repository includes foundations for these areas:

- **Career onboarding** — gather a user's goals and context.
- **Workspaces** — keep planning and related work organized.
- **Tasks and next steps** — break plans into smaller actions.
- **Activity history** — revisit relevant previous activity.
- **Authentication** — backend foundations for protected user access.

These describe the project's current direction and codebase, not a promise that every flow is already complete. If you spot something unfinished or inconsistent, feedback and fixes are very welcome.

## 🛠️ Tech stack

| Area | Technologies |
| --- | --- |
| Frontend | Next.js, React, Tailwind CSS |
| Backend API | Python, FastAPI, Uvicorn |
| Database | MongoDB, Motor, PyMongo |
| Authentication and security foundations | JWT, Passlib, Bcrypt |
| Validation and configuration | Pydantic, python-dotenv |
| Local development | Docker, Docker Compose |

## 📁 Project structure

```text
Pipoo-Clearity-AI/
├── frontend/                 # Next.js web application
├── backend/
│   ├── app/
│   │   ├── core/             # Configuration, security, database setup
│   │   ├── models/            # Data models
│   │   ├── routes/            # API endpoints
│   │   └── services/          # Application/business logic
│   ├── tests/                 # Backend tests
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
├── .gitignore
├── LICENSE
└── README.md
```

## 🚀 Run it locally

You'll need Python 3.10+, Node.js with npm, and access to a MongoDB instance. Docker Desktop is optional if you want to use Docker Compose.

### 1. Clone the repository

```bash
git clone https://github.com/BeautyMauryaa/Pipoo-Clearity-AI.git
cd Pipoo-Clearity-AI
```

### 2. Start the backend

```bash
cd backend
python -m venv .venv
```

Activate the virtual environment.

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

Create your local environment file using the variables expected by the backend configuration. Set your MongoDB connection string and a strong JWT secret. Never commit real credentials or your `.env` file.

Start the API from the `backend/` directory:

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

If the application starts successfully, try the API docs at [http://localhost:8000/docs](http://localhost:8000/docs). The health endpoint is available at [http://localhost:8000/health](http://localhost:8000/health) if it is enabled in your current checkout.

### 3. Start the frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

If the frontend needs an API base URL, configure the environment variable used by the current frontend code and point it to your local backend. Check the project's existing configuration before adding a new variable.

### 4. Using Docker Compose

A `docker-compose.yml` file is included for local development. Review the services and environment variables in that file before running it. Make sure database URLs, ports, and credentials match your local setup; `localhost` inside a container refers to that container, not automatically to your host machine.

## 🌱 Ways to contribute

You can contribute in a way that matches your interests and experience:

- Share a practical feature idea or a better user flow.
- Improve layout, accessibility, responsive behavior, or UI consistency.
- Help connect frontend screens to backend APIs.
- Add or improve validation, error handling, and loading states.
- Write tests, reproduce bugs, and help debug issues.
- Improve setup instructions or add useful documentation.
- Review a pull request and share constructive feedback.

### First contribution? Start here

1. Explore the repository and run the part you're interested in.
2. Check the open issues, or open one to discuss your idea before starting a larger change.
3. Fork the repository and create a branch for your change.
4. Keep the change focused and explain what it improves.
5. Test what you changed and open a pull request with a short summary and testing notes.

No pressure to know everything already. Asking questions and learning as you go are part of the process.

## 🔐 A few security basics

- Keep API keys, passwords, database credentials, and tokens out of commits.
- Use a strong, private JWT secret in your own environment.
- Review authentication, authorization, and user-data access before deploying publicly.
- Use trusted CORS origins for anything beyond local development.
- Please report security concerns privately instead of posting exploitable details in a public issue.

## 🗺️ What's next?

Some useful areas to keep improving are end-to-end testing, reliable frontend/backend integration, authorization checks, clear error states, and a smoother setup experience. If you have a different idea that fits the project's purpose, I'd love to hear it—open source is better when people can bring different perspectives.

## 📄 License

This project is available under the MIT License. See [LICENSE](LICENSE) for the full text.

---

Built in public by [Beauty Mauryaa](https://github.com/BeautyMauryaa). Learning as I go, and happy to build with others. 🌱
