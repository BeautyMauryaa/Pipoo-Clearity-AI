# app/main.py
from app.routes import auth, onboarding, workspace, dev, tasks, history  # Add tasks, history
from app.routes import auth, onboarding, workspace, dev  # Add dev
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import connect_to_mongodb, close_mongodb_connection  # ⭐ NEW
from app.routes import auth, onboarding, workspace

# Create FastAPI app instance
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS (allows frontend to connect)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# INCLUDE ROUTERS
# ==========================================
app.include_router(auth.router, prefix=settings.API_PREFIX)
app.include_router(onboarding.router, prefix=settings.API_PREFIX)
app.include_router(workspace.router, prefix=settings.API_PREFIX)
app.include_router(dev.router, prefix=settings.API_PREFIX, tags=["Dev"])
app.include_router(tasks.router, prefix=settings.API_PREFIX)
app.include_router(history.router, prefix=settings.API_PREFIX)
# ==========================================
# ROOT ENDPOINT (HEALTH CHECK)
# ==========================================
@app.get("/")
def root():
    """
    Root endpoint - Health check
    Returns server status
    """
    return {
        "status": "ok",
        "message": "Clarity AI backend running",
        "version": settings.VERSION,
        "docs": "/docs"
    }

# ==========================================
# HEALTH CHECK ENDPOINT
# ==========================================
@app.get("/health")
def health_check():
    """
    Health check endpoint for monitoring
    """
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION
    }

# ==========================================
# STARTUP EVENT
# ==========================================
@app.on_event("startup")
async def startup_event():
    """
    Runs when server starts
    """
    print("=" * 50)
    print(f"🚀 {settings.PROJECT_NAME} v{settings.VERSION}")
    print(f"📡 Server running on: http://{settings.HOST}:{settings.PORT}")
    print(f"📚 API Docs: http://localhost:{settings.PORT}/docs")
    print(f"🔐 Auth: {settings.API_PREFIX}/auth")
    print(f"📋 Onboarding: {settings.API_PREFIX}/onboarding")
    print(f"🖥️  Workspace: {settings.API_PREFIX}/workspace")
    print("=" * 50)
    
    # ⭐ NEW - Connect to MongoDB
    await connect_to_mongodb()

# ==========================================
# SHUTDOWN EVENT
# ==========================================
@app.on_event("shutdown")
async def shutdown_event():
    """
    Runs when server shuts down
    """
    print("\n👋 Server shutting down...")
    
    # ⭐ NEW - Close MongoDB connection
    await close_mongodb_connection()

# ==========================================
# EXAMPLE: API PREFIX ROUTE
# ==========================================
@app.get(f"{settings.API_PREFIX}/test")
def test_api():
    """
    Test endpoint to verify API prefix works
    """
    return {
        "message": "API test successful",
        "api_prefix": settings.API_PREFIX
    }