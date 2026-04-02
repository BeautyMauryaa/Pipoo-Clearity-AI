"""
Error Handler - Centralized error handling
"""
from utils.logger import logger
from kivymd.toast import toast
from config.settings import DEBUG_MODE
import traceback


class ErrorHandler:
    """
    Centralized error handling system
    """
    
    @staticmethod
    def handle_error(error, context="", show_user=True, critical=False):
        """
        Handle error with logging and user notification
        
        Args:
            error: Exception object
            context: Context description
            show_user: Whether to show toast to user
            critical: Whether error is critical
        """
        error_msg = str(error)
        full_context = f"{context}: {error_msg}" if context else error_msg
        
        # Log error
        if critical:
            logger.critical(full_context, exc_info=True)
        else:
            logger.error(full_context, exc_info=True)
        
        # Show to user
        if show_user:
            user_msg = ErrorHandler._get_user_friendly_message(error, context)
            toast(user_msg)
        
        # Print to console in debug mode
        if DEBUG_MODE:
            print(f"❌ ERROR: {full_context}")
            traceback.print_exc()
        
        return error_msg
    
    @staticmethod
    def _get_user_friendly_message(error, context):
        """Convert technical error to user-friendly message"""
        error_str = str(error).lower()
        
        # Network errors
        if 'connection' in error_str or 'network' in error_str:
            return "Network error. Please check your connection."
        
        # API errors
        if 'api' in error_str or 'quota' in error_str:
            return "Service temporarily unavailable. Please try again."
        
        # Database errors
        if 'database' in error_str or 'sqlite' in error_str:
            return "Data error. Your information is safe."
        
        # Permission errors
        if 'permission' in error_str or 'denied' in error_str:
            return "Permission required. Please grant access."
        
        # File errors
        if 'file' in error_str or 'path' in error_str:
            return "File access error. Please check storage."
        
        # Generic error
        if context:
            return f"Error: {context}. Please try again."
        
        return "Something went wrong. Please try again."
    
    @staticmethod
    def handle_storage_error(error, operation=""):
        """Handle storage-specific errors"""
        logger.error(f"Storage error during {operation}: {error}")
        toast("Failed to save data. Please try again.")
    
    @staticmethod
    def handle_api_error(error, service=""):
        """Handle API-specific errors"""
        logger.error(f"API error for {service}: {error}")
        
        error_str = str(error).lower()
        if 'quota' in error_str or 'limit' in error_str:
            toast("API limit reached. Please try again later.")
        elif 'key' in error_str or 'auth' in error_str:
            toast("API authentication error. Check settings.")
        else:
            toast("Service error. Please try again.")
    
    @staticmethod
    def handle_voice_error(error):
        """Handle voice-specific errors"""
        logger.error(f"Voice error: {error}")
        
        error_str = str(error).lower()
        if 'microphone' in error_str or 'audio' in error_str:
            toast("Microphone error. Check permissions.")
        elif 'timeout' in error_str:
            toast("No speech detected. Please try again.")
        else:
            toast("Voice error. Please try again.")