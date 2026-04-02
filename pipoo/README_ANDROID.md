# Pipoo - Android Build Guide

## Prerequisites

### For Linux (Ubuntu/Debian):
```bash
# Install system dependencies
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# Install Cython
pip3 install --upgrade cython

# Install Buildozer
pip3 install --upgrade buildozer
```

### For Windows (WSL2):
1. Install WSL2 with Ubuntu
2. Follow Linux instructions above

### For macOS:
```bash
# Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install python3 autoconf automake libtool pkg-config
brew install --cask android-studio

# Install Buildozer
pip3 install --upgrade buildozer
```

---

## Building APK

### Step 1: Navigate to Project
```bash
cd /path/to/Pipoo
```

### Step 2: Initialize Buildozer (First Time Only)
```bash
buildozer init
# This creates buildozer.spec (already included in Phase 8)
```

### Step 3: Build Debug APK
```bash
# Clean build (recommended for first build)
buildozer android clean

# Build debug APK
buildozer -v android debug
```

This will:
- Download Android SDK/NDK (first time only, ~2-3 GB)
- Download Python-for-Android
- Compile all dependencies
- Create APK in `bin/` folder

**Build time**: 20-60 minutes (first build), 5-10 minutes (subsequent builds)

### Step 4: Install on Device
```bash
# Enable USB debugging on your Android device
# Connect device via USB

# Install APK
buildozer android deploy run
```

Or manually:
```bash
# Find APK in bin/ folder
adb install bin/pipoo-1.0.0-arm64-v8a-debug.apk
```

---

## Building Release APK (For Distribution)

### Step 1: Generate Keystore
```bash
keytool -genkey -v -keystore pipoo-release-key.keystore -alias pipoo -keyalg RSA -keysize 2048 -validity 10000
```

### Step 2: Configure buildozer.spec
Add to buildozer.spec:
```ini
[app]
# ... existing config ...

# Android signing
android.release_artifact = aab
android.sign_apk = True
android.keystore = pipoo-release-key.keystore
android.keystore_alias = pipoo
android.keystore_password = your_password
android.key_password = your_password
```

### Step 3: Build Release
```bash
buildozer android release
```

Output: `bin/pipoo-1.0.0-arm64-v8a-release-signed.apk`

---

## Troubleshooting

### Build Fails - "SDK not found"
```bash
# Set Android SDK path manually
export ANDROID_SDK_ROOT=$HOME/.buildozer/android/platform/android-sdk
```

### Build Fails - "NDK not found"
```bash
# Let buildozer download it automatically
buildozer android clean
buildozer -v android debug
```

### Build Fails - Java errors
```bash
# Install correct Java version
sudo apt install openjdk-17-jdk
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
```

### App Crashes on Android
```bash
# Check logs
buildozer android logcat

# Or using adb
adb logcat | grep python
```

### Permissions Not Working
- Ensure permissions are in buildozer.spec (already configured)
- Check `utils/permissions.py` is requesting runtime permissions
- Android 6.0+ requires runtime permission requests

### Voice Not Working on Android
- Check RECORD_AUDIO permission is granted
- Ensure microphone is not used by another app
- Test with: Settings → Apps → Pipoo → Permissions

### APK Size Too Large
Current APK will be ~50-80 MB. To reduce:
```ini
# In buildozer.spec, change:
android.archs = arm64-v8a
# Instead of: arm64-v8a, armeabi-v7a
```

---

## Testing on Device

### USB Debugging
1. Enable Developer Options on Android
2. Enable USB Debugging
3. Connect via USB
4. Accept debugging prompt on device

### Wireless Testing (Android 11+)
```bash
# Pair device
adb pair <device_ip>:port

# Connect
adb connect <device_ip>:5555

# Deploy
buildozer android deploy run
```

---

## APK Specifications

**Built APK Details:**
- Package: `com.pipoo.pipoo`
- Version: 1.0.0
- Min Android: 5.0 (API 21)
- Target Android: 13 (API 33)
- Architectures: ARM64-v8a, ARMv7a
- Size: ~50-80 MB
- Permissions: 7 (see buildozer.spec)

---

## Distribution

### Google Play Store
1. Build release APK
2. Create Google Play Developer account ($25 one-time)
3. Upload APK to Play Console
4. Fill app details
5. Submit for review

### Direct Distribution
1. Build release APK
2. Upload to website/GitHub
3. Users must enable "Install from Unknown Sources"

---

## Updating the App

### Version Bump
Edit `buildozer.spec`:
```ini
version = 1.0.1
```

### Rebuild
```bash
buildozer android clean
buildozer android release
```

---

## Common Build Commands
```bash
# Clean build files
buildozer android clean

# Debug build
buildozer -v android debug

# Release build
buildozer android release

# Deploy to connected device
buildozer android deploy

# Build and deploy
buildozer android debug deploy run

# View logs
buildozer android logcat

# List connected devices
adb devices
```

---

## File Locations After Build
```
Pipoo/
├── bin/
│   └── pipoo-1.0.0-arm64-v8a-debug.apk  (Your APK!)
├── .buildozer/
│   └── android/
│       ├── platform/  (Android SDK/NDK)
│       └── app/       (Compiled app)
└── buildozer.spec
```

---

## Android-Specific Code

All Android-specific code is already implemented in:
- `utils/permissions.py` - Runtime permissions
- `services/voice_service.py` - Android TTS/STT
- `config/settings.py` - Platform detection

**No additional Android code needed!**

---

## Support

**Build Issues:**
- Check Buildozer docs: https://buildozer.readthedocs.io/
- Python-for-Android: https://python-for-android.readthedocs.io/

**App Issues:**
- Check logcat: `adb logcat | grep python`
- Enable DEBUG_MODE in config/settings.py

---

## Notes

- First build takes 30-60 minutes (downloads SDK/NDK)
- Subsequent builds take 5-10 minutes
- Clean build recommended after major changes
- Test on multiple Android versions if possible
- Voice features require Android 5.0+
- AI features require internet connection
```

---

## 4. Update `.gitignore` (if not exists, create it)
```
# Buildozer files
.buildozer/
bin/
*.apk
*.aab

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# Kivy
*.pyc
.kivy/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Data
data/app.db
data/*.log

# Keys
*.keystore
*.jks