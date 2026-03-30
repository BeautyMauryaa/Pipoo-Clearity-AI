# # app/core/dependencies.py
# from fastapi import Depends, HTTPException, status
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# from app.core.security import decode_access_token
# from typing import Optional

# # HTTP Bearer token scheme
# security = HTTPBearer()

# # ==========================================
# # GET CURRENT USER FROM TOKEN
# # ==========================================

# async def get_current_user(
#     credentials: HTTPAuthorizationCredentials = Depends(security)
# ) -> dict:
#     """
#     Dependency to get current user from JWT token
    
#     This function:
#     1. Extracts token from Authorization header
#     2. Decodes and validates token
#     3. Returns user data if valid
#     4. Raises 401 if invalid
    
#     Usage in routes:
#         @app.get("/protected")
#         def protected_route(current_user: dict = Depends(get_current_user)):
#             return {"user_id": current_user["sub"]}
#     """
#     token = credentials.credentials
    
#     # Decode token
#     payload = decode_access_token(token)
    
#     if payload is None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid or expired token",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
    
#     return payload

# # ==========================================
# # OPTIONAL AUTH (doesn't fail if no token)
# # ==========================================

# async def get_current_user_optional(
#     credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)
# ) -> Optional[dict]:
#     """
#     Optional auth - doesn't fail if no token provided
#     Returns None if no token, user data if valid token
#     """
#     if not credentials:
#         return None
    
#     token = credentials.credentials
#     payload = decode_access_token(token)
    
#     return payload

# # ==========================================
# # ROLE-BASED ACCESS CONTROL
# # ==========================================

# def require_role(allowed_roles: list):
#     """
#     Dependency factory for role-based access control
    
#     Usage:
#         @app.get("/student-only")
#         def student_route(
#             current_user: dict = Depends(get_current_user),
#             _: None = Depends(require_role(["student"]))
#         ):
#             return {"message": "Student access granted"}
#     """
#     async def role_checker(current_user: dict = Depends(get_current_user)):
#         user_role = current_user.get("role")
        
#         if user_role not in allowed_roles:
#             raise HTTPException(
#                 status_code=status.HTTP_403_FORBIDDEN,
#                 detail=f"Access forbidden. Required roles: {allowed_roles}"
#             )
        
#         return None
    
#     return role_checker



"""
FastAPI Dependencies
Provides database and repository instances to routes
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security import decode_access_token
from app.core.database import get_database
from app.db.repositories import (
    UserRepository,
    OnboardingRepository,
    TaskRepository,
    HistoryRepository,
    SkillProofRepository
)
from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import Optional

# HTTP Bearer token scheme
security = HTTPBearer()

# ==========================================
# GET CURRENT USER FROM TOKEN
# ==========================================

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncIOMotorDatabase = Depends(get_database)
) -> dict:
    """
    Dependency to get current user from JWT token
    
    This function:
    1. Extracts token from Authorization header
    2. Decodes and validates token
    3. Returns user data if valid
    4. Raises 401 if invalid
    
    Usage in routes:
        @app.get("/protected")
        def protected_route(current_user: dict = Depends(get_current_user)):
            return {"user_id": current_user["sub"]}
    """
    token = credentials.credentials
    
    # Decode token
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    
    # Get user from database
    user_repo = UserRepository(db)
    user = await user_repo.get_user_by_id(payload.get("sub"))
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    return {
        "user_id": user["user_id"],
        "email": user["email"],
        "role": user["role"],
        "onboarding_completed": user.get("onboarding_completed", False)
    }

# ==========================================
# REPOSITORY DEPENDENCIES
# ==========================================

def get_user_repo(db: AsyncIOMotorDatabase = Depends(get_database)) -> UserRepository:
    """Get User Repository"""
    return UserRepository(db)

def get_onboarding_repo(db: AsyncIOMotorDatabase = Depends(get_database)) -> OnboardingRepository:
    """Get Onboarding Repository"""
    return OnboardingRepository(db)

def get_task_repo(db: AsyncIOMotorDatabase = Depends(get_database)) -> TaskRepository:
    """Get Task Repository"""
    return TaskRepository(db)

def get_history_repo(db: AsyncIOMotorDatabase = Depends(get_database)) -> HistoryRepository:
    """Get History Repository"""
    return HistoryRepository(db)

def get_skill_proof_repo(db: AsyncIOMotorDatabase = Depends(get_database)) -> SkillProofRepository:
    """Get Skill Proof Repository"""
    return SkillProofRepository(db)