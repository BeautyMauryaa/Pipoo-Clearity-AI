"""
Application Configuration - UPDATED FOR PHASE 6 (FIXED)
"""
import os
import sys  # ← ADD THIS LINE

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Database
DB_PATH = os.path.join(DATA_DIR, 'app.db')

# API Configuration
GEMINI_API_KEY = "AIzaSyCJDOfwr_eHr4Chjs70IuePqH0TC5AtWIo"  # Replace with your actual Gemini API key
GEMINI_MODEL = "gemini-2.0-flash-exp"  # Gemini 2.5 Flash model
# App Settings
APP_NAME = "Pipoo"
APP_VERSION = "1.0.0"
DEBUG_MODE = True

# Platform Detection
PLATFORM = sys.platform
IS_ANDROID = False
IS_WINDOWS = PLATFORM.startswith('win')
IS_LINUX = PLATFORM.startswith('linux')

try:
    from jnius import autoclass
    IS_ANDROID = True
except:
    pass

# Session
SESSION_TIMEOUT = 3600

# Voice Settings
STT_LANGUAGE = "en-US"
STT_TIMEOUT = 5
STT_PHRASE_LIMIT = 15
TTS_RATE = 150
TTS_VOLUME = 0.9
TTS_VOICE_INDEX = 0
USE_GOOGLE_STT = True
USE_SPHINX_STT = False

# AI Settings
AI_MAX_HISTORY = 10
AI_TEMPERATURE = 0.7
AI_MAX_TOKENS = 1000
AI_TIMEOUT = 30

# Logging
LOG_LEVEL = "INFO"
LOG_FILE = os.path.join(DATA_DIR, 'app.log')
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5MB
LOG_BACKUP_COUNT = 3

# Performance Settings
ENABLE_PERFORMANCE_MONITORING = True
DATABASE_OPTIMIZE_INTERVAL = 86400  # 24 hours in seconds
CACHE_SIZE_LIMIT = 100  # Maximum cached items
AUTO_CLEANUP_OLD_LOGS = True
LOG_RETENTION_DAYS = 30

# Memory Management
MAX_CHAT_HISTORY_MEMORY = 100  # Maximum messages in memory
MAX_NOTES_LOAD = 50  # Maximum notes to load at once
MAX_REMINDERS_LOAD = 50  # Maximum reminders to load at once

# UI Performance
ENABLE_ANIMATIONS = True
TRANSITION_DURATION = 0.3
DEBOUNCE_DELAY = 0.5  # Seconds to wait before processing input

# Error Reporting
ENABLE_ERROR_REPORTING = True
ERROR_REPORT_FREQUENCY = 3600  # Report errors every hour

# Auto-Update (Future)
CHECK_UPDATES_ON_STARTUP = False
UPDATE_CHECK_URL = "https://api.pipoo.app/version"

# Feature Flags
ENABLE_VOICE = True
ENABLE_AI = True
ENABLE_NOTES = True
ENABLE_REMINDERS = True
ENABLE_DAILY_BRIEFING = True
ENABLE_COMMAND_PARSER = True

# Development
SIMULATE_SLOW_NETWORK = False  # For testing
SIMULATE_API_ERRORS = False    # For testing