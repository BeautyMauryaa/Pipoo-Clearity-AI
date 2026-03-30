"""
Workspace Service - Business Logic Layer
Generates workspace data based on user context and database state
"""

from app.models.workspace import WorkspaceDataResponse
from app.models.database import TaskDB, HistoryDB
from app.db.repositories import (
    UserRepository,
    OnboardingRepository,
    TaskRepository,
    HistoryRepository
)
from datetime import datetime, timedelta
import uuid

# ==========================================
# WORKSPACE SERVICE CLASS
# ==========================================

class WorkspaceService:
    """
    Handles workspace data generation with database memory
    """
    
    def __init__(
        self,
        user_repo: UserRepository,
        onboarding_repo: OnboardingRepository,
        task_repo: TaskRepository,
        history_repo: HistoryRepository
    ):
        self.user_repo = user_repo
        self.onboarding_repo = onboarding_repo
        self.task_repo = task_repo
        self.history_repo = history_repo
    
    async def get_workspace_data(
        self,
        user_id: str,
        role: str,
        view: str,
        onboarding_data: dict
    ) -> dict:
        """
        Generate workspace data based on role and view
        Uses real database state instead of mock data
        """
        
        if role == "student":
            return await self._get_student_workspace(user_id, view, onboarding_data)
        elif role == "professional":
            return await self._get_professional_workspace(user_id, view, onboarding_data)
        elif role == "company":
            return await self._get_company_workspace(user_id, view, onboarding_data)
        else:
            raise ValueError(f"Unknown role: {role}")
    
    # ==========================================
    # STUDENT WORKSPACE
    # ==========================================
    
    async def _get_student_workspace(
        self,
        user_id: str,
        view: str,
        onboarding_data: dict
    ) -> dict:
        """
        Generate student workspace data
        """
        
        if view == "overview":
            return await self._student_overview(user_id, onboarding_data)
        elif view == "career":
            return await self._student_career(user_id, onboarding_data)
        elif view == "focus":
            return await self._student_focus(user_id, onboarding_data)
        elif view == "skill":
            return await self._student_skill(user_id, onboarding_data)
        elif view == "history":
            return await self._student_history(user_id)
        else:
            raise ValueError(f"Unknown view: {view}")
    
    async def _student_overview(self, user_id: str, onboarding_data: dict) -> dict:
        """
        Student Overview - Daily dashboard
        
        Logic:
        1. Read today's tasks from database
        2. If no tasks exist, create one based on onboarding
        3. Check recent completion pattern
        4. Generate Pipoo message based on state
        5. Log insight
        """
        
        # Get today's date
        today = datetime.utcnow().date().isoformat()
        
        # Read today's tasks
        today_tasks = await self.task_repo.get_user_tasks(
            user_id=user_id,
            date=today
        )
        
        # If no tasks for today, create one
        if not today_tasks:
            task = await self._create_daily_task(user_id, onboarding_data, today)
            today_tasks = [task]
        
        # Get completion stats
        stats = await self.task_repo.get_completion_stats(user_id)
        
        # Get recent history (last 7 days)
        recent_events = await self.history_repo.get_recent_events(
            user_id=user_id,
            event_type="task_completed",
            days=7
        )
        
        # Decide Pipoo message based on state
        pipoo_message = self._generate_student_overview_message(
            onboarding_data=onboarding_data,
            stats=stats,
            recent_completions=len(recent_events)
        )
        
        # Log this insight (Pipoo's message)
        await self._log_pipoo_insight(
            user_id=user_id,
            view="overview",
            message=pipoo_message,
            context={"stats": stats, "tasks_today": len(today_tasks)}
        )
        
        return {
            "role": "student",
            "view": "overview",
            "pipoo": {
                "message": pipoo_message
            },
            "data": {
                "tasks": [self._format_task(t) for t in today_tasks],
                "stats": stats,
                "streak": len(recent_events)
            }
        }
    
    async def _student_career(self, user_id: str, onboarding_data: dict) -> dict:
        """
        Student Career View - Career guidance
        
        Logic:
        1. Analyze onboarding goal and timeline
        2. Generate honest assessment
        3. Show skill gaps (logic-based, not AI yet)
        """
        
        goal = onboarding_data.get("goal", "job-ready")
        timeline = onboarding_data.get("timeline", "6-12m")
        skills = onboarding_data.get("skills", "")
        target_role = onboarding_data.get("target_role", "Developer")
        
        # Logic-based career message
        pipoo_message = f"You want to be {goal} in {timeline}. "
        
        if timeline == "0-3m":
            pipoo_message += "This is aggressive. Focus on one skill deeply rather than many shallowly."
        elif timeline == "3-6m":
            pipoo_message += "This is tight but doable if you're consistent. No distractions."
        else:
            pipoo_message += "You have time to build properly. Consistency matters more than speed."
        
        # Skill gap analysis (simple logic)
        skill_gaps = self._analyze_skill_gaps(skills, target_role)
        
        return {
            "role": "student",
            "view": "career",
            "pipoo": {
                "message": pipoo_message
            },
            "data": {
                "goal": goal,
                "timeline": timeline,
                "target_role": target_role,
                "skill_gaps": skill_gaps,
                "current_skills": skills.split(",") if skills else []
            }
        }
    
    async def _student_focus(self, user_id: str, onboarding_data: dict) -> dict:
        """
        Student Focus View - Accountability check
        
        Logic:
        1. Check missed days in last 7 days
        2. Detect blocker patterns
        3. Adjust scope if needed
        """
        
        # Get last 7 days of tasks
        all_tasks = await self.task_repo.get_user_tasks(user_id=user_id)
        recent_tasks = [
            t for t in all_tasks
            if self._is_recent(t.get("assigned_date"), days=7)
        ]
        
        completed = [t for t in recent_tasks if t.get("completed")]
        skipped = [t for t in recent_tasks if t.get("skipped")]
        pending = [t for t in recent_tasks if not t.get("completed") and not t.get("skipped")]
        
        blocker = onboarding_data.get("blocker", "unknown")
        
        # Generate focus message
        if len(skipped) > 3:
            pipoo_message = f"You've skipped {len(skipped)} tasks this week. "
            pipoo_message += "Let's reduce scope. Doing 1 thing well beats planning 5 and doing 0."
        elif len(completed) >= 5:
            pipoo_message = f"Strong week. {len(completed)} tasks completed. Keep this momentum."
        elif len(pending) > 5:
            pipoo_message = "You have many pending tasks. Let's be honest: pick 1 and finish it today."
        else:
            pipoo_message = "You're on track. Focus on today's task, nothing else."
        
        return {
            "role": "student",
            "view": "focus",
            "pipoo": {
                "message": pipoo_message
            },
            "data": {
                "completed": len(completed),
                "skipped": len(skipped),
                "pending": len(pending),
                "blocker": blocker,
                "warning": len(skipped) > 3
            }
        }
    
    async def _student_skill(self, user_id: str, onboarding_data: dict) -> dict:
        """
        Student Skill View - Skill proof tasks
        """
        
        # Get skill tasks
        skill_tasks = await self.task_repo.get_user_tasks(
            user_id=user_id,
            task_type="skill"
        )
        
        return {
            "role": "student",
            "view": "skill",
            "pipoo": {
                "message": "Skill proof tasks will appear here. Complete them to build credibility."
            },
            "data": {
                "tasks": [self._format_task(t) for t in skill_tasks],
                "available": len([t for t in skill_tasks if not t.get("completed")])
            }
        }
    
    async def _student_history(self, user_id: str) -> dict:
        """
        Student History View - Audit trail
        """
        
        # Get all history events
        events = await self.history_repo.get_user_history(user_id, limit=50)
        
        # Get task history
        all_tasks = await self.task_repo.get_user_tasks(user_id=user_id)
        completed_tasks = [t for t in all_tasks if t.get("completed")]
        
        return {
            "role": "student",
            "view": "history",
            "pipoo": {
                "message": f"You have {len(events)} events and {len(completed_tasks)} completed tasks in your history."
            },
            "data": {
                "events": events,
                "completed_tasks": [self._format_task(t) for t in completed_tasks]
            }
        }
    
    # ==========================================
    # PROFESSIONAL WORKSPACE (Similar structure)
    # ==========================================
    
    async def _get_professional_workspace(
        self,
        user_id: str,
        view: str,
        onboarding_data: dict
    ) -> dict:
        """
        Generate professional workspace data
        Similar to student but different messaging
        """
        
        if view == "overview":
            return await self._professional_overview(user_id, onboarding_data)
        elif view == "direction":
            return await self._professional_direction(user_id, onboarding_data)
        elif view == "focus":
            return await self._professional_focus(user_id, onboarding_data)
        elif view == "skill-edge":
            return await self._professional_skill_edge(user_id, onboarding_data)
        elif view == "history":
            return await self._professional_history(user_id)
        else:
            raise ValueError(f"Unknown view: {view}")
    
    async def _professional_overview(self, user_id: str, onboarding_data: dict) -> dict:
        """Professional overview - similar logic to student"""
        
        today = datetime.utcnow().date().isoformat()
        today_tasks = await self.task_repo.get_user_tasks(user_id=user_id, date=today)
        
        if not today_tasks:
            task = await self._create_daily_task(user_id, onboarding_data, today)
            today_tasks = [task]
        
        stats = await self.task_repo.get_completion_stats(user_id)
        
        direction = onboarding_data.get("direction", "upskill")
        
        pipoo_message = f"You're working on: {direction}. Today's focus is clear. Execute."
        
        return {
            "role": "professional",
            "view": "overview",
            "pipoo": {"message": pipoo_message},
            "data": {
                "tasks": [self._format_task(t) for t in today_tasks],
                "stats": stats
            }
        }
    
    async def _professional_direction(self, user_id: str, onboarding_data: dict) -> dict:
        """Professional direction view"""
        
        direction = onboarding_data.get("direction", "upskill")
        objective = onboarding_data.get("objective", "")
        
        return {
            "role": "professional",
            "view": "direction",
            "pipoo": {
                "message": f"Your direction: {direction}. Your objective: {objective}."
            },
            "data": {
                "direction": direction,
                "objective": objective
            }
        }
    
    async def _professional_focus(self, user_id: str, onboarding_data: dict) -> dict:
        """Professional focus view"""
        return await self._student_focus(user_id, onboarding_data)  # Same logic
    
    async def _professional_skill_edge(self, user_id: str, onboarding_data: dict) -> dict:
        """Professional skill edge view"""
        return await self._student_skill(user_id, onboarding_data)  # Same logic
    
    async def _professional_history(self, user_id: str) -> dict:
        """Professional history view"""
        return await self._student_history(user_id)  # Same logic
    
    # ==========================================
    # COMPANY WORKSPACE (Simplified for now)
    # ==========================================
    
    async def _get_company_workspace(
        self,
        user_id: str,
        view: str,
        onboarding_data: dict
    ) -> dict:
        """
        Generate company workspace data
        """
        
        return {
            "role": "company",
            "view": view,
            "pipoo": {
                "message": "Company workspace - candidate evaluation features coming in Phase 5."
            },
            "data": {
                "candidates": [],
                "evaluations": []
            }
        }
    
    # ==========================================
    # HELPER METHODS
    # ==========================================
    
    async def _create_daily_task(
        self,
        user_id: str,
        onboarding_data: dict,
        assigned_date: str
    ) -> dict:
        """
        Create a daily task based on onboarding context
        System responsibility
        """
        
        goal = onboarding_data.get("goal", "learning")
        skills = onboarding_data.get("skills", "")
        time_available = onboarding_data.get("time_available", "1-2h")
        
        # Simple logic to generate task
        if "Python" in skills:
            title = "Practice Python fundamentals"
            description = "Write 3 small programs to reinforce concepts"
        elif "JavaScript" in skills:
            title = "Build a small JS project"
            description = "Create an interactive web component"
        else:
            title = f"Work on {goal} goal"
            description = "Focus on core skill development"
        
        task_id = f"task_{uuid.uuid4().hex[:12]}"
        
        task_data = TaskDB(
            task_id=task_id,
            user_id=user_id,
            title=title,
            description=description,
            task_type="daily",
            difficulty="medium",
            estimated_time=time_available,
            assigned_date=assigned_date,
            completed=False,
            skipped=False
        )
        
        await self.task_repo.create_task(task_data)
        
        print(f"📝 Auto-created task: {title} for user {user_id}")
        
        return task_data.model_dump()
    
    def _generate_student_overview_message(
        self,
        onboarding_data: dict,
        stats: dict,
        recent_completions: int
    ) -> str:
        """
        Generate Pipoo's message for student overview
        Based on real state
        """
        
        goal = onboarding_data.get("goal", "job-ready")
        timeline = onboarding_data.get("timeline", "6-12m")
        blocker = onboarding_data.get("blocker", "consistency")
        
        message = f"You want to be {goal} in {timeline}. "
        
        if stats["completed"] == 0:
            message += "Let's start. Complete today's task."
        elif recent_completions >= 5:
            message += f"Strong momentum: {recent_completions} tasks completed recently. Keep going."
        elif stats["skipped"] > stats["completed"]:
            message += f"You've skipped more than completed. Your blocker is {blocker}. Let's fix that."
        else:
            message += "You're making progress. Stay consistent."
        
        return message
    
    def _analyze_skill_gaps(self, current_skills: str, target_role: str) -> list:
        """
        Simple skill gap analysis (logic-based, not AI)
        """
        
        skill_list = [s.strip() for s in current_skills.split(",")] if current_skills else []
        
        # Simple role-to-skills mapping
        role_requirements = {
            "Full Stack Developer": ["HTML", "CSS", "JavaScript", "React", "Node.js", "Database", "Git"],
            "Data Scientist": ["Python", "Statistics", "Machine Learning", "SQL", "Pandas"],
            "Backend Developer": ["Python", "Database", "API Design", "Git"],
        }
        
        required = role_requirements.get(target_role, [])
        gaps = [skill for skill in required if skill not in skill_list]
        
        return gaps
    
    async def _log_pipoo_insight(
        self,
        user_id: str,
        view: str,
        message: str,
        context: dict
    ):
        """
        Log Pipoo's insight to history
        System responsibility
        """
        
        history_data = HistoryDB(
            history_id=f"hist_{uuid.uuid4().hex[:12]}",
            user_id=user_id,
            event_type="pipoo_insight",
            description=f"Pipoo insight for {view} view",
            context={
                "view": view,
                "message": message,
                **context
            },
            timestamp=datetime.utcnow().isoformat()
        )
        
        await self.history_repo.log_event(history_data)
    
    def _format_task(self, task: dict) -> dict:
        """Format task for frontend"""
        return {
            "id": task.get("task_id"),
            "title": task.get("title"),
            "description": task.get("description"),
            "type": task.get("task_type"),
            "difficulty": task.get("difficulty"),
            "estimated_time": task.get("estimated_time"),
            "completed": task.get("completed", False),
            "skipped": task.get("skipped", False),
            "assigned_date": task.get("assigned_date"),
            "completed_at": task.get("completed_at")
        }
    
    def _is_recent(self, date_str: str, days: int = 7) -> bool:
        """Check if date is within last N days"""
        try:
            task_date = datetime.fromisoformat(date_str.split("T")[0])
            cutoff_date = datetime.utcnow() - timedelta(days=days)
            return task_date.date() >= cutoff_date.date()
        except:
            return False


# ==========================================
# LEGACY FUNCTION (for backward compatibility)
# ==========================================

def get_workspace_data(role: str, view: str, onboarding_data: dict, user_id: str) -> dict:
    """
    Legacy function - returns mock data
    Will be replaced by WorkspaceService in routes
    """
    return {
        "role": role,
        "view": view,
        "pipoo": {
            "message": "Legacy mock data - use WorkspaceService instead"
        },
        "data": {}
    }