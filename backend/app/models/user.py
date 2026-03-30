# app/models/user.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal
from datetime import datetime

# ==========================================
# USER ROLE TYPE
# ==========================================
UserRole = Literal["student", "professional", "company"]

# ==========================================
# REQUEST MODELS (Input from frontend)
# ==========================================

class SignupRequest(BaseModel):
    """
    Data required for user signup
    """
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8)
    role: UserRole
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com",
                "password": "securepass123",
                "role": "student"
            }
        }

class LoginRequest(BaseModel):
    """
    Data required for user login
    """
    email: EmailStr
    password: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "email": "john@example.com",
                "password": "securepass123"
            }
        }

# ==========================================
# RESPONSE MODELS (Output to frontend)
# ==========================================

class UserResponse(BaseModel):
    """
    User data returned to frontend
    NEVER includes password
    """
    id: str
    name: str
    email: EmailStr
    role: UserRole
    onboarding_completed: bool
    created_at: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "user_123",
                "name": "John Doe",
                "email": "john@example.com",
                "role": "student",
                "onboarding_completed": False,
                "created_at": "2024-01-01T00:00:00"
            }
        }

class AuthResponse(BaseModel):
    """
    Response after successful login/signup
    """
    access_token: str
    token_type: str = "bearer"
    user: UserResponse
    
    class Config:
        json_schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "token_type": "bearer",
                "user": {
                    "id": "user_123",
                    "name": "John Doe",
                    "email": "john@example.com",
                    "role": "student",
                    "onboarding_completed": False,
                    "created_at": "2024-01-01T00:00:00"
                }
            }
        }

# ==========================================
# DATABASE MODEL (Internal storage)
# ==========================================

class UserInDB(BaseModel):
    """
    User model as stored in database
    Includes hashed password (never sent to frontend)
    """
    id: str
    name: str
    email: EmailStr
    hashed_password: str  # NEVER send this to frontend
    role: UserRole
    onboarding_completed: bool = False
    onboarding_data: Optional[dict] = None
    created_at: str
    updated_at: Optional[str] = None