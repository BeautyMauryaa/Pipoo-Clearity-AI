"""
Navigation Manager - Handles screen transitions
"""
from kivy.uix.screenmanager import ScreenManager, SlideTransition


class NavigationManager(ScreenManager):
    """
    Custom Screen Manager with navigation methods
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = SlideTransition(direction='left', duration=0.3)
    
    def goto_screen(self, screen_name, direction='left'):
        """
        Navigate to a specific screen
        
        Args:
            screen_name (str): Name of the screen to navigate to
            direction (str): Transition direction ('left', 'right', 'up', 'down')
        """
        self.transition.direction = direction
        self.current = screen_name
    
    def go_back(self):
        """Navigate back with right transition"""
        self.transition.direction = 'right'
        # Logic to track previous screen will be added in Phase 3
        pass
    
    def clear_and_goto(self, screen_name):
        """
        Clear navigation history and go to screen
        Used for logout or major state changes
        """
        self.transition.direction = 'left'
        self.current = screen_name