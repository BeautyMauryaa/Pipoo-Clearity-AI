"""
Database Collections Setup
Defines collection schemas and creates indexes
"""

from motor.motor_asyncio import AsyncIOMotorDatabase
from app.core.database import Collections

# ==========================================
# COLLECTION SCHEMAS (MongoDB Validation)
# ==========================================

async def create_collections_with_validation(db: AsyncIOMotorDatabase):
    """
    Create collections with JSON schema validation
    This ensures data integrity at database level
    """
    
    # ==========================================
    # 1️⃣ USERS COLLECTION
    # ==========================================
    
    users_schema = {
        "bsonType": "object",
        "required": ["user_id", "name", "email", "hashed_password", "role", "created_at"],
        "properties": {
            "user_id": {"bsonType": "string"},
            "name": {"bsonType": "string"},
            "email": {"bsonType": "string"},
            "hashed_password": {"bsonType": "string"},
            "role": {"enum": ["student", "professional", "company"]},
            "onboarding_completed": {"bsonType": "bool"},
            "created_at": {"bsonType": "string"},
            "updated_at": {"bsonType": "string"}
        }
    }
    
    try:
        await db.create_collection(
            Collections.USERS,
            validator={"$jsonSchema": users_schema}
        )
        print(f"✅ Created collection: {Collections.USERS}")
    except Exception:
        print(f"ℹ️  Collection {Collections.USERS} already exists")
    
    # Create indexes for users
    await db[Collections.USERS].create_index("user_id", unique=True)
    await db[Collections.USERS].create_index("email", unique=True)
    print(f"   📇 Indexes: user_id (unique), email (unique)")
    
    # ==========================================
    # 2️⃣ ONBOARDING_PROFILES COLLECTION
    # ==========================================
    
    onboarding_schema = {
        "bsonType": "object",
        "required": ["user_id", "role", "data", "completed_at"],
        "properties": {
            "user_id": {"bsonType": "string"},
            "role": {"enum": ["student", "professional", "company"]},
            "data": {"bsonType": "object"},
            "completed_at": {"bsonType": "string"}
        }
    }
    
    try:
        await db.create_collection(
            Collections.ONBOARDING_PROFILES,
            validator={"$jsonSchema": onboarding_schema}
        )
        print(f"✅ Created collection: {Collections.ONBOARDING_PROFILES}")
    except Exception:
        print(f"ℹ️  Collection {Collections.ONBOARDING_PROFILES} already exists")
    
    # Create indexes for onboarding_profiles
    await db[Collections.ONBOARDING_PROFILES].create_index("user_id", unique=True)
    print(f"   📇 Indexes: user_id (unique)")
    
    # ==========================================
    # 3️⃣ TASKS COLLECTION
    # ==========================================
    
    tasks_schema = {
        "bsonType": "object",
        "required": ["task_id", "user_id", "title", "task_type", "assigned_date"],
        "properties": {
            "task_id": {"bsonType": "string"},
            "user_id": {"bsonType": "string"},
            "title": {"bsonType": "string"},
            "description": {"bsonType": "string"},
            "task_type": {"enum": ["daily", "skill", "optional", "micro"]},
            "difficulty": {"enum": ["easy", "medium", "hard"]},
            "estimated_time": {"bsonType": "string"},
            "assigned_date": {"bsonType": "string"},
            "due_date": {"bsonType": "string"},
            "completed": {"bsonType": "bool"},
            "completed_at": {"bsonType": "string"},
            "skipped": {"bsonType": "bool"},
            "skipped_reason": {"bsonType": "string"}
        }
    }
    
    try:
        await db.create_collection(
            Collections.TASKS,
            validator={"$jsonSchema": tasks_schema}
        )
        print(f"✅ Created collection: {Collections.TASKS}")
    except Exception:
        print(f"ℹ️  Collection {Collections.TASKS} already exists")
    
    # Create indexes for tasks
    await db[Collections.TASKS].create_index("task_id", unique=True)
    await db[Collections.TASKS].create_index("user_id")
    await db[Collections.TASKS].create_index([("user_id", 1), ("assigned_date", -1)])
    await db[Collections.TASKS].create_index([("user_id", 1), ("completed", 1)])
    print(f"   📇 Indexes: task_id (unique), user_id, user_id+date, user_id+status")
    
    # ==========================================
    # 4️⃣ HISTORY COLLECTION (NEW - Pipoo Insights)
    # ==========================================
    
    history_schema = {
        "bsonType": "object",
        "required": ["history_id", "user_id", "event_type", "description", "timestamp"],
        "properties": {
            "history_id": {"bsonType": "string"},
            "user_id": {"bsonType": "string"},
            "event_type": {
                "enum": [
                    "task_completed",
                    "task_skipped",
                    "skill_proof_completed",
                    "evaluation_flagged",
                    "onboarding_completed",
                    "login",
                    "pipoo_insight",  # NEW - for Pipoo messages
                    "other"
                ]
            },
            "description": {"bsonType": "string"},
            "context": {"bsonType": "object"},
            "timestamp": {"bsonType": "string"}
        }
    }
    
    try:
        await db.create_collection(
            Collections.HISTORY,
            validator={"$jsonSchema": history_schema}
        )
        print(f"✅ Created collection: {Collections.HISTORY}")
    except Exception:
        print(f"ℹ️  Collection {Collections.HISTORY} already exists")
    
    # Create indexes for history
    await db[Collections.HISTORY].create_index("history_id", unique=True)
    await db[Collections.HISTORY].create_index("user_id")
    await db[Collections.HISTORY].create_index([("user_id", 1), ("timestamp", -1)])
    await db[Collections.HISTORY].create_index([("user_id", 1), ("event_type", 1)])
    print(f"   📇 Indexes: history_id (unique), user_id, user_id+timestamp, user_id+type")
    
    # ==========================================
    # 5️⃣ SKILL_PROOFS COLLECTION
    # ==========================================
    
    skill_proof_schema = {
        "bsonType": "object",
        "required": ["proof_id", "candidate_id", "company_id", "task_name", "submitted_at"],
        "properties": {
            "proof_id": {"bsonType": "string"},
            "candidate_id": {"bsonType": "string"},
            "company_id": {"bsonType": "string"},
            "task_name": {"bsonType": "string"},
            "task_type": {"bsonType": "string"},
            "score": {"bsonType": "int"},
            "flags": {"bsonType": "array"},
            "submitted_at": {"bsonType": "string"},
            "evaluated_at": {"bsonType": "string"},
            "evaluation_data": {"bsonType": "object"}
        }
    }
    
    try:
        await db.create_collection(
            Collections.SKILL_PROOFS,
            validator={"$jsonSchema": skill_proof_schema}
        )
        print(f"✅ Created collection: {Collections.SKILL_PROOFS}")
    except Exception:
        print(f"ℹ️  Collection {Collections.SKILL_PROOFS} already exists")
    
    # Create indexes for skill_proofs
    await db[Collections.SKILL_PROOFS].create_index("proof_id", unique=True)
    await db[Collections.SKILL_PROOFS].create_index("candidate_id")
    await db[Collections.SKILL_PROOFS].create_index("company_id")
    await db[Collections.SKILL_PROOFS].create_index([("company_id", 1), ("evaluated_at", -1)])
    print(f"   📇 Indexes: proof_id (unique), candidate_id, company_id, company_id+date")

# ==========================================
# COLLECTION INFO (For Debugging)
# ==========================================

async def list_collections(db: AsyncIOMotorDatabase):
    """
    List all collections and their document counts
    Useful for debugging
    """
    print("\n" + "=" * 50)
    print("📊 DATABASE STATUS")
    print("=" * 50)
    
    collections = await db.list_collection_names()
    
    for collection_name in collections:
        count = await db[collection_name].count_documents({})
        print(f"📁 {collection_name}: {count} documents")
    
    print("=" * 50 + "\n")

# ==========================================
# DROP ALL COLLECTIONS (DANGEROUS - Dev only)
# ==========================================

async def drop_all_collections(db: AsyncIOMotorDatabase):
    """
    ⚠️ DANGER: Drop all collections
    Use only in development for clean restart
    """
    collections = [
        Collections.USERS,
        Collections.ONBOARDING_PROFILES,
        Collections.TASKS,
        Collections.HISTORY,
        Collections.SKILL_PROOFS
    ]
    
    for collection in collections:
        await db[collection].drop()
        print(f"🗑️  Dropped collection: {collection}")