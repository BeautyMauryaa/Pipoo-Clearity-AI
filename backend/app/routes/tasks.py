"""
Task Management Routes
System creates tasks, Users mark status
"""

from fastapi import APIRouter, Depends, HTTPException, status
from app.models.database import TaskDB, HistoryDB
from app.core.dependencies import (
    get_current_user,
    get_task_repo,
    get_history_repo
)
from app.db.repositories import TaskRepository, HistoryRepository
from pydantic import BaseModel
from datetime import datetime
import uuid

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# ==========================================
# REQUEST MODELS
# ==========================================

class CompleteTaskRequest(BaseModel):
    task_id: str

class SkipTaskRequest(BaseModel):
    task_id: str
    reason: str | None = None

class CreateTaskRequest(BaseModel):
    """
    System-only request (not exposed to users)
    Used internally by workspace logic
    """
    title: str
    description: str | None = None
    task_type: str  # daily, skill, optional, micro
    difficulty: str | None = None
    estimated_time: str
    assigned_date: str
    due_date: str | None = None

# ==========================================
# GET USER'S TASKS
# ==========================================

@router.get("")
async def get_user_tasks(
    current_user: dict = Depends(get_current_user),
    task_repo: TaskRepository = Depends(get_task_repo),
    date: str | None = None,
    task_type: str | None = None
):
    """
    Get current user's tasks
    
    CRUD Permission: User reads their own tasks
    
    Query params:
    - date: Filter by assigned date (YYYY-MM-DD)
    - task_type: Filter by type (daily, skill, optional, micro)
    """
    user_id = current_user["user_id"]
    
    tasks = await task_repo.get_user_tasks(
        user_id=user_id,
        date=date,
        task_type=task_type
    )
    
    return {
        "user_id": user_id,
        "tasks": tasks,
        "total": len(tasks)
    }

# ==========================================
# COMPLETE TASK
# ==========================================

@router.post("/complete")
async def complete_task(
    request: CompleteTaskRequest,
    current_user: dict = Depends(get_current_user),
    task_repo: TaskRepository = Depends(get_task_repo),
    history_repo: HistoryRepository = Depends(get_history_repo)
):
    """
    Mark task as completed
    
    CRUD Permission: User updates status of their own tasks
    System automatically logs completion in history
    
    Process:
    1. Verify task belongs to user
    2. Mark as completed in tasks collection
    3. Auto-log event in history collection
    4. Return success
    """
    user_id = current_user["user_id"]
    
    # Get task to verify ownership
    task = await task_repo.get_task_by_id(request.task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    # Verify ownership
    if task["user_id"] != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only complete your own tasks"
        )
    
    # Check if already completed
    if task.get("completed"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task already completed"
        )
    
    # Mark as completed
    success = await task_repo.complete_task(request.task_id, user_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to complete task"
        )
    
    # AUTO-LOG in history (System responsibility)
    history_data = HistoryDB(
        history_id=f"hist_{uuid.uuid4().hex[:12]}",
        user_id=user_id,
        event_type="task_completed",
        description=f"Completed task: {task['title']}",
        context={
            "task_id": request.task_id,
            "task_title": task["title"],
            "task_type": task["task_type"],
            "assigned_date": task["assigned_date"]
        },
        timestamp=datetime.utcnow().isoformat()
    )
    await history_repo.log_event(history_data)
    
    print(f"✅ Task completed: {task['title']} by {current_user['email']}")
    
    return {
        "success": True,
        "message": "Task completed successfully",
        "task_id": request.task_id
    }

# ==========================================
# SKIP TASK
# ==========================================

@router.post("/skip")
async def skip_task(
    request: SkipTaskRequest,
    current_user: dict = Depends(get_current_user),
    task_repo: TaskRepository = Depends(get_task_repo),
    history_repo: HistoryRepository = Depends(get_history_repo)
):
    """
    Mark task as skipped
    
    CRUD Permission: User updates status of their own tasks
    System automatically logs skip in history
    
    Process:
    1. Verify task belongs to user
    2. Mark as skipped in tasks collection
    3. Auto-log event in history collection
    4. Return success
    """
    user_id = current_user["user_id"]
    
    # Get task to verify ownership
    task = await task_repo.get_task_by_id(request.task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    # Verify ownership
    if task["user_id"] != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only skip your own tasks"
        )
    
    # Check if already completed or skipped
    if task.get("completed"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot skip completed task"
        )
    
    if task.get("skipped"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task already skipped"
        )
    
    # Mark as skipped
    success = await task_repo.skip_task(request.task_id, user_id, request.reason)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to skip task"
        )
    
    # AUTO-LOG in history (System responsibility)
    history_data = HistoryDB(
        history_id=f"hist_{uuid.uuid4().hex[:12]}",
        user_id=user_id,
        event_type="task_skipped",
        description=f"Skipped task: {task['title']}",
        context={
            "task_id": request.task_id,
            "task_title": task["title"],
            "task_type": task["task_type"],
            "reason": request.reason,
            "assigned_date": task["assigned_date"]
        },
        timestamp=datetime.utcnow().isoformat()
    )
    await history_repo.log_event(history_data)
    
    print(f"⚠️ Task skipped: {task['title']} by {current_user['email']} (Reason: {request.reason})")
    
    return {
        "success": True,
        "message": "Task skipped successfully",
        "task_id": request.task_id,
        "reason": request.reason
    }

# ==========================================
# GET TASK STATS
# ==========================================

@router.get("/stats")
async def get_task_stats(
    current_user: dict = Depends(get_current_user),
    task_repo: TaskRepository = Depends(get_task_repo)
):
    """
    Get task completion statistics
    
    CRUD Permission: User reads their own stats
    """
    user_id = current_user["user_id"]
    
    stats = await task_repo.get_completion_stats(user_id)
    
    return {
        "user_id": user_id,
        "stats": stats
    }

# ==========================================
# CREATE TASK (SYSTEM ONLY - Internal use)
# ==========================================

@router.post("/system/create")
async def create_task_system(
    request: CreateTaskRequest,
    current_user: dict = Depends(get_current_user),
    task_repo: TaskRepository = Depends(get_task_repo)
):
    """
    Create task (System only)
    
    CRUD Permission: System creates tasks
    
    NOTE: In production, this endpoint should be:
    1. Protected with admin/system role check
    2. Or called internally by workspace service
    3. NOT exposed to regular users
    
    For now, users can create their own tasks for testing
    """
    user_id = current_user["user_id"]
    
    # Generate task_id
    task_id = f"task_{uuid.uuid4().hex[:12]}"
    
    # Create task document
    task_data = TaskDB(
        task_id=task_id,
        user_id=user_id,
        title=request.title,
        description=request.description,
        task_type=request.task_type,
        difficulty=request.difficulty,
        estimated_time=request.estimated_time,
        assigned_date=request.assigned_date,
        due_date=request.due_date,
        completed=False,
        skipped=False
    )
    
    await task_repo.create_task(task_data)
    
    print(f"📝 Task created: {request.title} for {current_user['email']}")
    
    return {
        "success": True,
        "message": "Task created successfully",
        "task_id": task_id,
        "task": task_data.model_dump()
    }