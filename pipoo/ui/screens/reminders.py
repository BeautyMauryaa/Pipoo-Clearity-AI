from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.icon_definitions import md_icons
from kivymd.toast import toast
from config.settings import DEBUG_MODE
from utils.validators import Validators
from utils.helpers import Helpers
from datetime import datetime, timedelta


class RemindersScreen(Screen):
    """
    Reminders manager screen
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'reminders'
        self.reminders = []
        self.dialog = None
    
    def on_enter(self):
        """Called when screen is displayed"""
        if DEBUG_MODE:
            print("📱 Reminders Screen Loaded")
        
        # Load reminders
        self.load_reminders()
    
    def load_reminders(self):
        """Load reminders from storage"""
        app = self.manager.app
        
        if not app.is_authenticated or not app.current_user:
            return
        
        user_id = app.current_user.id
        self.reminders = app.storage_service.get_reminders_by_user(user_id, status='active')
        
        # Update state
        app.state_service.update_reminders(self.reminders)
        
        # Refresh UI
        self.refresh_reminders_list()
        
        if DEBUG_MODE:
            print(f"⏰ Loaded {len(self.reminders)} reminders")
    
    def refresh_reminders_list(self):
        """Refresh the reminders list UI"""
        # Clear existing reminders
        container = self.ids.reminders_container
        container.clear_widgets()
        
        # Add header
        header = MDLabel(
            text="Active Reminders",
            font_size='16sp',
            bold=True,
            theme_text_color='Custom',
            text_color=self.manager.app.colors['text_secondary'],
            size_hint_y=None,
            height='30dp'
        )
        container.add_widget(header)
        
        if not self.reminders:
            # Show empty state
            empty_label = MDLabel(
                text="No active reminders.\nTap + to create one!",
                halign='center',
                theme_text_color='Custom',
                text_color=self.manager.app.colors['text_secondary'],
                size_hint_y=None,
                height='100dp'
            )
            container.add_widget(empty_label)
            return
        
        # Add reminder cards
        for reminder in self.reminders:
            card = self.create_reminder_card(reminder)
            container.add_widget(card)
    
    def create_reminder_card(self, reminder):
        """Create a reminder card widget"""
        card = MDCard(
            orientation='horizontal',
            padding='15dp',
            spacing='15dp',
            md_bg_color=self.manager.app.colors['surface'],
            elevation=2,
            radius=[15],
            size_hint_y=None,
            height='80dp'
        )
        
        # Icon
        from kivymd.uix.label import MDIcon
        icon = MDIcon(
            icon="bell",
            theme_text_color='Custom',
            text_color=self.manager.app.colors['primary'],
            font_size='32sp',
            size_hint_x=None,
            width='40dp',
            pos_hint={'center_y': 0.5}
        )
        
        # Content box
        content_box = MDBoxLayout(
            orientation='vertical',
            spacing='5dp',
        )
        
        title_label = MDLabel(
            text=reminder.title,
            font_size='16sp',
            bold=True,
            theme_text_color='Custom',
            text_color=self.manager.app.colors['text_primary']
        )
        
        time_label = MDLabel(
            text=Helpers.format_time(reminder.time),
            font_size='14sp',
            theme_text_color='Custom',
            text_color=self.manager.app.colors['text_secondary']
        )
        
        content_box.add_widget(title_label)
        content_box.add_widget(time_label)
        
        # Complete button
        complete_btn = MDIconButton(
            icon="check-circle",
            theme_text_color='Custom',
            text_color=self.manager.app.colors['success'],
            size_hint_x=None,
            width='40dp',
            on_release=lambda x: self.complete_reminder(reminder.id)
        )
        
        card.add_widget(icon)
        card.add_widget(content_box)
        card.add_widget(complete_btn)
        
        return card
    
    def show_add_reminder_dialog(self):
        """Show dialog to add reminder"""
        content = MDBoxLayout(
            orientation='vertical',
            spacing='15dp',
            size_hint_y=None,
            height='200dp',
            padding='10dp'
        )
        
        title_field = MDTextField(
            hint_text="Reminder Title",
            mode="rectangle",
        )
        
        # Simple time input (HH:MM format)
        time_field = MDTextField(
            hint_text="Time (HH:MM, e.g., 14:30)",
            mode="rectangle",
        )
        
        content.add_widget(title_field)
        content.add_widget(time_field)
        
        self.dialog = MDDialog(
            title="Add Reminder",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    on_release=lambda x: self.dialog.dismiss()
                ),
                MDRaisedButton(
                    text="SAVE",
                    on_release=lambda x: self.save_reminder(title_field.text, time_field.text)
                ),
            ],
        )
        
        self.dialog.open()
    
    def save_reminder(self, title, time_str):
        """Save new reminder"""
        # Validate title
        is_valid, error = Validators.validate_reminder_title(title)
        if not is_valid:
            toast(error)
            return
        
        # Parse time
        try:
            # Simple time parsing (HH:MM)
            time_parts = time_str.strip().split(':')
            if len(time_parts) != 2:
                toast("Invalid time format. Use HH:MM (e.g., 14:30)")
                return
            
            hour = int(time_parts[0])
            minute = int(time_parts[1])
            
            if hour < 0 or hour > 23 or minute < 0 or minute > 59:
                toast("Invalid time. Hour must be 0-23, minute 0-59")
                return
            
            # Create datetime for today at specified time
            now = datetime.now()
            reminder_time = datetime(now.year, now.month, now.day, hour, minute)
            
            # If time has passed today, set for tomorrow
            if reminder_time < now:
                reminder_time += timedelta(days=1)
            
        except ValueError:
            toast("Invalid time format. Use HH:MM (e.g., 14:30)")
            return
        
        app = self.manager.app
        user_id = app.current_user.id
        
        # Create reminder
        reminder = app.storage_service.create_reminder(
            user_id,
            title.strip(),
            reminder_time.isoformat()
        )
        
        if reminder:
            toast("Reminder created!")
            self.dialog.dismiss()
            self.load_reminders()
        else:
            toast("Failed to create reminder")
    
    def complete_reminder(self, reminder_id):
        """Mark reminder as completed"""
        app = self.manager.app
        success = app.storage_service.update_reminder_status(reminder_id, 'completed')
        
        if success:
            toast("Reminder completed!")
            self.load_reminders()
        else:
            toast("Failed to complete reminder")
    
    def go_back(self):
        """Navigate back to dashboard"""
        self.manager.goto_screen('dashboard', direction='right')