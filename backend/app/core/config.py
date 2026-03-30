# app/core/config.py
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Settings:
    """
    Application settings and configuration
    """
    # Project Info
    PROJECT_NAME: str = "Clarity AI Backend"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Backend API for Clarity AI - Career clarity, skill proof, and focus platform"
    
    # Server Config
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # CORS Settings (for frontend connection)
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000")
    ALLOWED_ORIGINS: list = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]
    
    # API Settings
    API_PREFIX: str = "/api"
    
    # JWT Settings
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "your-secret-key-change-in-production")
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_MINUTES: int = 1440  # 24 hours
    
    # Database Settings
    MONGODB_URL: str = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "clarity_ai")
    
    # Debug Mode
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"

# Create settings instance
settings = Settings()

# Print confirmation on load
if settings.DEBUG:
    print(f"✅ Config loaded - {settings.PROJECT_NAME} v{settings.VERSION}")