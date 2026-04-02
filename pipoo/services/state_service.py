"""
State Service - Global Application State Management
"""
from config.settings import DEBUG_MODE


class StateService:
    """
    Global state manager (Singleton pattern)
    """
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StateService, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        
        self._initialized = True
        
        # Authentication state
        self.current_user = None
        self.is_authenticated = False
        
        # App state
        self.current_notes = []
        self.current_reminders = []
        self.current_chat_history = []
        
        if DEBUG_MODE:
            print("✅ State service initialized")
    
    def set_user(self, user):
        """Set current user"""
        self.current_user = user
        self.is_authenticated = True if user else False
        
        if DEBUG_MODE and user:
            print(f"✅ Current user set: {user.username}")
    
    def clear_user(self):
        """Clear current user (logout)"""
        self.current_user = None
        self.is_authenticated = False
        self.current_notes = []
        self.current_reminders = []
        self.current_chat_history = []
        
        if DEBUG_MODE:
            print("✅ User state cleared")
    
    def update_notes(self, notes):
        """Update notes cache"""
        self.current_notes = notes
    
    def update_reminders(self, reminders):
        """Update reminders cache"""
        self.current_reminders = reminders
    
    def update_chat_history(self, messages):
        """Update chat history cache"""
        self.current_chat_history = messages
    
    def get_user_id(self):
        """Get current user ID"""
        return self.current_user.id if self.current_user else None