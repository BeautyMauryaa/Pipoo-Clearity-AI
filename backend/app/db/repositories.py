"""
Repository Layer - Data Access with Ownership Control
Each repository enforces who can do what with the data
"""

from motor.motor_asyncio import AsyncIOMotorDatabase
from app.models.database import (
    UserDB, 
    OnboardingProfileDB, 
    TaskDB, 
    HistoryDB, 
    SkillProofDB
)
from app.core.database import Collections
from typing import Optional, List, Dict, Any
from datetime import datetime

# ==========================================
# BASE REPOSITORY (Common operations)
# ==========================================

class BaseRepository:
    """
    Base repository with common database operations
    """
    def __init__(self, db: AsyncIOMotorDatabase, collection_name: str):
        self.db = db
        self.collection = db[collection_name]
    
    async def find_one(self, query: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Find single document"""
        return await self.collection.find_one(query)
    
    async def find_many(
        self, 
        query: Dict[str, Any], 
        limit: int = 100,
        sort: Optional[List[tuple]] = None
    ) -> List[Dict[str, Any]]:
        """Find multiple documents"""
        cursor = self.collection.find(query)
        if sort:
            cursor = cursor.sort(sort)
        cursor = cursor.limit(limit)
        return await cursor.to_list(length=limit)
    
    async def insert_one(self, document: Dict[str, Any]) -> str:
        """Insert single document"""
        result = await self.collection.insert_one(document)
        return str(result.inserted_id)
    
    async def update_one(
        self, 
        query: Dict[str, Any], 
        update: Dict[str, Any]
    ) -> bool:
        """Update single document"""
        result = await self.collection.update_one(query, {"$set": update})
        return result.modified_count > 0
    
    async def delete_one(self, query: Dict[str, Any]) -> bool:
        """Delete single document"""
        result = await self.collection.delete_one(query)
        return result.deleted_count > 0

# ==========================================
# 1. USER REPOSITORY
# Owner: User
# ==========================================

class UserRepository(BaseRepository):
    """
    User data access
    
    Ownership: User owns their identity
    CRUD Rules:
    - Create: User (signup), System (admin)
    - Read: User (self), System
    - Update: User (self), System
    - Delete: User (self), System (admin)
    """
    
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(db, Collections.USERS)
    
    async def create_user(self, user_data: UserDB) -> str:
        """
        Create new user
        Called during signup
        """
        user_dict = user_data.model_dump()
        user_dict["created_at"] = datetime.utcnow().isoformat()
        return await self.insert_one(user_dict)
    
    async def get_user_by_id(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Get user by ID"""
        return await self.find_one({"user_id": user_id})
    
    async def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        """Get user by email (for login)"""
        return await self.find_one({"email": email})
    
    async def update_user(
        self, 
        user_id: str, 
        updates: Dict[str, Any]
    ) -> bool:
        """
        Update user data
        Only user can update their own data
        """
        updates["updated_at"] = datetime.utcnow().isoformat()
        return await self.update_one({"user_id": user_id}, updates)
    
    async def mark_onboarding_complete(self, user_id: str) -> bool:
        """Mark user's onboarding as complete"""
        return await self.update_user(user_id, {"onboarding_completed": True})

# ==========================================
# 2. ONBOARDING PROFILE REPOSITORY
# Owner: User
# ==========================================

class OnboardingRepository(BaseRepository):
    """
    Onboarding profile data access
    
    Ownership: User owns their onboarding context
    CRUD Rules:
    - Create: User (once)
    - Read: User (self), System
    - Update: User (rare, re-onboarding)
    - Delete: User (self)
    """
    
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(db, Collections.ONBOARDING_PROFILES)
    
    async def create_profile(self, profile_data: OnboardingProfileDB) -> str:
        """
        Create onboarding profile
        Called after user completes onboarding
        """
        profile_dict = profile_data.model_dump()
        profile_dict["completed_at"] = datetime.utcnow().isoformat()
        return await self.insert_one(profile_dict)
    
    async def get_profile(self, user_id: str) -> Optional[Dict[str, Any]]:
        """
        Get user's onboarding profile
        Returns None if not completed
        """
        return await self.find_one({"user_id": user_id})
    
    async def update_profile(
        self, 
        user_id: str, 
        new_data: Dict[str, Any]
    ) -> bool:
        """
        Update onboarding profile (rare)
        Used when user wants to re-onboard
        """
        return await self.update_one({"user_id": user_id}, {"data": new_data})

# ==========================================
# 3. TASK REPOSITORY
# Owner: User (but System creates)
# ==========================================

class TaskRepository(BaseRepository):
    """
    Task data access
    
    Ownership: User owns execution, System assigns tasks
    CRUD Rules:
    - Create: System (AI/Logic decides tasks)
    - Read: User (own tasks only)
    - Update: User (status: complete/skip), System
    - Delete: System (cleanup old tasks)
    """
    
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(db, Collections.TASKS)
    
    async def create_task(self, task_data: TaskDB) -> str:
        """
        Create task (System only)
        Called by workspace logic or AI
        """
        task_dict = task_data.model_dump()
        return await self.insert_one(task_dict)
    
    async def get_user_tasks(
        self, 
        user_id: str,
        date: Optional[str] = None,
        task_type: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get user's tasks
        Filters by date or type if provided
        """
        query = {"user_id": user_id}
        
        if date:
            query["assigned_date"] = date
        
        if task_type:
            query["task_type"] = task_type
        
        return await self.find_many(
            query, 
            sort=[("assigned_date", -1)]  # Newest first
        )
    
    async def get_task_by_id(self, task_id: str) -> Optional[Dict[str, Any]]:
        """Get specific task"""
        return await self.find_one({"task_id": task_id})
    
    async def complete_task(self, task_id: str, user_id: str) -> bool:
        """
        Mark task as completed
        Only owner can complete their task
        """
        return await self.update_one(
            {"task_id": task_id, "user_id": user_id},
            {
                "completed": True,
                "completed_at": datetime.utcnow().isoformat()
            }
        )
    
    async def skip_task(
        self, 
        task_id: str, 
        user_id: str, 
        reason: Optional[str] = None
    ) -> bool:
        """
        Mark task as skipped
        Only owner can skip their task
        """
        return await self.update_one(
            {"task_id": task_id, "user_id": user_id},
            {
                "skipped": True,
                "skipped_reason": reason
            }
        )
    
    async def get_completion_stats(self, user_id: str) -> Dict[str, int]:
        """
        Get task completion statistics
        Used for accountability tracking
        """
        all_tasks = await self.get_user_tasks(user_id)
        
        total = len(all_tasks)
        completed = len([t for t in all_tasks if t.get("completed")])
        skipped = len([t for t in all_tasks if t.get("skipped")])
        pending = total - completed - skipped
        
        return {
            "total": total,
            "completed": completed,
            "skipped": skipped,
            "pending": pending
        }

# ==========================================
# 4. HISTORY REPOSITORY
# Owner: System (audit trail)
# ==========================================

class HistoryRepository(BaseRepository):
    """
    History/Activity log data access
    
    Ownership: System owns audit trail
    CRUD Rules:
    - Create: System (automatic logging)
    - Read: User (own history), Company (candidate history)
    - Update: Never
    - Delete: Never (audit integrity)
    """
    
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(db, Collections.HISTORY)
    
    async def log_event(self, event_data: HistoryDB) -> str:
        """
        Log system event
        Called automatically by system
        """
        event_dict = event_data.model_dump()
        event_dict["timestamp"] = datetime.utcnow().isoformat()
        return await self.insert_one(event_dict)
    
    async def get_user_history(
        self, 
        user_id: str,
        limit: int = 50
    ) -> List[Dict[str, Any]]:
        """
        Get user's activity history
        Used in History view
        """
        return await self.find_many(
            {"user_id": user_id},
            limit=limit,
            sort=[("timestamp", -1)]  # Newest first
        )
    
    async def get_recent_events(
        self, 
        user_id: str,
        event_type: str,
        days: int = 7
    ) -> List[Dict[str, Any]]:
        """
        Get recent events of specific type
        Used for pattern analysis
        """
        # In production, add date filtering here
        return await self.find_many(
            {"user_id": user_id, "event_type": event_type},
            limit=100,
            sort=[("timestamp", -1)]
        )

# ==========================================
# 5. SKILL PROOF REPOSITORY
# Owner: Company + Candidate (shared)
# ==========================================

class SkillProofRepository(BaseRepository):
    """
    Skill proof data access
    
    Ownership: Shared between Company and Candidate
    CRUD Rules:
    - Create: System (when task submitted)
    - Read: Company (all candidates), Candidate (own proofs)
    - Update: System (evaluation results)
    - Delete: Never (legal/audit requirement)
    """
    
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(db, Collections.SKILL_PROOFS)
    
    async def create_proof(self, proof_data: SkillProofDB) -> str:
        """
        Create skill proof record
        Called when candidate submits task
        """
        proof_dict = proof_data.model_dump()
        return await self.insert_one(proof_dict)
    
    async def get_candidate_proofs(
        self, 
        candidate_id: str
    ) -> List[Dict[str, Any]]:
        """
        Get all proofs for a candidate
        Candidate can see their own proofs
        """
        return await self.find_many(
            {"candidate_id": candidate_id},
            sort=[("submitted_at", -1)]
        )
    
    async def get_company_candidates(
        self, 
        company_id: str
    ) -> List[Dict[str, Any]]:
        """
        Get all candidate proofs for a company
        Company can see all candidates they evaluated
        """
        return await self.find_many(
            {"company_id": company_id},
            sort=[("evaluated_at", -1)]
        )
    
    async def update_evaluation(
        self, 
        proof_id: str,
        score: int,
        flags: List[str],
        evaluation_data: Dict[str, Any]
    ) -> bool:
        """
        Update proof with evaluation results
        System only (AI evaluation)
        """
        return await self.update_one(
            {"proof_id": proof_id},
            {
                "score": score,
                "flags": flags,
                "evaluation_data": evaluation_data,
                "evaluated_at": datetime.utcnow().isoformat()
            }
        )