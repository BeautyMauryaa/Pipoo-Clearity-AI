from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from config.settings import DEBUG_MODE


class LoginScreen(Screen):
    """
    User login screen
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'login'
    
    def on_enter(self):
        """Called when screen is displayed"""
        if DEBUG_MODE:
            print("📱 Login Screen Loaded")
    
    def validate_and_login(self):
        """Validate inputs and attempt login"""
        username = self.ids.username_field.text.strip()
        password = self.ids.password_field.text
        
        if not username:
            toast("Please enter username")
            return
        
        if not password:
            toast("Please enter password")
            return
        
        # Get app and auth service
        app = self.manager.app
        
        # Attempt login
        success, result = app.auth_service.login(username, password)
        
        if success:
            # Update app state
            app.update_auth_state(result)
            
            toast(f"Welcome back, {result.username}!")
            
            # Clear password field
            self.ids.password_field.text = ""
            
            # Navigate to dashboard
            self.manager.goto_screen('dashboard')
        else:
            toast(result)  # Show error message
            self.ids.password_field.text = ""
    
    def goto_signup(self):
        """Navigate to signup screen"""
        self.manager.goto_screen('signup', direction='left')


class SignupScreen(Screen):
    """
    User registration screen
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'signup'
    
    def on_enter(self):
        """Called when screen is displayed"""
        if DEBUG_MODE:
            print("📱 Signup Screen Loaded")
    
    def validate_and_signup(self):
        """Validate inputs and create account"""
        username = self.ids.username_field.text.strip()
        password = self.ids.password_field.text
        confirm_password = self.ids.confirm_password_field.text
        
        if not username:
            toast("Please enter username")
            return
        
        if not password:
            toast("Please enter password")
            return
        
        if password != confirm_password:
            toast("Passwords do not match")
            return
        
        # Get app and auth service
        app = self.manager.app
        
        # Attempt registration
        success, result = app.auth_service.register(username, password)
        
        if success:
            toast("Account created successfully!")
            
            # Clear fields
            self.ids.username_field.text = ""
            self.ids.password_field.text = ""
            self.ids.confirm_password_field.text = ""
            
            # Navigate to login
            self.manager.goto_screen('login', direction='right')
        else:
            toast(result)  # Show error message
    
    def goto_login(self):
        """Navigate back to login screen"""
        self.manager.goto_screen('login', direction='right')