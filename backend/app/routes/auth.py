"""
Authentication Routes
Handles signup, login, and user verification with MongoDB persistence
"""

from fastapi import APIRouter, HTTPException, status, Depends
from app.models.user import SignupRequest, LoginRequest, AuthResponse, UserResponse
from app.models.database import UserDB, HistoryDB
from app.core.security import hash_password, verify_password, create_access_token
from app.core.dependencies import (
    get_current_user,
    get_user_repo,
    get_history_repo
)
from app.db.repositories import UserRepository, HistoryRepository
from datetime import datetime
import uuid

router = APIRouter(prefix="/auth", tags=["Authentication"])

# ==========================================
# SIGNUP ENDPOINT
# ==========================================

@router.post("/signup", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
async def signup(
    request: SignupRequest,
    user_repo: UserRepository = Depends(get_user_repo),
    history_repo: HistoryRepository = Depends(get_history_repo)
):
    """
    Register a new user
    
    CRUD Permission: User creates their own identity
    
    Process:
    1. Check if email already exists
    2. Hash password (never store plain text)
    3. Create user record in MongoDB
    4. Log signup event in history
    5. Generate JWT token
    6. Return token + user data
    """
    # Check if email already exists
    existing_user = await user_repo.get_user_by_email(request.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Generate unique user ID
    user_id = f"user_{uuid.uuid4().hex[:12]}"
    
    # Hash password
    hashed_password = hash_password(request.password)
    
    # Create user document
    user_data = UserDB(
        user_id=user_id,
        name=request.name,
        email=request.email,
        hashed_password=hashed_password,
        role=request.role,
        onboarding_completed=False,
        created_at=datetime.utcnow().isoformat()
    )
    
    # Save to MongoDB
    await user_repo.create_user(user_data)
    
    # Log signup event in history
    history_data = HistoryDB(
        history_id=f"hist_{uuid.uuid4().hex[:12]}",
        user_id=user_id,
        event_type="other",
        description=f"User signed up with role: {request.role}",
        context={
            "action": "signup",
            "role": request.role,
            "name": request.name
        },
        timestamp=datetime.utcnow().isoformat()
    )
    await history_repo.log_event(history_data)
    
    # Create JWT token
    token_data = {
        "sub": user_id,
        "email": request.email,
        "role": request.role,
        "onboarding_completed": False
    }
    access_token = create_access_token(token_data)
    
    # Prepare response (WITHOUT password)
    user_response = UserResponse(
        id=user_id,
        name=request.name,
        email=request.email,
        role=request.role,
        onboarding_completed=False,
        created_at=user_data.created_at
    )
    
    print(f"✅ New user created: {request.email} ({request.role}) - ID: {user_id}")
    
    return AuthResponse(
        access_token=access_token,
        user=user_response
    )

# ==========================================
# LOGIN ENDPOINT
# ==========================================

@router.post("/login", response_model=AuthResponse)
async def login(
    request: LoginRequest,
    user_repo: UserRepository = Depends(get_user_repo),
    history_repo: HistoryRepository = Depends(get_history_repo)
):
    """
    Authenticate existing user
    
    CRUD Permission: User reads their own identity
    
    Process:
    1. Find user by email in MongoDB
    2. Verify password
    3. Log login event
    4. Generate new JWT token
    5. Return token + user data
    """
    # Find user by email
    user = await user_repo.get_user_by_email(request.email)
    
    # User not found
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    # Verify password
    if not verify_password(request.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    # Log login event
    history_data = HistoryDB(
        history_id=f"hist_{uuid.uuid4().hex[:12]}",
        user_id=user["user_id"],
        event_type="login",
        description="User logged in",
        context={"action": "login"},
        timestamp=datetime.utcnow().isoformat()
    )
    await history_repo.log_event(history_data)
    
    # Create JWT token
    token_data = {
        "sub": user["user_id"],
        "email": user["email"],
        "role": user["role"],
        "onboarding_completed": user.get("onboarding_completed", False)
    }
    access_token = create_access_token(token_data)
    
    # Prepare response (WITHOUT password)
    user_response = UserResponse(
        id=user["user_id"],
        name=user["name"],
        email=user["email"],
        role=user["role"],
        onboarding_completed=user.get("onboarding_completed", False),
        created_at=user["created_at"]
    )
    
    print(f"✅ User logged in: {request.email} - ID: {user['user_id']}")
    
    return AuthResponse(
        access_token=access_token,
        user=user_response
    )

# ==========================================
# GET CURRENT USER (ME) ENDPOINT
# ==========================================

@router.get("/me", response_model=UserResponse)
async def get_me(
    current_user: dict = Depends(get_current_user),
    user_repo: UserRepository = Depends(get_user_repo)
):
    """
    Get current authenticated user's data
    
    CRUD Permission: User reads their own data
    
    This endpoint:
    - Requires valid JWT token
    - Returns fresh user data from MongoDB
    - Used by frontend to verify session
    """
    user_id = current_user["user_id"]
    
    # Get fresh user data from MongoDB
    user = await user_repo.get_user_by_id(user_id)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return UserResponse(
        id=user["user_id"],
        name=user["name"],
        email=user["email"],
        role=user["role"],
        onboarding_completed=user.get("onboarding_completed", False),
        created_at=user["created_at"]
    )

# ==========================================
# VERIFY TOKEN ENDPOINT
# ==========================================

@router.get("/verify")
async def verify_token(current_user: dict = Depends(get_current_user)):
    """
    Verify if token is valid
    Returns basic token info without database lookup
    
    Used for quick token validation
    """
    return {
        "valid": True,
        "user_id": current_user["user_id"],
        "email": current_user["email"],
        "role": current_user["role"],
        "onboarding_completed": current_user["onboarding_completed"]
    }

# ==========================================
# LOGOUT ENDPOINT (Optional - Client-side only)
# ==========================================

@router.post("/logout")
async def logout(
    current_user: dict = Depends(get_current_user),
    history_repo: HistoryRepository = Depends(get_history_repo)
):
    """
    Logout endpoint
    
    Note: JWT tokens are stateless, so logout is client-side
    (client deletes token). This endpoint just logs the event.
    """
    # Log logout event
    history_data = HistoryDB(
        history_id=f"hist_{uuid.uuid4().hex[:12]}",
        user_id=current_user["user_id"],
        event_type="other",
        description="User logged out",
        context={"action": "logout"},
        timestamp=datetime.utcnow().isoformat()
    )
    await history_repo.log_event(history_data)
    
    print(f"✅ User logged out: {current_user['email']}")
    
    return {
        "message": "Logged out successfully",
        "note": "Token is still valid until expiry. Client should delete token."
    }