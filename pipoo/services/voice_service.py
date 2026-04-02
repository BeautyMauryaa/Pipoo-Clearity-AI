"""
Voice Service - UPDATED WITH BETTER MICROPHONE HANDLING
"""
import threading
from config.settings import (
    IS_ANDROID,
    IS_WINDOWS,
    STT_LANGUAGE,
    STT_TIMEOUT,
    STT_PHRASE_LIMIT,
    TTS_RATE,
    TTS_VOLUME,
    TTS_VOICE_INDEX,
    USE_GOOGLE_STT,
    DEBUG_MODE
)


class VoiceService:
    """
    Cross-platform voice service for STT and TTS
    """
    
    def __init__(self):
        """Initialize voice service"""
        self.is_listening = False
        self.is_speaking = False
        self.stt_engine = None
        self.tts_engine = None
        
        # Initialize TTS
        self._init_tts()
        
        # Initialize STT
        self._init_stt()
    
    def _init_tts(self):
        """Initialize Text-to-Speech engine"""
        try:
            if IS_ANDROID:
                # Android TTS
                from jnius import autoclass
                self.tts_class = autoclass('android.speech.tts.TextToSpeech')
                self.locale_class = autoclass('java.util.Locale')
                self.PythonActivity = autoclass('org.kivy.android.PythonActivity')
                
                # Initialize will happen on first speak
                self.tts_initialized = False
                
                if DEBUG_MODE:
                    print("✅ Android TTS ready")
            else:
                # Desktop TTS (pyttsx3)
                import pyttsx3
                self.tts_engine = pyttsx3.init()
                
                # Configure voice
                voices = self.tts_engine.getProperty('voices')
                if voices and len(voices) > TTS_VOICE_INDEX:
                    self.tts_engine.setProperty('voice', voices[TTS_VOICE_INDEX].id)
                
                # Configure rate and volume
                self.tts_engine.setProperty('rate', TTS_RATE)
                self.tts_engine.setProperty('volume', TTS_VOLUME)
                
                if DEBUG_MODE:
                    print("✅ Desktop TTS initialized")
        
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ TTS initialization error: {e}")
            self.tts_engine = None
    
    def _init_stt(self):
        """Initialize Speech-to-Text engine"""
        try:
            if IS_ANDROID:
                # Android STT (will use SpeechRecognizer)
                from jnius import autoclass
                self.SpeechRecognizer = autoclass('android.speech.SpeechRecognizer')
                self.RecognizerIntent = autoclass('android.speech.RecognizerIntent')
                self.Intent = autoclass('android.content.Intent')
                
                if DEBUG_MODE:
                    print("✅ Android STT ready")
            else:
                # Desktop STT (SpeechRecognition)
                import speech_recognition as sr
                self.stt_engine = sr.Recognizer()
                
                # IMPROVED: Better microphone settings
                self.stt_engine.energy_threshold = 300  # Lowered from 4000 (more sensitive)
                self.stt_engine.dynamic_energy_threshold = True
                self.stt_engine.pause_threshold = 0.8  # Seconds of silence to consider phrase complete
                
                if DEBUG_MODE:
                    print("✅ Desktop STT initialized")
        
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ STT initialization error: {e}")
            self.stt_engine = None
    
    # ==================== TEXT-TO-SPEECH ====================
    
    def speak(self, text, callback=None):
        """
        Speak text using TTS
        
        Args:
            text (str): Text to speak
            callback (function): Called when speech completes
        """
        if not text:
            if callback:
                callback(False, "No text to speak")
            return
        
        if self.is_speaking:
            if DEBUG_MODE:
                print("⚠️ Already speaking, skipping")
            if callback:
                callback(False, "Already speaking")
            return
        
        # Run in thread to avoid blocking UI
        thread = threading.Thread(target=self._speak_thread, args=(text, callback))
        thread.daemon = True
        thread.start()
    
    def _speak_thread(self, text, callback):
        """Internal speak thread"""
        self.is_speaking = True
        
        try:
            if IS_ANDROID:
                self._speak_android(text)
            else:
                self._speak_desktop(text)
            
            if DEBUG_MODE:
                print(f"🔊 Spoke: {text[:50]}...")
            
            if callback:
                callback(True, "Speech completed")
        
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ TTS error: {e}")
            
            if callback:
                callback(False, str(e))
        
        finally:
            self.is_speaking = False
    
    def _speak_android(self, text):
        """Speak using Android TTS"""
        try:
            # Initialize TTS if needed
            if not self.tts_initialized:
                context = self.PythonActivity.mActivity
                self.tts = self.tts_class(context, None)
                self.tts.setLanguage(self.locale_class.US)
                self.tts_initialized = True
                
                # Wait for initialization
                import time
                time.sleep(0.5)
            
            # Speak
            self.tts.speak(text, self.tts_class.QUEUE_FLUSH, None, None)
            
            # Wait for speech to complete (rough estimation)
            import time
            words = len(text.split())
            duration = (words / TTS_RATE) * 60
            time.sleep(duration)
        
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Android TTS error: {e}")
            raise
    
    def _speak_desktop(self, text):
        """Speak using desktop TTS"""
        if not self.tts_engine:
            raise Exception("TTS engine not initialized")
        
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()
    
    def stop_speaking(self):
        """Stop current speech"""
        try:
            if IS_ANDROID and hasattr(self, 'tts') and self.tts_initialized:
                self.tts.stop()
            elif self.tts_engine:
                self.tts_engine.stop()
            
            self.is_speaking = False
            
            if DEBUG_MODE:
                print("🔇 Speech stopped")
        
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Stop speaking error: {e}")
    
    # ==================== SPEECH-TO-TEXT ====================
    
    def listen(self, callback):
        """
        Listen for speech and convert to text
        
        Args:
            callback (function): Called with (success, text_or_error)
        """
        if self.is_listening:
            if DEBUG_MODE:
                print("⚠️ Already listening")
            callback(False, "Already listening")
            return
        
        # Run in thread to avoid blocking UI
        thread = threading.Thread(target=self._listen_thread, args=(callback,))
        thread.daemon = True
        thread.start()
    
    def _listen_thread(self, callback):
        """Internal listen thread"""
        self.is_listening = True
        
        try:
            if IS_ANDROID:
                text = self._listen_android()
            else:
                text = self._listen_desktop()
            
            if text:
                if DEBUG_MODE:
                    print(f"🎤 Heard: {text}")
                callback(True, text)
            else:
                callback(False, "No speech detected")
        
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ STT error: {e}")
            callback(False, str(e))
        
        finally:
            self.is_listening = False
    
    def _listen_android(self):
        """Listen using Android Speech Recognizer"""
        try:
            from jnius import autoclass, PythonJavaClass, java_method
            from android import activity
            
            # Create intent
            intent = self.Intent(self.RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
            intent.putExtra(
                self.RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                self.RecognizerIntent.LANGUAGE_MODEL_FREE_FORM
            )
            intent.putExtra(self.RecognizerIntent.EXTRA_LANGUAGE, STT_LANGUAGE)
            intent.putExtra(self.RecognizerIntent.EXTRA_MAX_RESULTS, 1)
            
            # Start recognition activity
            activity.startActivityForResult(intent, 1234)
            
            # Wait for result (simplified - in production use proper callback)
            import time
            time.sleep(5)
            
            # Result will be handled by activity callback
            # For now, return placeholder
            return None
        
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Android STT error: {e}")
            raise
    
    def _listen_desktop(self):
        """Listen using desktop Speech Recognition"""
        if not self.stt_engine:
            raise Exception("STT engine not initialized")
        
        import speech_recognition as sr
        
        with sr.Microphone() as source:
            if DEBUG_MODE:
                print("🎤 Adjusting for ambient noise... (speak now)")
            
            # IMPROVED: Longer adjustment time, lower threshold
            try:
                self.stt_engine.adjust_for_ambient_noise(source, duration=1)
            except:
                pass  # Continue even if adjustment fails
            
            if DEBUG_MODE:
                print(f"🎤 Listening... (energy threshold: {self.stt_engine.energy_threshold})")
            
            try:
                # Listen with longer timeout
                audio = self.stt_engine.listen(
                    source,
                    timeout=10,  # Increased from 5 to 10 seconds
                    phrase_time_limit=STT_PHRASE_LIMIT
                )
                
                if DEBUG_MODE:
                    print("🔄 Processing speech...")
                
                # Recognize
                if USE_GOOGLE_STT:
                    # Google Speech Recognition (requires internet)
                    text = self.stt_engine.recognize_google(audio, language=STT_LANGUAGE)
                else:
                    # Sphinx (offline, lower accuracy)
                    text = self.stt_engine.recognize_sphinx(audio)
                
                return text
                
            except sr.WaitTimeoutError:
                if DEBUG_MODE:
                    print("⏱️ No speech detected within timeout")
                return None
    
    def stop_listening(self):
        """Stop listening"""
        self.is_listening = False
        
        if DEBUG_MODE:
            print("🔇 Listening stopped")
    
    # ==================== UTILITY ====================
    
    def is_available(self):
        """
        Check if voice service is available
        
        Returns:
            tuple: (tts_available, stt_available)
        """
        tts_available = self.tts_engine is not None or IS_ANDROID
        stt_available = self.stt_engine is not None or IS_ANDROID
        
        return tts_available, stt_available
    
    def get_voices(self):
        """
        Get available TTS voices (desktop only)
        
        Returns:
            list: Available voices
        """
        if IS_ANDROID:
            return []
        
        if not self.tts_engine:
            return []
        
        try:
            voices = self.tts_engine.getProperty('voices')
            return [{'id': v.id, 'name': v.name} for v in voices]
        except:
            return []