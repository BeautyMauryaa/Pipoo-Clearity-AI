# app/core/database.py
"""
Database Connection Module
Handles MongoDB connection and provides database instance
"""

from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings
from typing import Optional

# ==========================================
# DATABASE CLIENT (Singleton)
# ==========================================

class Database:
    client: Optional[AsyncIOMotorClient] = None
    db = None

database = Database()

# ==========================================
# CONNECT TO DATABASE
# ==========================================

async def connect_to_mongodb():
    """
    Connect to MongoDB
    Called on application startup
    """
    try:
        database.client = AsyncIOMotorClient(settings.MONGODB_URL)
        database.db = database.client[settings.DATABASE_NAME]
        
        # Test connection
        await database.client.admin.command('ping')
        
        print(f"✅ Connected to MongoDB: {settings.DATABASE_NAME}")
        
        # ⭐ NEW - Create collections with validation
        from app.db.collections import create_collections_with_validation
        await create_collections_with_validation(database.db)
        
        print(f"✅ Collections initialized")
        
    except Exception as e:
        print(f"❌ Failed to connect to MongoDB: {e}")
        print(f"   Make sure MongoDB is running at: {settings.MONGODB_URL}")
        database.client = None
        database.db = None

# ==========================================
# DISCONNECT FROM DATABASE
# ==========================================

async def close_mongodb_connection():
    """
    Close MongoDB connection
    Called on application shutdown
    """
    if database.client:
        database.client.close()
        print("👋 Disconnected from MongoDB")

# ==========================================
# GET DATABASE INSTANCE
# ==========================================

def get_database():
    """
    Get database instance
    Use this in routes and services
    """
    if database.db is None:
        raise Exception("Database not connected. Please start MongoDB.")
    return database.db

# ==========================================
# COLLECTION NAMES (Constants)
# ==========================================

class Collections:
    """Database collection names"""
    USERS = "users"
    ONBOARDING_PROFILES = "onboarding_profiles"
    TASKS = "tasks"
    HISTORY = "history"
    SKILL_PROOFS = "skill_proofs"