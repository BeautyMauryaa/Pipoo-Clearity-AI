from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.toast import toast
from config.settings import DEBUG_MODE
from utils.validators import Validators
from utils.helpers import Helpers


class NotesScreen(Screen):
    """
    Notes manager screen
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'notes'
        self.notes = []
        self.dialog = None
        self.edit_dialog = None
        self.editing_note_id = None
    
    def on_enter(self):
        """Called when screen is displayed"""
        if DEBUG_MODE:
            print("📱 Notes Screen Loaded")
        
        # Load notes
        self.load_notes()
    
    def load_notes(self):
        """Load notes from storage"""
        app = self.manager.app
        
        if not app.is_authenticated or not app.current_user:
            return
        
        user_id = app.current_user.id
        self.notes = app.storage_service.get_notes_by_user(user_id)
        
        # Update state
        app.state_service.update_notes(self.notes)
        
        # Refresh UI
        self.refresh_notes_list()
        
        if DEBUG_MODE:
            print(f"📝 Loaded {len(self.notes)} notes")
    
    def refresh_notes_list(self):
        """Refresh the notes list UI"""
        # Clear existing notes
        container = self.ids.notes_container
        container.clear_widgets()
        
        if not self.notes:
            # Show empty state
            empty_label = MDLabel(
                text="No notes yet.\nTap + to create your first note!",
                halign='center',
                theme_text_color='Custom',
                text_color=self.manager.app.colors['text_secondary'],
                size_hint_y=None,
                height='100dp'
            )
            container.add_widget(empty_label)
            return
        
        # Add note cards
        for note in self.notes:
            card = self.create_note_card(note)
            container.add_widget(card)
    
    def create_note_card(self, note):
        """Create a note card widget"""
        card = MDCard(
            orientation='vertical',
            padding='20dp',
            spacing='10dp',
            md_bg_color=self.manager.app.colors['surface'],
            elevation=2,
            radius=[15],
            size_hint_y=None,
            height='140dp',
            ripple_behavior=True,
        )
        
        # Title
        title_label = MDLabel(
            text=note.title,
            font_size='18sp',
            bold=True,
            theme_text_color='Custom',
            text_color=self.manager.app.colors['text_primary'],
            size_hint_y=None,
            height='30dp'
        )
        
        # Content preview
        content_preview = Helpers.truncate_text(note.content, 80)
        content_label = MDLabel(
            text=content_preview,
            font_size='14sp',
            theme_text_color='Custom',
            text_color=self.manager.app.colors['text_secondary'],
            size_hint_y=None,
            height='60dp'
        )
        
        # Date
        date_str = Helpers.format_date(note.updated_at)
        date_label = MDLabel(
            text=date_str,
            font_size='12sp',
            theme_text_color='Custom',
            text_color=self.manager.app.colors['text_secondary'],
            size_hint_y=None,
            height='20dp'
        )
        
        card.add_widget(title_label)
        card.add_widget(content_label)
        card.add_widget(date_label)
        
        # Add tap handler to edit
        card.bind(on_release=lambda x: self.edit_note(note))
        
        return card
    
    def show_add_note_dialog(self):
        """Show dialog to add new note"""
        content = MDBoxLayout(
            orientation='vertical',
            spacing='15dp',
            size_hint_y=None,
            height='250dp',
            padding='10dp'
        )
        
        title_field = MDTextField(
            hint_text="Title",
            mode="rectangle",
        )
        
        content_field = MDTextField(
            hint_text="Content",
            mode="rectangle",
            multiline=True,
            size_hint_y=None,
            height='150dp'
        )
        
        content.add_widget(title_field)
        content.add_widget(content_field)
        
        self.dialog = MDDialog(
            title="Add New Note",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    on_release=lambda x: self.dialog.dismiss()
                ),
                MDRaisedButton(
                    text="SAVE",
                    on_release=lambda x: self.save_new_note(title_field.text, content_field.text)
                ),
            ],
        )
        
        self.dialog.open()
    
    def save_new_note(self, title, content):
        """Save new note"""
        # Validate title
        is_valid, error = Validators.validate_note_title(title)
        if not is_valid:
            toast(error)
            return
        
        # Validate content
        is_valid, error = Validators.validate_note_content(content)
        if not is_valid:
            toast(error)
            return
        
        app = self.manager.app
        user_id = app.current_user.id
        
        # Create note
        note = app.storage_service.create_note(user_id, title.strip(), content.strip())
        
        if note:
            toast("Note saved!")
            self.dialog.dismiss()
            self.load_notes()
        else:
            toast("Failed to save note")
    
    def edit_note(self, note):
        """Show dialog to edit note"""
        self.editing_note_id = note.id
        
        content = MDBoxLayout(
            orientation='vertical',
            spacing='15dp',
            size_hint_y=None,
            height='300dp',
            padding='10dp'
        )
        
        title_field = MDTextField(
            hint_text="Title",
            mode="rectangle",
            text=note.title
        )
        
        content_field = MDTextField(
            hint_text="Content",
            mode="rectangle",
            multiline=True,
            text=note.content,
            size_hint_y=None,
            height='150dp'
        )
        
        content.add_widget(title_field)
        content.add_widget(content_field)
        
        self.edit_dialog = MDDialog(
            title="Edit Note",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="DELETE",
                    theme_text_color='Custom',
                    text_color=self.manager.app.colors['error'],
                    on_release=lambda x: self.delete_note_confirm(note.id)
                ),
                MDFlatButton(
                    text="CANCEL",
                    on_release=lambda x: self.edit_dialog.dismiss()
                ),
                MDRaisedButton(
                    text="UPDATE",
                    on_release=lambda x: self.update_note(note.id, title_field.text, content_field.text)
                ),
            ],
        )
        
        self.edit_dialog.open()
    
    def update_note(self, note_id, title, content):
        """Update existing note"""
        # Validate title
        is_valid, error = Validators.validate_note_title(title)
        if not is_valid:
            toast(error)
            return
        
        # Validate content
        is_valid, error = Validators.validate_note_content(content)
        if not is_valid:
            toast(error)
            return
        
        app = self.manager.app
        
        # Update note
        success = app.storage_service.update_note(note_id, title.strip(), content.strip())
        
        if success:
            toast("Note updated!")
            self.edit_dialog.dismiss()
            self.load_notes()
        else:
            toast("Failed to update note")
    
    def delete_note_confirm(self, note_id):
        """Confirm and delete note"""
        if self.edit_dialog:
            self.edit_dialog.dismiss()
        
        app = self.manager.app
        success = app.storage_service.delete_note(note_id)
        
        if success:
            toast("Note deleted")
            self.load_notes()
        else:
            toast("Failed to delete note")
    
    def go_back(self):
        """Navigate back to dashboard"""
        self.manager.goto_screen('dashboard', direction='right')