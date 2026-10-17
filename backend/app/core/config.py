# app/core/config.py
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def _required_jwt_secret() -> str:
    """Require a private JWT signing secret instead of silently using a public default."""
    secret = os.getenv("JWT_SECRET_KEY", "").strip()
    placeholder_values = {
        "",
        "your-secret-key-change-in-production",
        "replace-with-a-long-random-secret",
        "changeme",
        "change-me",
    }
    if secret.lower() in placeholder_values or len(secret) < 32:
        raise RuntimeError(
            "JWT_SECRET_KEY must be set to a private random value of at least 32 characters. "
            "Generate one with: python -c \"import secrets; print(secrets.token_urlsafe(48))\""
        )
    return secret


class Settings:
    """Application settings and configuration."""

    # Project info
    PROJECT_NAME: str = "Clarity AI Backend"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Backend API for Clarity AI - Career clarity, skill proof, and focus platform"

    # Server config
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # CORS settings
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000").strip().rstrip("/")
    ALLOWED_ORIGINS: list = list(
        dict.fromkeys(
            [
                "http://localhost:3000",
                "http://127.0.0.1:3000",
                FRONTEND_URL,
            ]
        )
    )

    # API settings
    API_PREFIX: str = "/api"

    # JWT settings
    JWT_SECRET_KEY: str = _required_jwt_secret()
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_MINUTES: int = 1440  # 24 hours

    # Database settings
    MONGODB_URL: str = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "clarity_ai")

    # Debug mode must be explicitly enabled for local development
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"


settings = Settings()

if settings.DEBUG:
    print(f"Config loaded - {settings.PROJECT_NAME} v{settings.VERSION}")
