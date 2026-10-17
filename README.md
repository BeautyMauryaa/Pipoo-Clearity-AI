# Pipoo Clearity AI ✨

**A little space to figure things out, stay focused, and take the next step.**

Pipoo Clearity AI is an open-source career clarity and focus platform I'm building with the idea of making goals and next steps feel a bit less overwhelming.

## 🤝 Got an idea? Let's build it together.

This project is open source, so if you're a student or developer who wants to learn by building, you're in the right place.

Got a feature idea? Found a weird bug? Want to try something, fix something, or just figure it out together? Jump in. We can share ideas, debug things, improve the project, and learn as we go.

- 💡 **Got an idea?** [Open an issue](https://github.com/BeautyMauryaa/Pipoo-Clearity-AI/issues) and tell me about it.
- 🐛 **Found a bug?** Share what happened and how to reproduce it.
- 🛠️ **Want to contribute?** Explore the code and open a pull request.
- 🌱 **Still learning?** Same energy. You don't need to know everything to get started.

No gatekeeping, no need to be an expert. Let's learn, build, debug, and grow together.

**Want to reach me?** Add your public email here: `your-email@example.com`

## 💭 What is it?

The goal is to bring career planning and focused action into one place—so it's easier to make sense of where you're going and what you can do next.

The codebase is a work in progress. It includes foundations for onboarding, workspaces, tasks, and activity history; some flows may still need wiring, testing, or improvement.

> Heads-up: this repo is the **career clarity web platform**. It's a separate project from the Python desktop voice assistant, even though the names are similar.

## 🧰 The stack

- **Frontend:** Next.js, React, Tailwind CSS
- **Backend:** Python, FastAPI, Uvicorn
- **Database:** MongoDB, Motor, PyMongo
- **Auth & validation:** JWT, Passlib/Bcrypt, Pydantic
- **Dev setup:** Docker, Docker Compose

## 📁 Project layout

```text
Pipoo-Clearity-AI/
├── frontend/       # Next.js app
├── backend/        # FastAPI app, routes, models and services
├── docker-compose.yml
└── README.md
```

## 🚀 Run it locally

You'll need **Python 3.10+**, **Node.js/npm**, and access to MongoDB.

### 1. Backend

```bash
cd backend
python -m venv .venv
```

Activate the virtual environment:

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

Set up your environment variables using the example file if provided. Add your MongoDB URL and a strong JWT secret. Keep real secrets out of Git.

Start the API from the `backend/` directory:

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

If the app's health route is configured, check [localhost:8000/health](http://localhost:8000/health). API docs are usually available at [localhost:8000/docs](http://localhost:8000/docs).

### 2. Frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Open [localhost:3000](http://localhost:3000). Make sure the frontend API URL points to your local backend.

### 3. Docker

There's a Docker Compose setup to explore, too. Check the environment variables and service settings before running it, and don't use development secrets in production.

## 🌱 What needs love next?

- Test the main user flows from frontend to backend
- Add and improve tests
- Check authentication and user-data access carefully
- Make local setup smoother for new contributors
- Keep improving the experience based on real feedback

If you work on something, please mention what you changed and how you tested it. Small, clear contributions are very welcome.

## 📄 License

This project is shared under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Built by [Beauty Mauryaa](https://github.com/BeautyMauryaa), with room for others to jump in.
