
"""
Settings Screen - UPDATED FOR PHASE 4
"""
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from config.settings import DEBUG_MODE


class SettingsScreen(Screen):
    """
    App settings and preferences
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'settings'
    
    def on_enter(self):
        """Called when screen is displayed"""
        if DEBUG_MODE:
            print("📱 Settings Screen Loaded")
        
        # Display current username
        app = self.manager.app
        if app.current_user:
            self.ids.username_display.text = f"Logged in as: {app.current_user.username}"
    
    def logout(self):
        """Logout user"""
        if DEBUG_MODE:
            print("🚪 Logging out")
        
        # Clear auth state
        app = self.manager.app
        app.clear_auth_state()
        
        toast("Logged out successfully")
        self.manager.goto_screen('login')
    
    def go_back(self):
        """Navigate back to dashboard"""
        self.manager.goto_screen('dashboard', direction='right')
