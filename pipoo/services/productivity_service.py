"""
Productivity Service - Advanced productivity features
"""
from config.settings import DEBUG_MODE
from utils.command_parser import CommandParser
from datetime import datetime
import webbrowser
import subprocess
import os


class ProductivityService:
    """
    Productivity tools and utilities
    """
    
    def __init__(self, storage_service, ai_service):
        """
        Initialize productivity service
        
        Args:
            storage_service: Storage service instance
            ai_service: AI service instance
        """
        self.storage = storage_service
        self.ai = ai_service
        self.command_parser = CommandParser()
    
    # ==================== COMMAND EXECUTION ====================
    
    def execute_command(self, text, user_id):
        """
        Execute productivity command from text
        
        Args:
            text (str): Command text
            user_id (int): User ID
        
        Returns:
            tuple: (success, message, command_type)
        """
        # Parse command
        command = self.command_parser.parse_command(text)
        
        if not command:
            return False, "No command detected", None
        
        command_type = command.get('type')
        
        if DEBUG_MODE:
            print(f"🎯 Executing command: {command_type}")
        
        # Execute based on type
        if command_type == 'note':
            return self._execute_note_command(command, user_id)
        elif command_type == 'reminder':
            return self._execute_reminder_command(command, user_id)
        elif command_type == 'search':
            return self._execute_search_command(command)
        elif command_type == 'open':
            return self._execute_open_command(command)
        else:
            return False, "Unknown command type", None
    
    def _execute_note_command(self, command, user_id):
        """Execute note creation command"""
        content = command.get('content', '')
        
        if not content:
            return False, "No note content provided", 'note'
        
        # Generate title using AI if available
        if self.ai.is_configured:
            title = self.ai.generate_note_title(content)
        else:
            # Fallback: Use first few words
            words = content.split()[:5]
            title = ' '.join(words)
            if len(content.split()) > 5:
                title += '...'
        
        # Create note
        note = self.storage.create_note(user_id, title, content)
        
        if note:
            if DEBUG_MODE:
                print(f"✅ Created note: {title}")
            return True, f"Note created: {title}", 'note'
        else:
            return False, "Failed to create note", 'note'
    
    def _execute_reminder_command(self, command, user_id):
        """Execute reminder creation command"""
        title = command.get('title', '')
        time_dt = command.get('time')
        time_str = command.get('time_str', 'later')
        
        if not title:
            return False, "No reminder title provided", 'reminder'
        
        # If no time specified, set for 1 hour from now
        if not time_dt:
            from datetime import timedelta
            time_dt = datetime.now() + timedelta(hours=1)
            time_str = "in 1 hour"
        
        # Create reminder
        reminder = self.storage.create_reminder(
            user_id,
            title,
            time_dt.isoformat()
        )
        
        if reminder:
            if DEBUG_MODE:
                print(f"✅ Created reminder: {title} at {time_str}")
            return True, f"Reminder set: {title} ({time_str})", 'reminder'
        else:
            return False, "Failed to create reminder", 'reminder'
    
    def _execute_search_command(self, command):
        """Execute web search command"""
        query = command.get('query', '')
        
        if not query:
            return False, "No search query provided", 'search'
        
        try:
            # Open Google search in browser
            search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(search_url)
            
            if DEBUG_MODE:
                print(f"🔍 Opened search: {query}")
            
            return True, f"Searching for: {query}", 'search'
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Search error: {e}")
            return False, f"Search failed: {str(e)}", 'search'
    
    def _execute_open_command(self, command):
        """Execute open app command"""
        app_name = command.get('app', '').lower()
        
        if not app_name:
            return False, "No app name provided", 'open'
        
        try:
            # Common app mappings
            app_paths = {
                'notepad': 'notepad.exe',
                'calculator': 'calc.exe',
                'paint': 'mspaint.exe',
                'chrome': 'chrome.exe',
                'firefox': 'firefox.exe',
                'edge': 'msedge.exe',
                'explorer': 'explorer.exe',
                'file explorer': 'explorer.exe',
            }
            
            # Try to find app
            app_to_open = app_paths.get(app_name, app_name)
            
            # Try to open
            if os.name == 'nt':  # Windows
                subprocess.Popen(app_to_open, shell=True)
            else:  # Linux/Mac
                subprocess.Popen([app_to_open])
            
            if DEBUG_MODE:
                print(f"🚀 Opened app: {app_name}")
            
            return True, f"Opening: {app_name}", 'open'
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Open app error: {e}")
            return False, f"Could not open {app_name}", 'open'
    
    # ==================== DAILY BRIEFING ====================
    
    def generate_daily_briefing(self, user_id):
        """
        Generate comprehensive daily briefing
        
        Args:
            user_id (int): User ID
        
        Returns:
            dict: Briefing data
        """
        # Get data
        notes = self.storage.get_notes_by_user(user_id)
        reminders = self.storage.get_reminders_by_user(user_id, status='active')
        chat_history = self.storage.get_chat_history(user_id, limit=10)
        
        # Count today's items
        today = datetime.now().date()
        today_notes = [n for n in notes if self._is_today(n.created_at)]
        today_reminders = [r for r in reminders if self._is_today(r.time)]
        
        briefing = {
            'date': datetime.now().strftime("%A, %B %d, %Y"),
            'total_notes': len(notes),
            'total_reminders': len(reminders),
            'today_notes': len(today_notes),
            'today_reminders': len(today_reminders),
            'recent_notes': notes[:3] if notes else [],
            'upcoming_reminders': reminders[:5] if reminders else [],
            'summary': None
        }
        
        # Generate AI summary if available
        if self.ai.is_configured and (notes or reminders):
            success, summary = self.ai.generate_summary(notes[:5], reminders[:5])
            if success:
                briefing['summary'] = summary
        
        return briefing
    
    def _is_today(self, date_str):
        """Check if date string is today"""
        try:
            if isinstance(date_str, str):
                dt = datetime.fromisoformat(date_str)
            else:
                dt = date_str
            
            return dt.date() == datetime.now().date()
        except:
            return False
    
    # ==================== SMART SUGGESTIONS ====================
    
    def get_smart_suggestions(self, user_id):
        """
        Get smart productivity suggestions
        
        Args:
            user_id (int): User ID
        
        Returns:
            list: List of suggestions
        """
        suggestions = []
        
        # Get user data
        notes = self.storage.get_notes_by_user(user_id)
        reminders = self.storage.get_reminders_by_user(user_id, status='active')
        
        # Suggestion: Review old notes
        old_notes = [n for n in notes if self._is_old(n.updated_at, days=7)]
        if old_notes:
            suggestions.append({
                'type': 'review',
                'message': f"You have {len(old_notes)} notes from last week. Time to review?",
                'action': 'open_notes'
            })
        
        # Suggestion: Upcoming reminders
        soon_reminders = [r for r in reminders if self._is_soon(r.time, hours=2)]
        if soon_reminders:
            suggestions.append({
                'type': 'reminder',
                'message': f"{len(soon_reminders)} reminder(s) in the next 2 hours",
                'action': 'open_reminders'
            })
        
        # Suggestion: Create daily note
        today_notes = [n for n in notes if self._is_today(n.created_at)]
        if not today_notes:
            suggestions.append({
                'type': 'create',
                'message': "Start your day by creating a note",
                'action': 'create_note'
            })
        
        return suggestions
    
    def _is_old(self, date_str, days=7):
        """Check if date is older than N days"""
        try:
            if isinstance(date_str, str):
                dt = datetime.fromisoformat(date_str)
            else:
                dt = date_str
            
            age = datetime.now() - dt
            return age.days >= days
        except:
            return False
    
    def _is_soon(self, date_str, hours=2):
        """Check if date is within N hours"""
        try:
            if isinstance(date_str, str):
                dt = datetime.fromisoformat(date_str)
            else:
                dt = date_str
            
            time_until = dt - datetime.now()
            return 0 <= time_until.total_seconds() <= (hours * 3600)
        except:
            return False