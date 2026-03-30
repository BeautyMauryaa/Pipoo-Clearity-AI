# app/models/onboarding.py
from pydantic import BaseModel, Field
from typing import List, Optional, Literal

# ==========================================
# STUDENT ONBOARDING DATA
# ==========================================

class StudentOnboardingRequest(BaseModel):
    """
    Onboarding data for students/job seekers
    Controls: task size, pace, strictness
    """
    goal: Literal["job-ready", "internship", "explore"]
    timeline: Literal["3-6m", "6-12m", "no-timeline"]
    time_per_day: Literal["less-1h", "1-2h", "3plus"]
    skill_level: Literal["beginner", "intermediate", "advanced"]
    interests: List[str] = Field(default_factory=list)  # ["ai-ml", "web", "backend", etc.]
    stage: Literal["1st-2nd", "3rd", "final", "graduate"]
    blocker: Literal["consistency", "confusion", "motivation", "time", "getting-started"]
    
    class Config:
        json_schema_extra = {
            "example": {
                "goal": "job-ready",
                "timeline": "6-12m",
                "time_per_day": "1-2h",
                "skill_level": "beginner",
                "interests": ["ai-ml", "web"],
                "stage": "final",
                "blocker": "consistency"
            }
        }

# ==========================================
# PROFESSIONAL ONBOARDING DATA
# ==========================================

class ProfessionalOnboardingRequest(BaseModel):
    """
    Onboarding data for working professionals
    Controls: depth vs breadth, workload, tone
    """
    objective: Literal["improve-role", "switch-role", "increase-output"]
    availability: Literal["weekdays", "weekends", "flexible"]
    time_per_session: Literal["less-1h", "1-2h", "3plus"]
    experience: Literal["0-1y", "1-3y", "3-5y", "5plus"]
    domain: Literal["frontend", "backend", "ai-ml", "data", "product"]
    blocker: Literal["time", "context-switching", "burnout", "unclear-next", "inconsistent"]
    
    class Config:
        json_schema_extra = {
            "example": {
                "objective": "improve-role",
                "availability": "weekdays",
                "time_per_session": "1-2h",
                "experience": "1-3y",
                "domain": "backend",
                "blocker": "context-switching"
            }
        }

# ==========================================
# COMPANY ONBOARDING DATA
# ==========================================

class CompanyOnboardingRequest(BaseModel):
    """
    Onboarding data for companies/recruiters
    Controls: evaluation strictness, filters
    """
    hiring_goal: Literal["screen-candidates", "evaluate-skills", "talent-pool"]
    hiring_frequency: Literal["occasionally", "monthly", "continuous"]
    team_size: Literal["1-5", "6-20", "20plus"]
    seniority_target: Literal["intern", "junior", "mid", "senior"]
    role_types: List[str] = Field(default_factory=list)  # ["frontend", "backend", etc.]
    hiring_challenge: Literal["fake-resumes", "interview-cheating", "skill-fit", "time-consuming", "reliability"]
    
    class Config:
        json_schema_extra = {
            "example": {
                "hiring_goal": "evaluate-skills",
                "hiring_frequency": "monthly",
                "team_size": "6-20",
                "seniority_target": "mid",
                "role_types": ["backend", "ai-ml"],
                "hiring_challenge": "fake-resumes"
            }
        }

# ==========================================
# GENERIC ONBOARDING RESPONSE
# ==========================================

class OnboardingResponse(BaseModel):
    """
    Response after successful onboarding submission
    """
    success: bool
    message: str
    user_id: str
    role: str
    onboarding_completed: bool
    
    class Config:
        json_schema_extra = {
            "example": {
                "success": True,
                "message": "Onboarding completed successfully",
                "user_id": "user_123",
                "role": "student",
                "onboarding_completed": True
            }
        }

# ==========================================
# ONBOARDING STATUS CHECK
# ==========================================

class OnboardingStatusResponse(BaseModel):
    """
    Response for checking if user completed onboarding
    """
    user_id: str
    role: str
    onboarding_completed: bool
    onboarding_data: Optional[dict] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "user_123",
                "role": "student",
                "onboarding_completed": True,
                "onboarding_data": {
                    "goal": "job-ready",
                    "timeline": "6-12m",
                    "blocker": "consistency"
                }
            }
        }