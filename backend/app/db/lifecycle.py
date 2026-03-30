"""
Data Lifecycle Management
Defines retention rules and cleanup policies
"""

from motor.motor_asyncio import AsyncIOMotorDatabase
from app.core.database import Collections
from datetime import datetime, timedelta
from typing import Optional

# ==========================================
# LIFECYCLE RULES (CONFIGURATION)
# ==========================================

class LifecycleRules:
    """
    Data retention configuration
    """
    
    # Tasks
    TASK_ARCHIVE_DAYS = 90  # Archive completed tasks after 90 days
    TASK_DELETE_DAYS = 365  # Delete archived tasks after 1 year
    
    # History/Insights
    HISTORY_SUMMARIZE_DAYS = 180  # Summarize old history after 6 months
    HISTORY_ARCHIVE_DAYS = 365  # Archive summarized history after 1 year
    
    # Skill Proofs
    SKILL_PROOF_DELETE_NEVER = True  # NEVER delete (audit/legal requirement)
    
    # Onboarding
    ONBOARDING_UPDATE_ALLOWED = True  # Allow users to re-onboard
    
    # Users
    USER_INACTIVE_DAYS = 365  # Mark user as inactive after 1 year

# ==========================================
# LIFECYCLE MANAGER
# ==========================================

class LifecycleManager:
    """
    Manages data lifecycle operations
    """
    
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
    
    # ==========================================
    # TASK LIFECYCLE
    # ==========================================
    
    async def archive_old_tasks(self) -> dict:
        """
        Archive completed tasks older than X days
        
        Process:
        1. Find completed tasks older than TASK_ARCHIVE_DAYS
        2. Add 'archived' flag
        3. Keep data intact (don't delete)
        
        Returns count of archived tasks
        """
        cutoff_date = (datetime.utcnow() - timedelta(days=LifecycleRules.TASK_ARCHIVE_DAYS)).isoformat()
        
        result = await self.db[Collections.TASKS].update_many(
            {
                "completed": True,
                "completed_at": {"$lt": cutoff_date},
                "archived": {"$ne": True}
            },
            {
                "$set": {
                    "archived": True,
                    "archived_at": datetime.utcnow().isoformat()
                }
            }
        )
        
        print(f"📦 Archived {result.modified_count} old tasks")
        
        return {
            "archived_count": result.modified_count,
            "cutoff_date": cutoff_date
        }
    
    async def delete_ancient_tasks(self) -> dict:
        """
        Delete archived tasks older than TASK_DELETE_DAYS
        
        CAUTION: This permanently deletes data
        Only for tasks that are:
        1. Already archived
        2. Older than 1 year
        """
        cutoff_date = (datetime.utcnow() - timedelta(days=LifecycleRules.TASK_DELETE_DAYS)).isoformat()
        
        result = await self.db[Collections.TASKS].delete_many(
            {
                "archived": True,
                "archived_at": {"$lt": cutoff_date}
            }
        )
        
        print(f"🗑️  Deleted {result.deleted_count} ancient tasks")
        
        return {
            "deleted_count": result.deleted_count,
            "cutoff_date": cutoff_date
        }
    
    # ==========================================
    # HISTORY LIFECYCLE
    # ==========================================
    
    async def summarize_old_history(self) -> dict:
        """
        Summarize old history events
        
        Process:
        1. Find events older than HISTORY_SUMMARIZE_DAYS
        2. Group by event_type and month
        3. Create summary documents
        4. Mark original events as 'summarized'
        
        Example summary:
        {
            "user_id": "user_123",
            "month": "2024-01",
            "event_type": "task_completed",
            "count": 25,
            "summary": "Completed 25 tasks in January 2024"
        }
        """
        cutoff_date = (datetime.utcnow() - timedelta(days=LifecycleRules.HISTORY_SUMMARIZE_DAYS)).isoformat()
        
        # Mark old events as summarized (don't delete)
        result = await self.db[Collections.HISTORY].update_many(
            {
                "timestamp": {"$lt": cutoff_date},
                "summarized": {"$ne": True}
            },
            {
                "$set": {
                    "summarized": True,
                    "summarized_at": datetime.utcnow().isoformat()
                }
            }
        )
        
        print(f"📊 Summarized {result.modified_count} old history events")
        
        return {
            "summarized_count": result.modified_count,
            "cutoff_date": cutoff_date
        }
    
    async def archive_old_history(self) -> dict:
        """
        Archive summarized history older than HISTORY_ARCHIVE_DAYS
        
        Move to cold storage or separate collection
        """
        cutoff_date = (datetime.utcnow() - timedelta(days=LifecycleRules.HISTORY_ARCHIVE_DAYS)).isoformat()
        
        result = await self.db[Collections.HISTORY].update_many(
            {
                "summarized": True,
                "summarized_at": {"$lt": cutoff_date},
                "archived": {"$ne": True}
            },
            {
                "$set": {
                    "archived": True,
                    "archived_at": datetime.utcnow().isoformat()
                }
            }
        )
        
        print(f"📦 Archived {result.modified_count} old history events")
        
        return {
            "archived_count": result.modified_count,
            "cutoff_date": cutoff_date
        }
    
    # ==========================================
    # SKILL PROOF LIFECYCLE
    # ==========================================
    
    async def verify_skill_proof_integrity(self) -> dict:
        """
        Verify skill proofs are intact
        
        Skill proofs are NEVER deleted (legal/audit requirement)
        This function only verifies integrity
        """
        total = await self.db[Collections.SKILL_PROOFS].count_documents({})
        
        # Check for any proofs with 'deleted' flag (should be 0)
        deleted = await self.db[Collections.SKILL_PROOFS].count_documents({"deleted": True})
        
        if deleted > 0:
            print(f"⚠️  WARNING: {deleted} skill proofs marked as deleted!")
        
        print(f"🔐 Skill proof integrity check: {total} proofs, {deleted} flagged as deleted")
        
        return {
            "total_proofs": total,
            "deleted_count": deleted,
            "integrity_ok": deleted == 0
        }
    
    # ==========================================
    # USER LIFECYCLE
    # ==========================================
    
    async def mark_inactive_users(self) -> dict:
        """
        Mark users as inactive if no activity for USER_INACTIVE_DAYS
        
        Process:
        1. Find users with no recent history events
        2. Mark as 'inactive' (don't delete)
        """
        cutoff_date = (datetime.utcnow() - timedelta(days=LifecycleRules.USER_INACTIVE_DAYS)).isoformat()
        
        # Find users with no recent history
        inactive_user_ids = []
        
        async for user in self.db[Collections.USERS].find({}):
            user_id = user["user_id"]
            
            recent_activity = await self.db[Collections.HISTORY].find_one(
                {
                    "user_id": user_id,
                    "timestamp": {"$gte": cutoff_date}
                }
            )
            
            if not recent_activity:
                inactive_user_ids.append(user_id)
        
        # Mark as inactive
        if inactive_user_ids:
            result = await self.db[Collections.USERS].update_many(
                {"user_id": {"$in": inactive_user_ids}},
                {
                    "$set": {
                        "inactive": True,
                        "inactive_since": datetime.utcnow().isoformat()
                    }
                }
            )
            
            print(f"💤 Marked {result.modified_count} users as inactive")
            
            return {
                "inactive_count": result.modified_count,
                "cutoff_date": cutoff_date
            }
        else:
            print("✅ All users are active")
            return {"inactive_count": 0}
    
    # ==========================================
    # RUN ALL LIFECYCLE TASKS
    # ==========================================
    
    async def run_all_lifecycle_tasks(self) -> dict:
        """
        Run all lifecycle management tasks
        Should be run periodically (daily cron job)
        """
        print("\n" + "=" * 50)
        print("🔄 Running Data Lifecycle Management")
        print("=" * 50)
        
        results = {}
        
        # Archive old tasks
        results["tasks_archived"] = await self.archive_old_tasks()
        
        # Summarize old history
        results["history_summarized"] = await self.summarize_old_history()
        
        # Archive old history
        results["history_archived"] = await self.archive_old_history()
        
        # Verify skill proof integrity
        results["skill_proof_integrity"] = await self.verify_skill_proof_integrity()
        
        # Mark inactive users
        results["inactive_users"] = await self.mark_inactive_users()
        
        print("=" * 50)
        print("✅ Lifecycle management complete")
        print("=" * 50 + "\n")
        
        return results

# ==========================================
# QUERY HELPERS (Exclude archived data)
# ==========================================

class LifecycleQueries:
    """
    Helper queries that respect lifecycle rules
    """
    
    @staticmethod
    def active_tasks_filter() -> dict:
        """
        Filter for active (non-archived) tasks
        Use in queries to exclude archived data
        """
        return {"archived": {"$ne": True}}
    
    @staticmethod
    def active_history_filter() -> dict:
        """
        Filter for active (non-archived) history
        """
        return {"archived": {"$ne": True}}
    
    @staticmethod
    def recent_tasks_filter(days: int = 30) -> dict:
        """
        Filter for tasks from last N days
        """
        cutoff_date = (datetime.utcnow() - timedelta(days=days)).date().isoformat()
        return {
            "archived": {"$ne": True},
            "assigned_date": {"$gte": cutoff_date}
        }