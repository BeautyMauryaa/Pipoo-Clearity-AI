"""
Android Permissions Helper
Instructions for handling permissions in Android build
"""

# This file is for reference only
# Permissions are handled in buildozer.spec and utils/permissions.py

REQUIRED_PERMISSIONS = [
    'INTERNET',                  # For AI API calls
    'ACCESS_NETWORK_STATE',      # Check network connectivity
    'RECORD_AUDIO',              # Voice input (STT)
    'WRITE_EXTERNAL_STORAGE',    # Save data
    'READ_EXTERNAL_STORAGE',     # Read data
    'VIBRATE',                   # Notifications
    'WAKE_LOCK',                 # Keep screen on when needed
]

PERMISSION_EXPLANATIONS = {
    'INTERNET': 'Required for AI chat and web features',
    'ACCESS_NETWORK_STATE': 'Check if internet is available',
    'RECORD_AUDIO': 'Voice input and commands',
    'WRITE_EXTERNAL_STORAGE': 'Save your notes and reminders',
    'READ_EXTERNAL_STORAGE': 'Access your saved data',
    'VIBRATE': 'Reminder notifications',
    'WAKE_LOCK': 'Prevent sleep during voice input',
}

# Runtime permissions (Android 6.0+)
RUNTIME_PERMISSIONS = [
    'RECORD_AUDIO',
    'WRITE_EXTERNAL_STORAGE',
    'READ_EXTERNAL_STORAGE',
]

"""
USAGE INSTRUCTIONS:

1. Permissions are already configured in buildozer.spec
2. Runtime permissions are handled in utils/permissions.py
3. When building APK, all permissions will be included
4. Users will be prompted for runtime permissions when needed

NO ADDITIONAL SETUP REQUIRED - This file is for reference only.
"""