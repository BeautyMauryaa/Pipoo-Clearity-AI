"""
Splash Screen - Initial loading screen
"""
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.animation import Animation
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from config.settings import DEBUG_MODE


class SplashScreen(Screen):
    """
    Splash screen with logo and loading animation
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'splash'
    
    def on_enter(self):
        """Called when screen is displayed"""
        if DEBUG_MODE:
            print("📱 Splash Screen Loaded")
        
        # Animate logo (will add logo widget in kv file)
        # Schedule navigation to login/dashboard after 3 seconds
        Clock.schedule_once(self.navigate_next, 3)
    
    def navigate_next(self, dt):
        """Navigate to next screen based on auth status"""
        app = self.manager.app if hasattr(self.manager, 'app') else None
        
        if app and app.is_authenticated:
            self.manager.goto_screen('dashboard')
        else:
            self.manager.goto_screen('login')