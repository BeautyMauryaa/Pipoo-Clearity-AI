# Pipoo Deployment Guide

## Quick Start

### Desktop (Windows)
```powershell
# Clone repository
git clone https://github.com/yourusername/pipoo.git
cd pipoo

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure API key
# Edit config/settings.py
# GEMINI_API_KEY = "your_key_here"

# Run application
python main.py
```

### Android
```bash
# Install Buildozer
pip install buildozer

# Build APK
buildozer -v android debug

# Install on device
adb install bin/pipoo-1.0.0-arm64-v8a-debug.apk
```

---

## Configuration

### 1. Gemini API Key (Required for AI features)
```python
# config/settings.py
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
```

Get key from: https://aistudio.google.com/app/apikey

### 2. Voice Settings
```python
# config/settings.py
STT_LANGUAGE = "en-US"  # Change for other languages
TTS_RATE = 150          # Speech speed
USE_GOOGLE_STT = True   # Requires internet
```

### 3. Performance Tuning
```python
# config/settings.py
ENABLE_PERFORMANCE_MONITORING = True
DATABASE_OPTIMIZE_INTERVAL = 86400  # 24 hours
MAX_CHAT_HISTORY_MEMORY = 100
```

---

## Building for Production

### Windows EXE
```powershell
# Build executable
pyinstaller pipoo.spec

# Create installer (optional)
# Use Inno Setup with installer.iss

# Output
dist/Pipoo/Pipoo.exe
```

### Android APK
```bash
# Release build
buildozer android release

# Sign APK
keytool -genkey -v -keystore pipoo.keystore -alias pipoo -keyalg RSA -keysize 2048 -validity 10000
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore pipoo.keystore bin/pipoo.apk pipoo
```

---

## Deployment Checklist

### Pre-Deploy
- [ ] Update version in config/settings.py
- [ ] Test all features on target platform
- [ ] Verify API keys are configured
- [ ] Check permissions are granted
- [ ] Test voice input/output
- [ ] Verify database operations
- [ ] Test offline functionality
- [ ] Check error handling
- [ ] Review logs for issues

### Windows
- [ ] Build with PyInstaller
- [ ] Test on clean Windows system
- [ ] Check antivirus compatibility
- [ ] Verify all DLLs included
- [ ] Test installer (if using Inno Setup)
- [ ] Sign executable (production)

### Android
- [ ] Build with Buildozer
- [ ] Test on multiple Android versions
- [ ] Verify all permissions work
- [ ] Check voice on different devices
- [ ] Test offline mode
- [ ] Optimize APK size
- [ ] Sign release APK

### Post-Deploy
- [ ] Monitor crash reports
- [ ] Track performance metrics
- [ ] Collect user feedback
- [ ] Update documentation
- [ ] Plan next version features

---

## Troubleshooting

### API Issues
```
Error: AI not configured
Solution: Add Gemini API key in config/settings.py
```

### Voice Issues
```
Error: Microphone permission denied
Solution: Grant permission in Settings → Apps → Pipoo
```

### Database Issues
```
Error: Database locked
Solution: Close other instances of the app
```

### Build Issues
```
Error: Module not found
Solution: pip install -r requirements.txt
```

---

## Monitoring

### Logs Location
- Windows: `data/app.log`
- Android: Use `adb logcat`

### Performance Metrics
- Startup time
- Memory usage
- API response time
- Database query time

### Error Tracking
- All errors logged to `data/app.log`
- Critical errors shown to user
- Stack traces in debug mode

---

## Support

### Documentation
- README.md - Quick start
- README_ANDROID.md - Android build
- README_WINDOWS.md - Windows build
- CHANGELOG.md - Version history

### Community
- GitHub Issues: Report bugs
- Discussions: Feature requests
- Wiki: Extended documentation

---

## License

[Your License Here]

## Credits

- Kivy/KivyMD: UI framework
- Google Generative AI: AI chat
- pyttsx3: Text-to-speech
- SpeechRecognition: Speech-to-text