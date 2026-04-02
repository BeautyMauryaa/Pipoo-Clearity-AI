"""
Storage Service - SQLite Database Management
"""
import sqlite3
from datetime import datetime
from config.settings import DB_PATH, DEBUG_MODE
from models import User, Note, Reminder, ChatMessage
import os


class StorageService:
    """
    SQLite database service for data persistence
    """
    
    def __init__(self):
        self.db_path = DB_PATH
        self._init_database()
    
    def _init_database(self):
        """Initialize database and create tables"""
        # Ensure data directory exists
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        ''')
        
        # Notes table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')
        
        # Reminders table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reminders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                time TEXT NOT NULL,
                recurring TEXT DEFAULT 'none',
                status TEXT DEFAULT 'active',
                created_at TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')
        
        # Chat history table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')
        
        conn.commit()
        conn.close()
        
        if DEBUG_MODE:
            print("✅ Database initialized")
    
    # ==================== USER OPERATIONS ====================
    
    def create_user(self, username, password_hash):
        """Create new user"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            created_at = datetime.now().isoformat()
            
            cursor.execute('''
                INSERT INTO users (username, password_hash, created_at)
                VALUES (?, ?, ?)
            ''', (username, password_hash, created_at))
            
            user_id = cursor.lastrowid
            conn.commit()
            conn.close()
            
            if DEBUG_MODE:
                print(f"✅ User created: {username}")
            
            return User(id=user_id, username=username, password_hash=password_hash, created_at=created_at)
        except sqlite3.IntegrityError:
            if DEBUG_MODE:
                print(f"❌ Username already exists: {username}")
            return None
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Error creating user: {e}")
            return None
    
    def get_user_by_username(self, username):
        """Get user by username"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            row = cursor.fetchone()
            conn.close()
            
            if row:
                return User(id=row[0], username=row[1], password_hash=row[2], created_at=row[3])
            return None
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Error fetching user: {e}")
            return None
    
    def get_user_by_id(self, user_id):
        """Get user by ID"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
            row = cursor.fetchone()
            conn.close()
            
            if row:
                return User(id=row[0], username=row[1], password_hash=row[2], created_at=row[3])
            return None
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Error fetching user: {e}")
            return None
    
    # ==================== NOTE OPERATIONS ====================
    
    def create_note(self, user_id, title, content):
        """Create new note"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            now = datetime.now().isoformat()
            
            cursor.execute('''
                INSERT INTO notes (user_id, title, content, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (user_id, title, content, now, now))
            
            note_id = cursor.lastrowid
            conn.commit()
            conn.close()
            
            if DEBUG_MODE:
                print(f"✅ Note created: {title}")
            
            return Note(id=note_id, user_id=user_id, title=title, content=content, created_at=now, updated_at=now)
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Error creating note: {e}")
            return None
    
    def get_notes_by_user(self, user_id):
        """Get all notes for a user"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM notes WHERE user_id = ? ORDER BY updated_at DESC', (user_id,))
            rows = cursor.fetchall()
            conn.close()
            
            notes = []
            for row in rows:
                notes.append(Note(
                    id=row[0],
                    user_id=row[1],
                    title=row[2],
                    content=row[3],
                    created_at=row[4],
                    updated_at=row[5]
                ))
            
            return notes
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Error fetching notes: {e}")
            return []
    
    def update_note(self, note_id, title, content):
        """Update existing note"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            updated_at = datetime.now().isoformat()
            
            cursor.execute('''
                UPDATE notes SET title = ?, content = ?, updated_at = ?
                WHERE id = ?
            ''', (title, content, updated_at, note_id))
            
            conn.commit()
            conn.close()
            
            if DEBUG_MODE:
                print(f"✅ Note updated: {note_id}")
            
            return True
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Error updating note: {e}")
            return False
    
    def delete_note(self, note_id):
        """Delete note"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
            
            conn.commit()
            conn.close()
            
            if DEBUG_MODE:
                print(f"✅ Note deleted: {note_id}")
            
            return True
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Error deleting note: {e}")
            return False
    
    # ==================== REMINDER OPERATIONS ====================
    
    def create_reminder(self, user_id, title, time, recurring='none'):
        """Create new reminder"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            created_at = datetime.now().isoformat()
            
            cursor.execute('''
                INSERT INTO reminders (user_id, title, time, recurring, status, created_at)
                VALUES (?, ?, ?, ?, 'active', ?)
            ''', (user_id, title, time, recurring, created_at))
            
            reminder_id = cursor.lastrowid
            conn.commit()
            conn.close()
            
            if DEBUG_MODE:
                print(f"✅ Reminder created: {title}")
            
            return Reminder(
                id=reminder_id,
                user_id=user_id,
                title=title,
                time=time,
                recurring=recurring,
                status='active',
                created_at=created_at
            )
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Error creating reminder: {e}")
            return None
    
    def get_reminders_by_user(self, user_id, status='active'):
        """Get all reminders for a user"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            if status:
                cursor.execute('SELECT * FROM reminders WHERE user_id = ? AND status = ? ORDER BY time', (user_id, status))
            else:
                cursor.execute('SELECT * FROM reminders WHERE user_id = ? ORDER BY time', (user_id,))
            
            rows = cursor.fetchall()
            conn.close()
            
            reminders = []
            for row in rows:
                reminders.append(Reminder(
                    id=row[0],
                    user_id=row[1],
                    title=row[2],
                    time=row[3],
                    recurring=row[4],
                    status=row[5],
                    created_at=row[6]
                ))
            
            return reminders
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Error fetching reminders: {e}")
            return []
    
    def update_reminder_status(self, reminder_id, status):
        """Update reminder status"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('UPDATE reminders SET status = ? WHERE id = ?', (status, reminder_id))
            
            conn.commit()
            conn.close()
            
            if DEBUG_MODE:
                print(f"✅ Reminder status updated: {reminder_id} -> {status}")
            
            return True
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Error updating reminder: {e}")
            return False
    
    def delete_reminder(self, reminder_id):
        """Delete reminder"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM reminders WHERE id = ?', (reminder_id,))
            
            conn.commit()
            conn.close()
            
            if DEBUG_MODE:
                print(f"✅ Reminder deleted: {reminder_id}")
            
            return True
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Error deleting reminder: {e}")
            return False
    
    # ==================== CHAT OPERATIONS ====================
    
    def save_chat_message(self, user_id, role, content):
        """Save chat message"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            timestamp = datetime.now().isoformat()
            
            cursor.execute('''
                INSERT INTO chat_history (user_id, role, content, timestamp)
                VALUES (?, ?, ?, ?)
            ''', (user_id, role, content, timestamp))
            
            message_id = cursor.lastrowid
            conn.commit()
            conn.close()
            
            return ChatMessage(id=message_id, user_id=user_id, role=role, content=content, timestamp=timestamp)
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Error saving chat message: {e}")
            return None
    
    def get_chat_history(self, user_id, limit=50):
        """Get chat history for a user"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT * FROM chat_history 
                WHERE user_id = ? 
                ORDER BY timestamp DESC 
                LIMIT ?
            ''', (user_id, limit))
            
            rows = cursor.fetchall()
            conn.close()
            
            messages = []
            for row in reversed(rows):  # Reverse to show oldest first
                messages.append(ChatMessage(
                    id=row[0],
                    user_id=row[1],
                    role=row[2],
                    content=row[3],
                    timestamp=row[4]
                ))
            
            return messages
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Error fetching chat history: {e}")
            return []
    
    def clear_chat_history(self, user_id):
        """Clear chat history for a user"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM chat_history WHERE user_id = ?', (user_id,))
            
            conn.commit()
            conn.close()
            
            if DEBUG_MODE:
                print(f"✅ Chat history cleared for user: {user_id}")
            
            return True
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Error clearing chat history: {e}")
            return False