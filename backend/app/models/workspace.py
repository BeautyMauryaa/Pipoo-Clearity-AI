# app/models/workspace.py
from pydantic import BaseModel
from typing import List, Dict, Optional, Any, Literal

# ==========================================
# PIPOO MESSAGE
# ==========================================

class PipooMessage(BaseModel):
    """Pipoo's contextual message"""
    message: str
    type: Literal["default", "important", "warning"] = "default"

# ==========================================
# TASK MODEL
# ==========================================

class Task(BaseModel):
    """Task structure for workspace"""
    id: str
    title: str
    description: Optional[str] = None
    estimated_time: str
    type: Literal["main", "optional", "micro"]
    difficulty: Optional[Literal["easy", "medium", "hard"]] = None

# ==========================================
# CARD MODEL (Generic)
# ==========================================

class Card(BaseModel):
    """Generic card for insights/metrics"""
    title: str
    content: Dict[str, Any]
    type: Literal["insight", "metric", "status", "warning"]

# ==========================================
# STATUS MODEL
# ==========================================

class WorkspaceStatus(BaseModel):
    """Status information"""
    focus_status: Literal["on-track", "at-risk", "needs-attention"]
    streak: int
    progress: str

# ==========================================
# WORKSPACE DATA RESPONSE
# ==========================================

class WorkspaceDataResponse(BaseModel):
    """
    Main workspace data response
    Used for all roles and views
    """
    role: Literal["student", "professional", "company"]
    view: str
    pipoo: PipooMessage
    data: Dict[str, Any]
    status: Optional[WorkspaceStatus] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "role": "student",
                "view": "overview",
                "pipoo": {
                    "message": "You want to be job-ready in 6–12 months...",
                    "type": "important"
                },
                "data": {
                    "cards": [],
                    "tasks": [],
                    "insights": {}
                },
                "status": {
                    "focus_status": "on-track",
                    "streak": 3,
                    "progress": "Day 3"
                }
            }
        }

# ==========================================
# ALLOWED VIEWS PER ROLE
# ==========================================

ALLOWED_VIEWS = {
    "student": ["overview", "career", "focus", "skillproof", "history"],
    "professional": ["overview", "direction", "focus", "skilledge", "history"],
    "company": ["dashboard", "candidates", "skillproof", "reports", "history"]
}