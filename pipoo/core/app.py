"""
Main Application Class - UPDATED FOR PHASE 10 (Performance & Error Handling)
"""
from kivymd.app import MDApp
from kivy.lang import Builder
from core.navigation import NavigationManager
from config.theme import THEME_CONFIG, COLORS
from config.settings import DEBUG_MODE, ENABLE_PERFORMANCE_MONITORING, DB_PATH
import os

# Import all screens
from ui.screens import (
    SplashScreen,
    LoginScreen,
    SignupScreen,
    DashboardScreen,
    ChatScreen,
    NotesScreen,
    RemindersScreen,
    SettingsScreen
)

# Import services
from services import (
    StorageService,
    AuthService,
    StateService,
    AIService,
    VoiceService,
    ProductivityService
)

# Import utilities
from utils import (
    PermissionsHandler,
    logger,
    ErrorHandler,
    perf_monitor
)


class PipooApp(MDApp):
    """
    Main Pipoo Application
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Pipoo - AI Voice Desk"
        self.theme_cls.theme_style = THEME_CONFIG['theme_style']
        self.theme_cls.primary_palette = THEME_CONFIG['primary_palette']
        self.theme_cls.primary_hue = THEME_CONFIG['primary_hue']
        self.theme_cls.accent_palette = THEME_CONFIG['accent_palette']
        self.theme_cls.accent_hue = THEME_CONFIG['accent_hue']
        
        # Custom colors
        self.colors = COLORS
        
        # Navigation manager
        self.nav_manager = None
        
        # Initialize services
        self.storage_service = None
        self.auth_service = None
        self.state_service = None
        self.ai_service = None
        self.voice_service = None
        self.productivity_service = None
        
        # Utilities
        self.permissions = None
        self.error_handler = ErrorHandler()
        
        # Global state shortcuts
        self.current_user = None
        self.is_authenticated = False
        
        # Performance monitoring
        if ENABLE_PERFORMANCE_MONITORING:
            perf_monitor.start_timer('app_startup')
    
    def build(self):
        """
        Build the application UI
        """
        try:
            logger.info("=" * 50)
            logger.info("Pipoo Application Starting...")
            logger.info("=" * 50)
            
            # Initialize services
            self._init_services()
            
            # Request permissions (Android)
            self._request_permissions()
            
            # Load all KV files
            self._load_kv_files()
            
            # Create navigation manager
            self.nav_manager = NavigationManager()
            
            # Store app reference in navigation manager
            self.nav_manager.app = self
            
            # Add all screens
            self._add_screens()
            
            # Set initial screen
            self.nav_manager.current = 'splash'
            
            if ENABLE_PERFORMANCE_MONITORING:
                startup_time = perf_monitor.end_timer('app_startup')
                logger.info(f"App startup completed in {startup_time:.2f}s")
            
            return self.nav_manager
            
        except Exception as e:
            self.error_handler.handle_error(e, "App initialization", critical=True)
            raise
    
    def _init_services(self):
        """Initialize all services"""
        try:
            if ENABLE_PERFORMANCE_MONITORING:
                perf_monitor.start_timer('service_init')
            
            # Storage service
            self.storage_service = StorageService()
            logger.info("Storage service initialized")
            
            # Auth service
            self.auth_service = AuthService(self.storage_service)
            logger.info("Auth service initialized")
            
            # State service
            self.state_service = StateService()
            logger.info("State service initialized")
            
            # AI service
            self.ai_service = AIService()
            if self.ai_service.is_configured:
                logger.info("AI service initialized")
            else:
                logger.warning("AI service not configured - add Gemini API key")
            
            # Voice service
            self.voice_service = VoiceService()
            tts_ok, stt_ok = self.voice_service.is_available()
            logger.info(f"Voice service initialized (TTS: {tts_ok}, STT: {stt_ok})")
            
            # Productivity service
            self.productivity_service = ProductivityService(
                self.storage_service,
                self.ai_service
            )
            logger.info("Productivity service initialized")
            
            # Permissions handler
            self.permissions = PermissionsHandler()
            logger.info("Permissions handler initialized")
            
            if ENABLE_PERFORMANCE_MONITORING:
                init_time = perf_monitor.end_timer('service_init')
                logger.info(f"Services initialized in {init_time:.2f}s")
                
        except Exception as e:
            self.error_handler.handle_error(e, "Service initialization", critical=True)
            raise
    
    def _request_permissions(self):
        """Request necessary permissions (Android)"""
        if self.permissions:
            self.permissions.request_microphone_permission()
            self.permissions.request_storage_permission()
    
    def _load_kv_files(self):
        """Load all KV files"""
        kv_path = os.path.join(os.path.dirname(__file__), '..', 'ui', 'kv')
        kv_files = [
            'base.kv',
            'splash.kv',
            'auth.kv',
            'dashboard.kv',
            'chat.kv',
            'notes.kv',
            'reminders.kv',
            'settings.kv',
        ]
        
        for kv_file in kv_files:
            try:
                file_path = os.path.join(kv_path, kv_file)
                if os.path.exists(file_path):
                    Builder.load_file(file_path)
                    logger.debug(f"Loaded: {kv_file}")
            except Exception as e:
                self.error_handler.handle_error(e, f"Loading {kv_file}", show_user=False)
    
    def _add_screens(self):
        """Add all screens to navigation manager"""
        try:
            screens = [
                SplashScreen(),
                LoginScreen(),
                SignupScreen(),
                DashboardScreen(),
                ChatScreen(),
                NotesScreen(),
                RemindersScreen(),
                SettingsScreen(),
            ]
            
            for screen in screens:
                self.nav_manager.add_widget(screen)
            
            logger.info(f"Added {len(screens)} screens")
            
        except Exception as e:
            self.error_handler.handle_error(e, "Adding screens", critical=True)
            raise
    
    def on_start(self):
        """
        Called when application starts
        """
        logger.info("🚀 Pipoo Application Started")
        logger.info(f"📱 Current Screen: {self.nav_manager.current}")
        
        if ENABLE_PERFORMANCE_MONITORING:
            perf_monitor.log_memory_usage()
    
    def update_auth_state(self, user):
        """Update authentication state across app"""
        self.current_user = user
        self.is_authenticated = True if user else False
        self.state_service.set_user(user)
        
        logger.info(f"Auth state updated: {user.username if user else 'None'}")
    
    def clear_auth_state(self):
        """Clear authentication state (logout)"""
        self.current_user = None
        self.is_authenticated = False
        self.state_service.clear_user()
        
        logger.info("Auth state cleared")
    
    def on_pause(self):
        """
        Handle application pause (Android)
        """
        logger.info("App paused")
        return True
    
    def on_resume(self):
        """
        Handle application resume (Android)
        """
        logger.info("App resumed")
    
    def on_stop(self):
        """
        Called when application is closing
        """
        try:
            # Stop voice services
            if self.voice_service:
                self.voice_service.stop_speaking()
                self.voice_service.stop_listening()
            
            # Optimize database
            if ENABLE_PERFORMANCE_MONITORING:
                perf_monitor.optimize_database(DB_PATH)
            
            # Log final stats
            uptime = perf_monitor.get_uptime()
            logger.info(f"App uptime: {uptime:.1f}s")
            logger.info("🛑 Pipoo Application Stopped")
            logger.info("=" * 50)
            
        except Exception as e:
            self.error_handler.handle_error(e, "App shutdown", show_user=False)