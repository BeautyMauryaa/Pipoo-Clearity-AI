"""
Authentication Service - Local User Authentication
"""
import bcrypt
from services.storage_service import StorageService
from config.settings import DEBUG_MODE
from utils.validators import Validators


class AuthService:
    """
    Authentication service for user management
    """
    
    def __init__(self, storage_service):
        self.storage = storage_service
    
    def register(self, username, password):
        """
        Register new user
        Returns: (success, user_or_error_message)
        """
        # Validate username
        is_valid, error = Validators.validate_username(username)
        if not is_valid:
            return False, error
        
        # Validate password
        is_valid, error = Validators.validate_password(password)
        if not is_valid:
            return False, error
        
        # Check if username exists
        existing_user = self.storage.get_user_by_username(username)
        if existing_user:
            return False, "Username already exists"
        
        # Hash password
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        # Create user
        user = self.storage.create_user(username, password_hash)
        
        if user:
            if DEBUG_MODE:
                print(f"✅ User registered: {username}")
            return True, user
        else:
            return False, "Failed to create user"
    
    def login(self, username, password):
        """
        Login user
        Returns: (success, user_or_error_message)
        """
        # Validate inputs
        if not username or not password:
            return False, "Username and password are required"
        
        # Get user
        user = self.storage.get_user_by_username(username)
        
        if not user:
            return False, "Invalid username or password"
        
        # Verify password
        try:
            if bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
                if DEBUG_MODE:
                    print(f"✅ User logged in: {username}")
                return True, user
            else:
                return False, "Invalid username or password"
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Login error: {e}")
            return False, "Authentication error"
    
    def logout(self):
        """Logout user (handled by app state)"""
        if DEBUG_MODE:
            print("✅ User logged out")
        return True