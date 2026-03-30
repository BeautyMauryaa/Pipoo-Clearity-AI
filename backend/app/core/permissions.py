"""
Access Control & Permissions
Enforces who can do what with data
"""

from fastapi import HTTPException, status
from typing import Literal

# ==========================================
# PERMISSION CHECKER
# ==========================================

class PermissionChecker:
    """
    Enforces CRUD permissions based on role and ownership
    """
    
    @staticmethod
    def can_create_onboarding(user_role: str) -> bool:
        """
        Users can create their own onboarding profile
        """
        return user_role in ["student", "professional", "company"]
    
    @staticmethod
    def can_read_own_tasks(user_id: str, task_user_id: str) -> bool:
        """
        Users can only read their own tasks
        """
        return user_id == task_user_id
    
    @staticmethod
    def can_update_task_status(user_id: str, task_user_id: str) -> bool:
        """
        Users can only update status of their own tasks
        System can update any task
        """
        return user_id == task_user_id
    
    @staticmethod
    def can_create_task(role: str) -> bool:
        """
        Only system can create tasks
        In practice, this is called by workspace logic, not user directly
        """
        return role == "system"
    
    @staticmethod
    def can_read_history(user_id: str, history_user_id: str, user_role: str) -> bool:
        """
        Users can read their own history
        Companies can read candidate history (via skill proofs)
        """
        if user_id == history_user_id:
            return True
        
        # Company can read candidate history if linked
        if user_role == "company":
            return True  # Further check in repository
        
        return False
    
    @staticmethod
    def can_read_skill_proofs(user_id: str, candidate_id: str, company_id: str, user_role: str) -> bool:
        """
        Candidates can read their own proofs
        Companies can read proofs they requested
        """
        if user_role == "company" and user_id == company_id:
            return True
        
        if user_role in ["student", "professional"] and user_id == candidate_id:
            return True
        
        return False
    
    @staticmethod
    def can_modify_candidate_data(user_role: str) -> bool:
        """
        Companies can NEVER modify candidate data
        This is critical for trust
        """
        if user_role == "company":
            return False
        return True
    
    @staticmethod
    def verify_ownership(user_id: str, resource_user_id: str, action: str = "access"):
        """
        Verify user owns the resource
        Raises 403 if not owner
        """
        if user_id != resource_user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"You don't have permission to {action} this resource"
            )

# ==========================================
# PERMISSION DECORATORS (Future Enhancement)
# ==========================================

def require_role(allowed_roles: list[str]):
    """
    Decorator to enforce role-based access
    Usage: @require_role(["student", "professional"])
    """
    def decorator(func):
        async def wrapper(*args, current_user: dict, **kwargs):
            if current_user["role"] not in allowed_roles:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"This action requires one of these roles: {allowed_roles}"
                )
            return await func(*args, current_user=current_user, **kwargs)
        return wrapper
    return decorator