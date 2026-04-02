"""
Input Validation Utilities
"""
import re


class Validators:
    """Input validation methods"""
    
    @staticmethod
    def validate_username(username):
        """
        Validate username
        Returns: (is_valid, error_message)
        """
        if not username:
            return False, "Username is required"
        
        if len(username) < 3:
            return False, "Username must be at least 3 characters"
        
        if len(username) > 20:
            return False, "Username must be less than 20 characters"
        
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            return False, "Username can only contain letters, numbers, and underscores"
        
        return True, None
    
    @staticmethod
    def validate_password(password):
        """
        Validate password
        Returns: (is_valid, error_message)
        """
        if not password:
            return False, "Password is required"
        
        if len(password) < 6:
            return False, "Password must be at least 6 characters"
        
        if len(password) > 50:
            return False, "Password must be less than 50 characters"
        
        return True, None
    
    @staticmethod
    def validate_note_title(title):
        """
        Validate note title
        Returns: (is_valid, error_message)
        """
        if not title or not title.strip():
            return False, "Title is required"
        
        if len(title) > 100:
            return False, "Title must be less than 100 characters"
        
        return True, None
    
    @staticmethod
    def validate_note_content(content):
        """
        Validate note content
        Returns: (is_valid, error_message)
        """
        if not content or not content.strip():
            return False, "Content is required"
        
        if len(content) > 10000:
            return False, "Content must be less than 10000 characters"
        
        return True, None
    
    @staticmethod
    def validate_reminder_title(title):
        """
        Validate reminder title
        Returns: (is_valid, error_message)
        """
        if not title or not title.strip():
            return False, "Title is required"
        
        if len(title) > 100:
            return False, "Title must be less than 100 characters"
        
        return True, None