"""
Reminder Data Model
"""
from datetime import datetime


class Reminder:
    """Reminder model"""
    
    def __init__(self, id=None, user_id=None, title=None, time=None,
                 recurring='none', status='active', created_at=None):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.time = time
        self.recurring = recurring  # 'none', 'daily', 'weekly'
        self.status = status  # 'active', 'completed', 'cancelled'
        self.created_at = created_at or datetime.now()
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'time': self.time.isoformat() if isinstance(self.time, datetime) else self.time,
            'recurring': self.recurring,
            'status': self.status,
            'created_at': self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at
        }
    
    @staticmethod
    def from_dict(data):
        """Create Reminder from dictionary"""
        return Reminder(
            id=data.get('id'),
            user_id=data.get('user_id'),
            title=data.get('title'),
            time=data.get('time'),
            recurring=data.get('recurring', 'none'),
            status=data.get('status', 'active'),
            created_at=data.get('created_at')
        )
    
    def __repr__(self):
        return f"<Reminder {self.title}>"