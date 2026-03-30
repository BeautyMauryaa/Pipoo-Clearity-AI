"""
Development utilities
⚠️ Remove this file before production deployment
"""

from fastapi import APIRouter, Depends
from app.core.database import get_database
from app.db.collections import list_collections, drop_all_collections
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter()

@router.get("/dev/collections")
async def get_collections_info(db: AsyncIOMotorDatabase = Depends(get_database)):
    """
    List all collections and their document counts
    """
    await list_collections(db)
    return {"message": "Check console for collection info"}

@router.delete("/dev/reset")
async def reset_database(db: AsyncIOMotorDatabase = Depends(get_database)):
    """
    ⚠️ DANGER: Delete all collections and data
    Use only in development
    """
    await drop_all_collections(db)
    
    # Recreate collections
    from app.db.collections import create_collections_with_validation
    await create_collections_with_validation(db)
    
    return {"message": "Database reset complete"}