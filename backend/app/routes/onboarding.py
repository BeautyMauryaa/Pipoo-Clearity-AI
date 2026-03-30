"""
Onboarding Routes
Handles role-specific onboarding completion with MongoDB persistence
"""

from fastapi import APIRouter, HTTPException, status, Depends
from app.models.onboarding import (
    StudentOnboardingRequest,
    ProfessionalOnboardingRequest,
    CompanyOnboardingRequest,
    OnboardingResponse,
    OnboardingStatusResponse
)
from app.models.database import OnboardingProfileDB, HistoryDB
from app.core.dependencies import (
    get_current_user,
    get_onboarding_repo,
    get_user_repo,
    get_history_repo
)
from app.db.repositories import OnboardingRepository, UserRepository, HistoryRepository
from datetime import datetime
import uuid

router = APIRouter(prefix="/onboarding", tags=["Onboarding"])

# ==========================================
# STUDENT ONBOARDING ENDPOINT
# ==========================================

@router.post("/student", response_model=OnboardingResponse)
async def complete_student_onboarding(
    request: StudentOnboardingRequest,
    current_user: dict = Depends(get_current_user),
    onboarding_repo: OnboardingRepository = Depends(get_onboarding_repo),
    user_repo: UserRepository = Depends(get_user_repo),
    history_repo: HistoryRepository = Depends(get_history_repo)
):
    """
    Save student onboarding data and mark completion
    
    CRUD Permission: User creates their own onboarding profile
    
    Process:
    1. Verify user is student role
    2. Check if onboarding already completed
    3. Save onboarding data to MongoDB
    4. Mark user's onboarding as complete
    5. Log event in history
    6. Return success
    """
    user_id = current_user["user_id"]
    user_role = current_user["role"]
    
    # Verify role matches
    if user_role != "student":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This endpoint is only for students"
        )
    
    # Check if onboarding already completed
    existing_profile = await onboarding_repo.get_profile(user_id)
    if existing_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Onboarding already completed. Use reset endpoint to re-onboard."
        )
    
    # Create onboarding profile document
    profile_data = OnboardingProfileDB(
        user_id=user_id,
        role="student",
        data=request.model_dump(),
        completed_at=datetime.utcnow().isoformat()
    )
    
    # Save to MongoDB
    await onboarding_repo.create_profile(profile_data)
    
    # Mark user's onboarding as complete
    await user_repo.mark_onboarding_complete(user_id)
    
    # Log onboarding completion in history
    history_data = HistoryDB(
        history_id=f"hist_{uuid.uuid4().hex[:12]}",
        user_id=user_id,
        event_type="onboarding_completed",
        description="Student onboarding completed",
        context={
            "role": "student",
            "goal": request.goal,
            "timeline": request.timeline,
            "blocker": request.blocker
        },
        timestamp=datetime.utcnow().isoformat()
    )
    await history_repo.log_event(history_data)
    
    print(f"✅ Student onboarding completed: {current_user['email']}")
    print(f"   Goal: {request.goal}, Timeline: {request.timeline}, Blocker: {request.blocker}")
    
    return OnboardingResponse(
        success=True,
        message="Student onboarding completed successfully",
        user_id=user_id,
        role=user_role,
        onboarding_completed=True
    )

# ==========================================
# PROFESSIONAL ONBOARDING ENDPOINT
# ==========================================

@router.post("/professional", response_model=OnboardingResponse)
async def complete_professional_onboarding(
    request: ProfessionalOnboardingRequest,
    current_user: dict = Depends(get_current_user),
    onboarding_repo: OnboardingRepository = Depends(get_onboarding_repo),
    user_repo: UserRepository = Depends(get_user_repo),
    history_repo: HistoryRepository = Depends(get_history_repo)
):
    """
    Save professional onboarding data and mark completion
    
    CRUD Permission: User creates their own onboarding profile
    
    Process:
    1. Verify user is professional role
    2. Check if onboarding already completed
    3. Save onboarding data to MongoDB
    4. Mark user's onboarding as complete
    5. Log event in history
    6. Return success
    """
    user_id = current_user["user_id"]
    user_role = current_user["role"]
    
    # Verify role matches
    if user_role != "professional":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This endpoint is only for professionals"
        )
    
    # Check if onboarding already completed
    existing_profile = await onboarding_repo.get_profile(user_id)
    if existing_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Onboarding already completed. Use reset endpoint to re-onboard."
        )
    
    # Create onboarding profile document
    profile_data = OnboardingProfileDB(
        user_id=user_id,
        role="professional",
        data=request.model_dump(),
        completed_at=datetime.utcnow().isoformat()
    )
    
    # Save to MongoDB
    await onboarding_repo.create_profile(profile_data)
    
    # Mark user's onboarding as complete
    await user_repo.mark_onboarding_complete(user_id)
    
    # Log onboarding completion in history
    history_data = HistoryDB(
        history_id=f"hist_{uuid.uuid4().hex[:12]}",
        user_id=user_id,
        event_type="onboarding_completed",
        description="Professional onboarding completed",
        context={
            "role": "professional",
            "direction": request.direction,
            "objective": request.objective,
            "blocker": request.blocker
        },
        timestamp=datetime.utcnow().isoformat()
    )
    await history_repo.log_event(history_data)
    
    print(f"✅ Professional onboarding completed: {current_user['email']}")
    print(f"   Direction: {request.direction}, Objective: {request.objective}, Blocker: {request.blocker}")
    
    return OnboardingResponse(
        success=True,
        message="Professional onboarding completed successfully",
        user_id=user_id,
        role=user_role,
        onboarding_completed=True
    )

# ==========================================
# COMPANY ONBOARDING ENDPOINT
# ==========================================

@router.post("/company", response_model=OnboardingResponse)
async def complete_company_onboarding(
    request: CompanyOnboardingRequest,
    current_user: dict = Depends(get_current_user),
    onboarding_repo: OnboardingRepository = Depends(get_onboarding_repo),
    user_repo: UserRepository = Depends(get_user_repo),
    history_repo: HistoryRepository = Depends(get_history_repo)
):
    """
    Save company onboarding data and mark completion
    
    CRUD Permission: User creates their own onboarding profile
    
    Process:
    1. Verify user is company role
    2. Check if onboarding already completed
    3. Save onboarding data to MongoDB
    4. Mark user's onboarding as complete
    5. Log event in history
    6. Return success
    """
    user_id = current_user["user_id"]
    user_role = current_user["role"]
    
    # Verify role matches
    if user_role != "company":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This endpoint is only for companies"
        )
    
    # Check if onboarding already completed
    existing_profile = await onboarding_repo.get_profile(user_id)
    if existing_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Onboarding already completed. Use reset endpoint to re-onboard."
        )
    
    # Create onboarding profile document
    profile_data = OnboardingProfileDB(
        user_id=user_id,
        role="company",
        data=request.model_dump(),
        completed_at=datetime.utcnow().isoformat()
    )
    
    # Save to MongoDB
    await onboarding_repo.create_profile(profile_data)
    
    # Mark user's onboarding as complete
    await user_repo.mark_onboarding_complete(user_id)
    
    # Log onboarding completion in history
    history_data = HistoryDB(
        history_id=f"hist_{uuid.uuid4().hex[:12]}",
        user_id=user_id,
        event_type="onboarding_completed",
        description="Company onboarding completed",
        context={
            "role": "company",
            "company_name": request.company_name,
            "hiring_goal": request.hiring_goal,
            "hiring_challenge": request.hiring_challenge
        },
        timestamp=datetime.utcnow().isoformat()
    )
    await history_repo.log_event(history_data)
    
    print(f"✅ Company onboarding completed: {current_user['email']}")
    print(f"   Company: {request.company_name}, Goal: {request.hiring_goal}")
    
    return OnboardingResponse(
        success=True,
        message="Company onboarding completed successfully",
        user_id=user_id,
        role=user_role,
        onboarding_completed=True
    )

# ==========================================
# GET ONBOARDING STATUS
# ==========================================

@router.get("/status", response_model=OnboardingStatusResponse)
async def get_onboarding_status(
    current_user: dict = Depends(get_current_user),
    onboarding_repo: OnboardingRepository = Depends(get_onboarding_repo)
):
    """
    Check if user has completed onboarding
    
    CRUD Permission: User reads their own onboarding status
    
    Returns onboarding status and data if completed
    """
    user_id = current_user["user_id"]
    user_role = current_user["role"]
    
    # Get onboarding profile from MongoDB
    profile = await onboarding_repo.get_profile(user_id)
    
    return OnboardingStatusResponse(
        user_id=user_id,
        role=user_role,
        onboarding_completed=profile is not None,
        onboarding_data=profile.get("data") if profile else None
    )

# ==========================================
# RESET ONBOARDING (Development/Testing)
# ==========================================

@router.delete("/reset")
async def reset_onboarding(
    current_user: dict = Depends(get_current_user),
    onboarding_repo: OnboardingRepository = Depends(get_onboarding_repo),
    user_repo: UserRepository = Depends(get_user_repo),
    history_repo: HistoryRepository = Depends(get_history_repo)
):
    """
    Reset user's onboarding status
    
    CRUD Permission: User can reset their own onboarding
    
    Useful for testing and development
    This allows users to re-onboard if they made mistakes
    """
    user_id = current_user["user_id"]
    
    # Delete onboarding profile from MongoDB
    from app.core.database import get_database, Collections
    db = get_database()
    await db[Collections.ONBOARDING_PROFILES].delete_one({"user_id": user_id})
    
    # Mark user's onboarding as incomplete
    await user_repo.update_user(user_id, {"onboarding_completed": False})
    
    # Log reset event
    history_data = HistoryDB(
        history_id=f"hist_{uuid.uuid4().hex[:12]}",
        user_id=user_id,
        event_type="other",
        description="Onboarding reset",
        context={"action": "reset_onboarding"},
        timestamp=datetime.utcnow().isoformat()
    )
    await history_repo.log_event(history_data)
    
    print(f"⚠️ Onboarding reset for: {current_user['email']}")
    
    return {
        "success": True,
        "message": "Onboarding reset successfully",
        "onboarding_completed": False
    }