"""
User Data Model
"""
from datetime import datetime


class User:
    """User model"""
    
    def __init__(self, id=None, username=None, password_hash=None, created_at=None):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.created_at = created_at or datetime.now()
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'username': self.username,
            'password_hash': self.password_hash,
            'created_at': self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at
        }
    
    @staticmethod
    def from_dict(data):
        """Create User from dictionary"""
        return User(
            id=data.get('id'),
            username=data.get('username'),
            password_hash=data.get('password_hash'),
            created_at=data.get('created_at')
        )
    
    def __repr__(self):
        return f"<User {self.username}>"