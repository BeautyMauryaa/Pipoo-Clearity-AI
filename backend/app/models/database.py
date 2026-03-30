# app/models/database.py
"""
Database Schema Definitions
These models define how data is stored in MongoDB
"""

from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any, Literal
from datetime import datetime

# ==========================================
# 1. USER DOCUMENT
# ==========================================

class UserDB(BaseModel):
    """
    User document stored in MongoDB
    Collection: users
    
    Purpose: Identity & access
    """
    user_id: str  # Unique user identifier
    name: str
    email: EmailStr
    hashed_password: str
    role: Literal["student", "professional", "company"]
    onboarding_completed: bool = False
    created_at: str
    updated_at: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "user_abc123",
                "name": "John Doe",
                "email": "john@example.com",
                "hashed_password": "$2b$12$...",
                "role": "student",
                "onboarding_completed": True,
                "created_at": "2024-01-01T00:00:00",
                "updated_at": "2024-01-02T00:00:00"
            }
        }

# ==========================================
# 2. ONBOARDING PROFILE DOCUMENT
# ==========================================

class OnboardingProfileDB(BaseModel):
    """
    Onboarding profile document
    Collection: onboarding_profiles
    
    Purpose: Context snapshot (one per user)
    """
    user_id: str  # Foreign key to users
    role: Literal["student", "professional", "company"]
    data: Dict[str, Any]  # Role-specific onboarding answers
    completed_at: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "user_abc123",
                "role": "student",
                "data": {
                    "goal": "job-ready",
                    "timeline": "6-12m",
                    "blocker": "consistency"
                },
                "completed_at": "2024-01-01T00:00:00"
            }
        }

# ==========================================
# 3. TASK DOCUMENT
# ==========================================

class TaskDB(BaseModel):
    """
    Task document
    Collection: tasks
    
    Purpose: Execution tracking
    """
    task_id: str  # Unique task identifier
    user_id: str  # Foreign key to users
    title: str
    description: Optional[str] = None
    task_type: Literal["daily", "skill", "optional", "micro"]
    difficulty: Optional[Literal["easy", "medium", "hard"]] = None
    estimated_time: str
    assigned_date: str
    due_date: Optional[str] = None
    completed: bool = False
    completed_at: Optional[str] = None
    skipped: bool = False
    skipped_reason: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "task_id": "task_xyz789",
                "user_id": "user_abc123",
                "title": "Set up development environment",
                "task_type": "daily",
                "estimated_time": "30-40 minutes",
                "assigned_date": "2024-01-01",
                "completed": True,
                "completed_at": "2024-01-01T14:30:00"
            }
        }

# ==========================================
# 4. HISTORY DOCUMENT
# ==========================================

class HistoryDB(BaseModel):
    """
    History/Activity log document
    Collection: history
    
    Purpose: Accountability & audit trail
    """
    history_id: str  # Unique history entry identifier
    user_id: str  # Foreign key to users
    event_type: Literal[
        "task_completed", 
        "task_skipped", 
        "skill_proof_completed", 
        "evaluation_flagged",
        "onboarding_completed",
        "login",
        "other"
    ]
    description: str
    context: Optional[Dict[str, Any]] = None  # Additional context data
    timestamp: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "history_id": "hist_123",
                "user_id": "user_abc123",
                "event_type": "task_completed",
                "description": "Completed Python setup task",
                "context": {
                    "task_id": "task_xyz789",
                    "view": "overview"
                },
                "timestamp": "2024-01-01T14:30:00"
            }
        }

# ==========================================
# 5. SKILL PROOF DOCUMENT (Company)
# ==========================================

class SkillProofDB(BaseModel):
    """
    Skill proof document
    Collection: skill_proofs
    
    Purpose: Hiring trust & candidate evaluation
    """
    proof_id: str  # Unique proof identifier
    candidate_id: str  # Candidate identifier (can be user_id or external)
    company_id: str  # Company that requested evaluation
    task_name: str
    task_type: str
    score: int  # 0-100
    flags: list[str] = []  # ["plagiarism", "ai-assisted", "pattern-match"]
    submitted_at: str
    evaluated_at: str
    evaluation_data: Optional[Dict[str, Any]] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "proof_id": "proof_456",
                "candidate_id": "candidate_789",
                "company_id": "company_abc",
                "task_name": "Python Logic Test",
                "task_type": "coding",
                "score": 75,
                "flags": ["ai-assisted"],
                "submitted_at": "2024-01-01T10:00:00",
                "evaluated_at": "2024-01-01T10:05:00"
            }
        }