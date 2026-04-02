"""
Dashboard Screen - FIXED THREAD ISSUE
"""
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from config.settings import DEBUG_MODE
from kivy.clock import Clock


class DashboardScreen(Screen):
    """
    Main dashboard with daily briefing and smart suggestions
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'dashboard'
        self.briefing_dialog = None
    
    def on_enter(self):
        """Called when screen is displayed"""
        if DEBUG_MODE:
            print("📱 Dashboard Screen Loaded")
        
        # Load user data
        self.load_summary()
        
        # Generate AI summary
        Clock.schedule_once(lambda dt: self.generate_ai_summary(), 0.5)
    
    def load_summary(self):
        """Load today's summary data"""
        app = self.manager.app
        
        if not app.is_authenticated or not app.current_user:
            return
        
        user_id = app.current_user.id
        
        # Load notes count
        notes = app.storage_service.get_notes_by_user(user_id)
        self.ids.notes_count.text = str(len(notes))
        
        # Load reminders count
        reminders = app.storage_service.get_reminders_by_user(user_id, status='active')
        self.ids.reminders_count.text = str(len(reminders))
        
        # Load chat messages count (today)
        chat_history = app.storage_service.get_chat_history(user_id, limit=100)
        self.ids.chats_count.text = str(len(chat_history))
        
        # Store for AI summary
        self.current_notes = notes
        self.current_reminders = reminders
        
        if DEBUG_MODE:
            print(f"📊 Dashboard loaded: {len(notes)} notes, {len(reminders)} reminders, {len(chat_history)} chats")
    
    def generate_ai_summary(self):
        """Generate AI-powered daily summary"""
        app = self.manager.app
        
        if not app.ai_service.is_configured:
            self.ids.ai_summary.text = "💡 Connect Gemini API for AI-powered insights!"
            return
        
        # Check if there's data to summarize
        if not hasattr(self, 'current_notes') or not hasattr(self, 'current_reminders'):
            return
        
        if len(self.current_notes) == 0 and len(self.current_reminders) == 0:
            self.ids.ai_summary.text = "📝 Start by creating some notes or reminders!"
            return
        
        # Show loading
        self.ids.ai_summary.text = "✨ Generating insights..."
        
        # Generate summary
        success, summary = app.ai_service.generate_summary(self.current_notes, self.current_reminders)
        
        if success:
            self.ids.ai_summary.text = f"💡 {summary}"
        else:
            self.ids.ai_summary.text = "📊 Your productivity hub is ready!"
    
    def show_daily_briefing(self):
        """Show comprehensive daily briefing dialog"""
        app = self.manager.app
        user_id = app.current_user.id
        
        # Generate briefing
        briefing = app.productivity_service.generate_daily_briefing(user_id)
        
        # Create briefing content
        content = MDBoxLayout(
            orientation='vertical',
            spacing='15dp',
            size_hint_y=None,
            height='400dp',
            padding='10dp'
        )
        
        # Date
        date_label = MDLabel(
            text=f"[b]{briefing['date']}[/b]",
            markup=True,
            theme_text_color='Custom',
            text_color=app.colors['text_primary'],
            size_hint_y=None,
            height='30dp'
        )
        content.add_widget(date_label)
        
        # Summary
        if briefing['summary']:
            summary_label = MDLabel(
                text=f"💡 {briefing['summary']}",
                theme_text_color='Custom',
                text_color=app.colors['text_secondary'],
                size_hint_y=None,
                height='80dp'
            )
            content.add_widget(summary_label)
        
        # Statistics
        stats_text = f"""
📊 [b]Statistics[/b]
- Total Notes: {briefing['total_notes']} ({briefing['today_notes']} today)
- Active Reminders: {briefing['total_reminders']} ({briefing['today_reminders']} today)
        """
        
        stats_label = MDLabel(
            text=stats_text.strip(),
            markup=True,
            theme_text_color='Custom',
            text_color=app.colors['text_primary'],
            size_hint_y=None,
            height='100dp'
        )
        content.add_widget(stats_label)
        
        # Recent items
        if briefing['recent_notes']:
            recent_text = "\n📝 [b]Recent Notes:[/b]\n"
            for note in briefing['recent_notes']:
                recent_text += f"• {note.title}\n"
            
            recent_label = MDLabel(
                text=recent_text.strip(),
                markup=True,
                theme_text_color='Custom',
                text_color=app.colors['text_secondary'],
                size_hint_y=None,
                height='100dp'
            )
            content.add_widget(recent_label)
        
        # Create dialog
        self.briefing_dialog = MDDialog(
            title="📋 Daily Briefing",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="CLOSE",
                    on_release=lambda x: self.briefing_dialog.dismiss()
                ),
            ],
        )
        
        self.briefing_dialog.open()
    
    def goto_chat(self):
        """Navigate to chat screen"""
        self.manager.goto_screen('chat')
    
    def goto_notes(self):
        """Navigate to notes screen"""
        self.manager.goto_screen('notes')
    
    def goto_reminders(self):
        """Navigate to reminders screen"""
        self.manager.goto_screen('reminders')
    
    def goto_settings(self):
        """Navigate to settings screen"""
        self.manager.goto_screen('settings')
    
    def start_voice_input(self):
        """Trigger voice input from dashboard"""
        app = self.manager.app
        
        # Check if voice service is available
        tts_ok, stt_ok = app.voice_service.is_available()
        
        if not stt_ok:
            toast("Voice input not available on this device")
            return
        
        if app.voice_service.is_listening:
            toast("Already listening...")
            return
        
        # Check microphone permission (Android)
        if app.permissions and not app.permissions.check_microphone_permission():
            toast("Microphone permission required")
            app.permissions.request_microphone_permission(
                callback=lambda granted: self._start_listening() if granted else toast("Permission denied")
            )
            return
        
        self._start_listening()
    
    def _start_listening(self):
        """Start listening for voice input"""
        app = self.manager.app
        
        toast("🎤 Listening... Say 'chat', 'notes', or 'reminders'")
        
        if DEBUG_MODE:
            print("🎤 Dashboard voice input started...")
        
        # Listen
        app.voice_service.listen(self._on_voice_result)
    
    def _on_voice_result(self, success, result):
        """Handle voice recognition result - FIXED FOR THREAD SAFETY"""
        # Use Clock.schedule_once to run on main thread
        Clock.schedule_once(lambda dt: self._handle_voice_result(success, result), 0)
    
    def _handle_voice_result(self, success, result):
        """Handle voice result on main thread"""
        if not success:
            toast(f"Voice error: {result}")
            return
        
        text = result.lower()
        
        if DEBUG_MODE:
            print(f"🎤 Heard: {text}")
        
        # Parse command
        if 'chat' in text or 'talk' in text or 'speak' in text:
            toast("Opening chat...")
            self.goto_chat()
        elif 'note' in text or 'write' in text:
            toast("Opening notes...")
            self.goto_notes()
        elif 'remind' in text or 'reminder' in text:
            toast("Opening reminders...")
            self.goto_reminders()
        elif 'setting' in text:
            toast("Opening settings...")
            self.goto_settings()
        elif 'briefing' in text or 'summary' in text:
            self.show_daily_briefing()
        else:
            # Treat as chat message
            toast("Taking you to chat...")
            self.manager.goto_screen('chat')
            # Send message to chat
            Clock.schedule_once(lambda dt: self._send_to_chat(text), 0.5)
    
    def _send_to_chat(self, message):
        """Send voice message to chat screen"""
        chat_screen = self.manager.get_screen('chat')
        chat_screen.process_message(message)