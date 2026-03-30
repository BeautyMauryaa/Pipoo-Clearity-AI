"""
Workspace Routes
Handles workspace data for all three roles with MongoDB persistence
"""

from fastapi import APIRouter, HTTPException, status, Depends, Query
from app.models.workspace import WorkspaceDataResponse, ALLOWED_VIEWS
from app.services.workspace_service import WorkspaceService  # Use the class
from app.core.dependencies import (
    get_current_user,
    get_user_repo,
    get_onboarding_repo,
    get_task_repo,
    get_history_repo
)
from app.db.repositories import (
    UserRepository,
    OnboardingRepository,
    TaskRepository,
    HistoryRepository
)

router = APIRouter(prefix="/workspace", tags=["Workspace"])

# ==========================================
# SINGLE WORKSPACE ENDPOINT (OPTION A)
# ==========================================

@router.get("", response_model=WorkspaceDataResponse)
async def get_workspace(
    view: str = Query(..., description="Workspace view to load (overview, career, focus, etc.)"),
    current_user: dict = Depends(get_current_user),
    user_repo: UserRepository = Depends(get_user_repo),
    onboarding_repo: OnboardingRepository = Depends(get_onboarding_repo),
    task_repo: TaskRepository = Depends(get_task_repo),
    history_repo: HistoryRepository = Depends(get_history_repo)
):
    """
    Get workspace data for specific view
    
    NOW WITH DATABASE LOGIC:
    1. Reads onboarding profile from MongoDB
    2. Reads user's tasks from MongoDB
    3. Reads recent history from MongoDB
    4. Decides what to show based on real state
    5. Creates new tasks if needed
    6. Logs Pipoo insights
    
    Examples:
    - GET /api/workspace?view=overview
    - GET /api/workspace?view=career
    - GET /api/workspace?view=focus
    """
    user_id = current_user["user_id"]
    user_role = current_user["role"]
    
    # Get user from MongoDB
    user = await user_repo.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Check if onboarding is complete
    if not user.get("onboarding_completed", False):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Please complete onboarding first"
        )
    
    # Validate view is allowed for role
    allowed_views = ALLOWED_VIEWS.get(user_role, [])
    if view not in allowed_views:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"View '{view}' not allowed for role '{user_role}'. Allowed views: {allowed_views}"
        )
    
    # Get onboarding profile from MongoDB
    onboarding_profile = await onboarding_repo.get_profile(user_id)
    if not onboarding_profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Onboarding profile not found"
        )
    
    onboarding_data = onboarding_profile.get("data", {})
    
    # Initialize workspace service with repositories
    workspace_service = WorkspaceService(
        user_repo=user_repo,
        onboarding_repo=onboarding_repo,
        task_repo=task_repo,
        history_repo=history_repo
    )
    
    # Call service layer with DATABASE LOGIC
    try:
        workspace_data = await workspace_service.get_workspace_data(
            user_id=user_id,
            role=user_role,
            view=view,
            onboarding_data=onboarding_data
        )
        
        print(f"✅ Workspace data served: {user_role}/{view} for {user['email']}")
        
        return workspace_data
    
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        print(f"❌ Error generating workspace data: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate workspace data"
        )

# ==========================================
# GET ALLOWED VIEWS FOR CURRENT USER
# ==========================================

@router.get("/views")
async def get_allowed_views(current_user: dict = Depends(get_current_user)):
    """
    Get list of allowed views for current user's role
    Useful for frontend to know what sidebar items to show
    """
    user_role = current_user["role"]
    allowed_views = ALLOWED_VIEWS.get(user_role, [])
    
    return {
        "role": user_role,
        "allowed_views": allowed_views
    }

# ==========================================
# WORKSPACE INFO ENDPOINT
# ==========================================

@router.get("/info")
async def get_workspace_info(
    current_user: dict = Depends(get_current_user),
    user_repo: UserRepository = Depends(get_user_repo)
):
    """
    Get basic workspace information
    Returns role, onboarding status, and allowed views
    """
    user_id = current_user["user_id"]
    user_role = current_user["role"]
    
    # Get fresh user data from MongoDB
    user = await user_repo.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return {
        "user_id": user_id,
        "role": user_role,
        "onboarding_completed": user.get("onboarding_completed", False),
        "allowed_views": ALLOWED_VIEWS.get(user_role, []),
        "workspace_ready": user.get("onboarding_completed", False)
    }