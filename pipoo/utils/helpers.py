"""
Helper Utilities
"""
from datetime import datetime


class Helpers:
    """Helper methods"""
    
    @staticmethod
    def format_date(date_str):
        """
        Format date string to readable format
        """
        try:
            if isinstance(date_str, str):
                dt = datetime.fromisoformat(date_str)
            elif isinstance(date_str, datetime):
                dt = date_str
            else:
                return date_str
            
            return dt.strftime("%m/%d/%Y")
        except:
            return date_str
    
    @staticmethod
    def format_time(time_str):
        """
        Format time string to readable format
        """
        try:
            if isinstance(time_str, str):
                dt = datetime.fromisoformat(time_str)
            elif isinstance(time_str, datetime):
                dt = time_str
            else:
                return time_str
            
            return dt.strftime("%I:%M %p")
        except:
            return time_str
    
    @staticmethod
    def format_datetime(datetime_str):
        """
        Format datetime string to readable format
        """
        try:
            if isinstance(datetime_str, str):
                dt = datetime.fromisoformat(datetime_str)
            elif isinstance(datetime_str, datetime):
                dt = datetime_str
            else:
                return datetime_str
            
            return dt.strftime("%m/%d/%Y %I:%M %p")
        except:
            return datetime_str
    
    @staticmethod
    def truncate_text(text, max_length=50):
        """
        Truncate text to max length
        """
        if not text:
            return ""
        
        if len(text) <= max_length:
            return text
        
        return text[:max_length-3] + "..."
    
    @staticmethod
    def get_time_ago(timestamp):
        """
        Get time ago string (e.g., '5 minutes ago')
        """
        try:
            if isinstance(timestamp, str):
                dt = datetime.fromisoformat(timestamp)
            elif isinstance(timestamp, datetime):
                dt = timestamp
            else:
                return "Unknown"
            
            now = datetime.now()
            diff = now - dt
            
            seconds = diff.total_seconds()
            
            if seconds < 60:
                return "Just now"
            elif seconds < 3600:
                minutes = int(seconds / 60)
                return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
            elif seconds < 86400:
                hours = int(seconds / 3600)
                return f"{hours} hour{'s' if hours != 1 else ''} ago"
            else:
                days = int(seconds / 86400)
                return f"{days} day{'s' if days != 1 else ''} ago"
        except:
            return "Unknown"