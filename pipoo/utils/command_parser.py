"""
Command Parser - Parse natural language commands
"""
from config.settings import DEBUG_MODE
import re
from datetime import datetime, timedelta


class CommandParser:
    """
    Parse natural language commands for productivity features
    """
    
    # Command patterns
    NOTE_KEYWORDS = ['note', 'write', 'remember', 'jot', 'save']
    REMINDER_KEYWORDS = ['remind', 'reminder', 'alert', 'notify', 'schedule']
    SEARCH_KEYWORDS = ['search', 'find', 'look', 'google']
    OPEN_KEYWORDS = ['open', 'launch', 'start', 'run']
    TIME_KEYWORDS = ['at', 'by', 'on', 'tomorrow', 'today', 'tonight', 'morning', 'afternoon', 'evening']
    
    @staticmethod
    def parse_command(text):
        """
        Parse command from text
        
        Args:
            text (str): User input text
        
        Returns:
            dict: Parsed command or None
        """
        text_lower = text.lower().strip()
        
        # Check for note command
        if CommandParser._is_note_command(text_lower):
            return CommandParser._parse_note_command(text, text_lower)
        
        # Check for reminder command
        if CommandParser._is_reminder_command(text_lower):
            return CommandParser._parse_reminder_command(text, text_lower)
        
        # Check for search command
        if CommandParser._is_search_command(text_lower):
            return CommandParser._parse_search_command(text, text_lower)
        
        # Check for open command
        if CommandParser._is_open_command(text_lower):
            return CommandParser._parse_open_command(text, text_lower)
        
        # No command detected
        return None
    
    @staticmethod
    def _is_note_command(text):
        """Check if text is a note command"""
        return any(keyword in text for keyword in CommandParser.NOTE_KEYWORDS)
    
    @staticmethod
    def _is_reminder_command(text):
        """Check if text is a reminder command"""
        return any(keyword in text for keyword in CommandParser.REMINDER_KEYWORDS)
    
    @staticmethod
    def _is_search_command(text):
        """Check if text is a search command"""
        return any(keyword in text for keyword in CommandParser.SEARCH_KEYWORDS)
    
    @staticmethod
    def _is_open_command(text):
        """Check if text is an open command"""
        return any(keyword in text for keyword in CommandParser.OPEN_KEYWORDS)
    
    @staticmethod
    def _parse_note_command(text, text_lower):
        """Parse note creation command"""
        # Find content after note keyword
        for keyword in CommandParser.NOTE_KEYWORDS:
            if keyword in text_lower:
                # Find position of keyword
                pos = text_lower.find(keyword)
                # Get content after keyword
                content = text[pos + len(keyword):].strip()
                
                # Remove common prefixes
                prefixes = ['that', 'this', 'to', 'down', ':']
                for prefix in prefixes:
                    if content.lower().startswith(prefix):
                        content = content[len(prefix):].strip()
                
                if content:
                    return {
                        'type': 'note',
                        'content': content,
                        'title': None  # Will be generated
                    }
        
        return None
    
    @staticmethod
    def _parse_reminder_command(text, text_lower):
        """Parse reminder creation command"""
        # Extract time if present
        time_info = CommandParser._extract_time(text_lower)
        
        # Find content
        content = text
        for keyword in CommandParser.REMINDER_KEYWORDS:
            if keyword in text_lower:
                pos = text_lower.find(keyword)
                content = text[pos + len(keyword):].strip()
                
                # Remove common prefixes
                prefixes = ['me', 'to', 'about']
                for prefix in prefixes:
                    if content.lower().startswith(prefix):
                        content = content[len(prefix):].strip()
                
                break
        
        # Remove time string from content
        if time_info and time_info.get('time_str'):
            content = content.replace(time_info['time_str'], '').strip()
        
        if content:
            return {
                'type': 'reminder',
                'title': content,
                'time': time_info.get('datetime') if time_info else None,
                'time_str': time_info.get('formatted') if time_info else None
            }
        
        return None
    
    @staticmethod
    def _extract_time(text):
        """Extract time information from text"""
        now = datetime.now()
        
        # Check for "tomorrow"
        if 'tomorrow' in text:
            target_date = now + timedelta(days=1)
            
            # Check for specific time
            time_match = re.search(r'(\d{1,2}):?(\d{2})?\s*(am|pm)?', text, re.IGNORECASE)
            if time_match:
                hour = int(time_match.group(1))
                minute = int(time_match.group(2)) if time_match.group(2) else 0
                am_pm = time_match.group(3)
                
                if am_pm and am_pm.lower() == 'pm' and hour < 12:
                    hour += 12
                elif am_pm and am_pm.lower() == 'am' and hour == 12:
                    hour = 0
                
                target_time = target_date.replace(hour=hour, minute=minute, second=0, microsecond=0)
            else:
                # Default to 9 AM tomorrow
                target_time = target_date.replace(hour=9, minute=0, second=0, microsecond=0)
            
            return {
                'datetime': target_time,
                'formatted': target_time.strftime("%I:%M %p"),
                'time_str': 'tomorrow'
            }
        
        # Check for "today" or "tonight"
        if 'today' in text or 'tonight' in text:
            if 'tonight' in text:
                target_time = now.replace(hour=20, minute=0, second=0, microsecond=0)
            else:
                # Check for specific time
                time_match = re.search(r'(\d{1,2}):?(\d{2})?\s*(am|pm)?', text, re.IGNORECASE)
                if time_match:
                    hour = int(time_match.group(1))
                    minute = int(time_match.group(2)) if time_match.group(2) else 0
                    am_pm = time_match.group(3)
                    
                    if am_pm and am_pm.lower() == 'pm' and hour < 12:
                        hour += 12
                    elif am_pm and am_pm.lower() == 'am' and hour == 12:
                        hour = 0
                    
                    target_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
                else:
                    # Default to 1 hour from now
                    target_time = now + timedelta(hours=1)
            
            return {
                'datetime': target_time,
                'formatted': target_time.strftime("%I:%M %p"),
                'time_str': 'today' if 'today' in text else 'tonight'
            }
        
        # Check for specific time format (e.g., "at 3pm", "at 15:30")
        time_match = re.search(r'at\s+(\d{1,2}):?(\d{2})?\s*(am|pm)?', text, re.IGNORECASE)
        if time_match:
            hour = int(time_match.group(1))
            minute = int(time_match.group(2)) if time_match.group(2) else 0
            am_pm = time_match.group(3)
            
            if am_pm and am_pm.lower() == 'pm' and hour < 12:
                hour += 12
            elif am_pm and am_pm.lower() == 'am' and hour == 12:
                hour = 0
            
            target_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            
            # If time has passed today