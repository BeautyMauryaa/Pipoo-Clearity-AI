from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.spinner import MDSpinner
from kivymd.toast import toast
from kivy.clock import Clock
from kivy.app import App
from datetime import datetime
from config.settings import DEBUG_MODE


class ChatScreen(Screen):
    def _on_voice_result(self, success, result):
        """Handle voice recognition result"""
        # Use Clock.schedule_once to run on main thread
        Clock.schedule_once(lambda dt: self._handle_voice_result(success, result), 0)
    
    def _handle_voice_result(self, success, result):
        """Handle voice result on main thread"""
        # Reset icon
        try:
            self.ids.voice_button.icon = "microphone"
        except:
            pass
        
        if success:
            # Process the recognized text
            self.process_message(result)
        else:
            toast(f"Voice error: {result}")
            self.is_voice_active = False
            
            if DEBUG_MODE:
                print(f"❌ Voice recognition error: {result}")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "chat"
        self.chat_history = []
        self.is_generating = False
        self.is_voice_active = False

    def on_enter(self):
        if DEBUG_MODE:
            print("📱 Chat Screen Loaded")

        self.load_chat_history()

    def load_chat_history(self):
        app = App.get_running_app()

        if not app.is_authenticated or not app.current_user:
            return

        user_id = app.current_user.id
        messages = app.storage_service.get_chat_history(user_id, limit=50)

        self.chat_history = [msg.to_dict() for msg in messages]

        app.state_service.update_chat_history(self.chat_history)
        self.refresh_chat_ui()

        if DEBUG_MODE:
            print(f"💬 Loaded {len(self.chat_history)} messages")

    def refresh_chat_ui(self):
        container = self.ids.chat_container
        container.clear_widgets()

        if not self.chat_history:
            welcome = MDLabel(
                text="👋 Hello! I'm Pipoo, your AI assistant.",
                halign="center",
                size_hint_y=None,
                height="200dp"
            )
            container.add_widget(welcome)
            return

        for msg in self.chat_history:
            container.add_widget(self.create_message_bubble(msg))

        Clock.schedule_once(lambda dt: self.scroll_to_bottom(), 0.1)

    def scroll_to_bottom(self):
        try:
            self.ids.chat_scroll.scroll_y = 0
        except Exception:
            pass

    def create_message_bubble(self, message):
        is_user = message["role"] == "user"

        bubble = MDCard(
            padding="15dp",
            size_hint_x=0.75,
            pos_hint={"right": 1} if is_user else {"x": 0}
        )

        bubble.add_widget(MDLabel(text=message["content"]))
        return bubble

    def send_message(self):
        if self.is_generating:
            toast("Please wait")
            return

        text = self.ids.message_input.text.strip()
        if not text:
            return

        self.ids.message_input.text = ""
        self.process_message(text)

    def process_message(self, message):
        app = App.get_running_app()
        user_id = app.current_user.id

        self.add_message("user", message)
        app.storage_service.save_chat_message(user_id, "user", message)

        self.show_loading()
        Clock.schedule_once(lambda dt: self.generate_ai_response(message), 0.1)

    def show_loading(self):
        self.is_generating = True

    def remove_loading(self):
        self.is_generating = False

    def generate_ai_response(self, user_message):
        app = App.get_running_app()

        self.remove_loading()
        success, response = app.ai_service.generate_response(
            user_message, self.chat_history
        )

        role = "ai"
        self.add_message(role, response)
        app.storage_service.save_chat_message(app.current_user.id, role, response)

    def add_message(self, role, content):
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        }

        self.chat_history.append(message)
        self.ids.chat_container.add_widget(self.create_message_bubble(message))
        self.scroll_to_bottom()

    def go_back(self):
        app = App.get_running_app()
        app.voice_service.stop_speaking()
        app.voice_service.stop_listening()
        self.manager.goto_screen("dashboard", direction="right")
