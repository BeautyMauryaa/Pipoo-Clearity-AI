"""
Chat Message Data Model
"""
from datetime import datetime


class ChatMessage:
    """Chat message model"""
    
    def __init__(self, id=None, user_id=None, role=None, content=None, timestamp=None):
        self.id = id
        self.user_id = user_id
        self.role = role  # 'user' or 'ai'
        self.content = content
        self.timestamp = timestamp or datetime.now()
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'role': self.role,
            'content': self.content,
            'timestamp': self.timestamp.isoformat() if isinstance(self.timestamp, datetime) else self.timestamp
        }
    
    @staticmethod
    def from_dict(data):
        """Create ChatMessage from dictionary"""
        return ChatMessage(
            id=data.get('id'),
            user_id=data.get('user_id'),
            role=data.get('role'),
            content=data.get('content'),
            timestamp=data.get('timestamp')
        )
    
    def __repr__(self):
        return f"<ChatMessage {self.role}: {self.content[:20]}...>"