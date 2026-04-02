"""
UI Screens Package
"""
from ui.screens.splash import SplashScreen
from ui.screens.auth import LoginScreen, SignupScreen
from ui.screens.dashboard import DashboardScreen
from ui.screens.chat import ChatScreen
from ui.screens.notes import NotesScreen
from ui.screens.reminders import RemindersScreen
from ui.screens.settings import SettingsScreen

__all__ = [
    'SplashScreen',
    'LoginScreen',
    'SignupScreen',
    'DashboardScreen',
    'ChatScreen',
    'NotesScreen',
    'RemindersScreen',
    'SettingsScreen',
]