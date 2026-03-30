"""
History Routes
Provides audit trail view by querying history and tasks collections
"""

from fastapi import APIRouter, Depends, Query
from app.core.dependencies import (
    get_current_user,
    get_history_repo,
    get_task_repo
)
from app.db.repositories import HistoryRepository, TaskRepository
from typing import Optional

router = APIRouter(prefix="/history", tags=["History"])

# ==========================================
# GET USER HISTORY
# ==========================================

@router.get("")
async def get_user_history(
    current_user: dict = Depends(get_current_user),
    history_repo: HistoryRepository = Depends(get_history_repo),
    limit: int = Query(50, description="Number of events to return"),
    event_type: Optional[str] = Query(None, description="Filter by event type")
):
    """
    Get user's activity history (audit trail)
    
    CRUD Permission: User reads their own history
    
    History is built from:
    - history collection (logged events)
    
    Query params:
    - limit: Max events to return (default: 50)
    - event_type: Filter by type (task_completed, task_skipped, login, etc.)
    """
    user_id = current_user["user_id"]
    
    if event_type:
        # Get filtered events
        events = await history_repo.get_recent_events(
            user_id=user_id,
            event_type=event_type,
            days=30  # Last 30 days
        )
    else:
        # Get all recent events
        events = await history_repo.get_user_history(
            user_id=user_id,
            limit=limit
        )
    
    return {
        "user_id": user_id,
        "events": events,
        "total": len(events),
        "filter": event_type
    }

# ==========================================
# GET TASK HISTORY (Completed/Skipped Tasks)
# ==========================================

@router.get("/tasks")
async def get_task_history(
    current_user: dict = Depends(get_current_user),
    task_repo: TaskRepository = Depends(get_task_repo),
    limit: int = Query(50, description="Number of tasks to return")
):
    """
    Get user's task execution history
    
    CRUD Permission: User reads their own task history
    
    Returns completed and skipped tasks
    """
    user_id = current_user["user_id"]
    
    # Get all tasks
    all_tasks = await task_repo.get_user_tasks(user_id=user_id)
    
    # Filter completed or skipped
    history_tasks = [
        task for task in all_tasks
        if task.get("completed") or task.get("skipped")
    ]
    
    # Sort by completion date (most recent first)
    history_tasks.sort(
        key=lambda t: t.get("completed_at") or t.get("assigned_date"),
        reverse=True
    )
    
    return {
        "user_id": user_id,
        "tasks": history_tasks[:limit],
        "total": len(history_tasks)
    }

# ==========================================
# GET ACTIVITY SUMMARY
# ==========================================

@router.get("/summary")
async def get_activity_summary(
    current_user: dict = Depends(get_current_user),
    history_repo: HistoryRepository = Depends(get_history_repo),
    task_repo: TaskRepository = Depends(get_task_repo)
):
    """
    Get activity summary
    
    CRUD Permission: User reads their own activity summary
    
    Combines data from history and tasks collections
    """
    user_id = current_user["user_id"]
    
    # Get task stats
    task_stats = await task_repo.get_completion_stats(user_id)
    
    # Get event counts by type
    all_events = await history_repo.get_user_history(user_id, limit=1000)
    
    event_counts = {}
    for event in all_events:
        event_type = event.get("event_type", "other")
        event_counts[event_type] = event_counts.get(event_type, 0) + 1
    
    return {
        "user_id": user_id,
        "task_stats": task_stats,
        "event_counts": event_counts,
        "total_events": len(all_events)
    }