"""
AI Service - Gemini 2.5 Flash API Integration
"""
import google.generativeai as genai
from config.settings import (
    GEMINI_API_KEY, 
    GEMINI_MODEL, 
    AI_TEMPERATURE, 
    AI_MAX_TOKENS,
    AI_MAX_HISTORY,
    AI_TIMEOUT,
    DEBUG_MODE
)
import time


class AIService:
    """
    Gemini 2.5 Flash AI service for conversational AI
    """
    
    def __init__(self):
        """Initialize Gemini API"""
        if not GEMINI_API_KEY or GEMINI_API_KEY == "YOUR_GEMINI_API_KEY_HERE":
            if DEBUG_MODE:
                print("⚠️ Gemini API key not configured!")
            self.model = None
            self.is_configured = False
            return
        
        try:
            # Configure API
            genai.configure(api_key=GEMINI_API_KEY)
            
            # Initialize model with generation config
            generation_config = {
                "temperature": AI_TEMPERATURE,
                "max_output_tokens": AI_MAX_TOKENS,
            }
            
            self.model = genai.GenerativeModel(
                model_name=GEMINI_MODEL,
                generation_config=generation_config
            )
            
            self.is_configured = True
            
            if DEBUG_MODE:
                print(f"✅ Gemini AI initialized: {GEMINI_MODEL}")
        
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Failed to initialize Gemini: {e}")
            self.model = None
            self.is_configured = False
    
    def generate_response(self, user_message, chat_history=None):
        """
        Generate AI response
        
        Args:
            user_message (str): User's message
            chat_history (list): List of previous messages (optional)
        
        Returns:
            tuple: (success, response_or_error)
        """
        if not self.is_configured:
            return False, "AI service not configured. Please add your Gemini API key."
        
        try:
            # Build conversation context
            conversation = self._build_conversation_context(user_message, chat_history)
            
            if DEBUG_MODE:
                print(f"🤖 Generating response for: {user_message[:50]}...")
            
            # Generate response
            start_time = time.time()
            response = self.model.generate_content(conversation)
            elapsed_time = time.time() - start_time
            
            if DEBUG_MODE:
                print(f"✅ Response generated in {elapsed_time:.2f}s")
            
            # Extract text from response
            if response and response.text:
                return True, response.text
            else:
                return False, "No response generated"
        
        except Exception as e:
            error_msg = str(e)
            if DEBUG_MODE:
                print(f"❌ AI generation error: {error_msg}")
            
            # Handle specific errors
            if "API_KEY_INVALID" in error_msg or "invalid" in error_msg.lower():
                return False, "Invalid API key. Please check your Gemini API key."
            elif "quota" in error_msg.lower() or "limit" in error_msg.lower():
                return False, "API quota exceeded. Please try again later."
            elif "timeout" in error_msg.lower():
                return False, "Request timed out. Please try again."
            else:
                return False, f"AI error: {error_msg}"
    
    def _build_conversation_context(self, user_message, chat_history=None):
        """
        Build conversation context with system prompt and history
        
        Args:
            user_message (str): Current user message
            chat_history (list): Previous messages
        
        Returns:
            str: Formatted conversation
        """
        # System prompt
        system_prompt = """You are Pipoo, a helpful AI voice assistant. You are:
- Friendly, conversational, and concise
- Helpful with productivity tasks like notes and reminders
- Knowledgeable across various topics
- Able to understand context from conversation history

Keep responses clear and under 200 words unless the user asks for more detail.
"""
        
        # Start with system prompt
        conversation_parts = [system_prompt]
        
        # Add recent history (limit to last N messages)
        if chat_history:
            recent_history = chat_history[-AI_MAX_HISTORY:] if len(chat_history) > AI_MAX_HISTORY else chat_history
            
            for msg in recent_history:
                role = msg.get('role', '')
                content = msg.get('content', '')
                
                if role == 'user':
                    conversation_parts.append(f"User: {content}")
                elif role == 'ai':
                    conversation_parts.append(f"Assistant: {content}")
        
        # Add current message
        conversation_parts.append(f"User: {user_message}")
        conversation_parts.append("Assistant:")
        
        return "\n\n".join(conversation_parts)
    
    def generate_summary(self, notes, reminders):
        """
        Generate daily summary based on notes and reminders
        
        Args:
            notes (list): List of notes
            reminders (list): List of reminders
        
        Returns:
            tuple: (success, summary_or_error)
        """
        if not self.is_configured:
            return False, "AI service not configured"
        
        try:
            # Build summary prompt
            prompt = f"""Generate a brief daily summary (2-3 sentences) based on:

Notes ({len(notes)} total):
"""
            
            for note in notes[:5]:  # Limit to 5 most recent
                prompt += f"- {note.title}\n"
            
            prompt += f"\nReminders ({len(reminders)} active):\n"
            
            for reminder in reminders[:5]:  # Limit to 5
                prompt += f"- {reminder.title}\n"
            
            prompt += "\nProvide an encouraging, concise summary."
            
            # Generate summary
            response = self.model.generate_content(prompt)
            
            if response and response.text:
                return True, response.text
            else:
                return False, "Could not generate summary"
        
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Summary generation error: {e}")
            return False, "Failed to generate summary"
    
    def extract_task_from_message(self, message):
        """
        Extract task/reminder from natural language
        
        Args:
            message (str): User message
        
        Returns:
            dict: Extracted task info or None
        """
        if not self.is_configured:
            return None
        
        try:
            prompt = f"""Analyze this message and extract task/reminder information if present:
"{message}"

If this contains a task or reminder, respond with JSON:
{{
    "is_task": true/false,
    "title": "task title",
    "time": "HH:MM" (if mentioned, otherwise null),
    "type": "note" or "reminder"
}}

If no task/reminder, respond with: {{"is_task": false}}
"""
            
            response = self.model.generate_content(prompt)
            
            if response and response.text:
                # Try to parse JSON from response
                import json
                import re
                
                # Extract JSON from response (in case there's extra text)
                json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                if json_match:
                    task_data = json.loads(json_match.group())
                    return task_data if task_data.get('is_task') else None
            
            return None
        
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Task extraction error: {e}")
            return None
    
    def generate_note_title(self, content):
        """
        Generate a title for note content
        
        Args:
            content (str): Note content
        
        Returns:
            str: Generated title
        """
        if not self.is_configured:
            return "Untitled Note"
        
        try:
            prompt = f"""Generate a concise title (3-5 words) for this note:

{content[:200]}

Respond with ONLY the title, nothing else."""
            
            response = self.model.generate_content(prompt)
            
            if response and response.text:
                title = response.text.strip().strip('"\'')
                return title[:50]  # Limit length
            else:
                return "Untitled Note"
        
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Title generation error: {e}")
            return "Untitled Note"
    
    def check_api_key(self):
        """
        Check if API key is valid
        
        Returns:
            tuple: (is_valid, message)
        """
        if not GEMINI_API_KEY or GEMINI_API_KEY == "YOUR_GEMINI_API_KEY_HERE":
            return False, "API key not configured"
        
        if not self.is_configured:
            return False, "Failed to initialize API"
        
        try:
            # Test API with simple request
            response = self.model.generate_content("Hello")
            return True, "API key is valid"
        except Exception as e:
            return False, f"API key error: {str(e)}"