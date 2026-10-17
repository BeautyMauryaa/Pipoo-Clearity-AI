# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.database import connect_to_mongodb, close_mongodb_connection
from app.routes import auth, onboarding, workspace, tasks, history

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Application routers. Development-only database utilities are intentionally
# not registered in the application, so the reset endpoint is not exposed.
app.include_router(auth.router, prefix=settings.API_PREFIX)
app.include_router(onboarding.router, prefix=settings.API_PREFIX)
app.include_router(workspace.router, prefix=settings.API_PREFIX)
app.include_router(tasks.router, prefix=settings.API_PREFIX)
app.include_router(history.router, prefix=settings.API_PREFIX)


@app.get("/")
def root():
    """Basic health check."""
    return {
        "status": "ok",
        "message": "Clarity AI backend running",
        "version": settings.VERSION,
        "docs": "/docs",
    }


@app.get("/health")
def health_check():
    """Health check endpoint for monitoring."""
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION,
    }


@app.on_event("startup")
async def startup_event():
    """Connect to the database when the application starts."""
    await connect_to_mongodb()


@app.on_event("shutdown")
async def shutdown_event():
    """Close the database connection when the application stops."""
    await close_mongodb_connection()


@app.get(f"{settings.API_PREFIX}/test")
def test_api():
    """Verify that the API prefix is working."""
    return {
        "message": "API test successful",
        "api_prefix": settings.API_PREFIX,
    }
