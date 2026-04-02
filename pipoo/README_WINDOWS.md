# Pipoo - Windows Build Guide

## Prerequisites

### Windows 10/11:
- Python 3.11+ installed
- Visual Studio Build Tools (for some dependencies)
- Virtual environment activated

### Install Build Tools:
```powershell
# Download from: https://visualstudio.microsoft.com/downloads/
# Install "Desktop development with C++"
```

---

## Building .exe

### Method 1: Using Batch Script (Recommended)
```batch
# Simply double-click:
build_windows.bat

# Or run in CMD:
build_windows.bat
```

### Method 2: Manual Build
```powershell
# 1. Activate virtual environment
venv\Scripts\activate

# 2. Install PyInstaller
pip install pyinstaller

# 3. Build
pyinstaller pipoo.spec

# Output: dist\Pipoo\Pipoo.exe
```

---

## Build Output

After successful build:
```
Pipoo/
├── dist/
│   └── Pipoo/
│       ├── Pipoo.exe          ← Your executable!
│       ├── _internal/          ← Required DLLs and files
│       ├── ui/                 ← UI files
│       └── config/             ← Config files
└── build/                      ← Temporary build files
```

**Important:** The entire `dist/Pipoo/` folder is needed to run the app!

---

## Running the Executable

### Option 1: From dist folder
```batch
cd dist\Pipoo
Pipoo.exe
```

### Option 2: Create desktop shortcut
1. Right-click `dist\Pipoo\Pipoo.exe`
2. Send to → Desktop (create shortcut)
3. Rename shortcut to "Pipoo"

---

## Creating Installer (Optional)

### Using Inno Setup (Recommended)

#### 1. Install Inno Setup
Download from: https://jrsoftware.org/isdl.php

#### 2. Create `installer.iss`
```ini
[Setup]
AppName=Pipoo
AppVersion=1.0.0
DefaultDirName={autopf}\Pipoo
DefaultGroupName=Pipoo
OutputDir=installer
OutputBaseFilename=Pipoo-Setup-1.0.0
Compression=lzma2
SolidCompression=yes
PrivilegesRequired=lowest
UninstallDisplayIcon={app}\Pipoo.exe

[Files]
Source: "dist\Pipoo\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Pipoo"; Filename: "{app}\Pipoo.exe"
Name: "{group}\Uninstall Pipoo"; Filename: "{uninstallexe}"
Name: "{autodesktop}\Pipoo"; Filename: "{app}\Pipoo.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"

[Run]
Filename: "{app}\Pipoo.exe"; Description: "Launch Pipoo"; Flags: nowait postinstall skipifsilent
```

#### 3. Compile Installer
```batch
# Right-click installer.iss → Compile
# Or use command line:
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer.iss
```

Output: `installer/Pipoo-Setup-1.0.0.exe`

---

## Troubleshooting

### Build Fails - "Module not found"
```powershell
# Reinstall dependencies in virtual environment
pip install --force-reinstall -r requirements.txt
```

### Build Fails - "UPX not available"

Edit `pipoo.spec`:
```python
upx=False,  # Change from True to False
```

### Executable Won't Start
```powershell
# Build with console to see errors
# Edit pipoo.spec:
console=True,  # Change from False

# Rebuild
pyinstaller pipoo.spec
```

### "VCRUNTIME140.dll missing"

Install Visual C++ Redistributable:
https://aka.ms/vs/17/release/vc_redist.x64.exe

### Antivirus Blocking

- Windows Defender may flag PyInstaller executables
- Add exception for `dist\Pipoo\` folder
- Or sign the executable (see Signing section)

### Slow Startup

First launch is slower (10-15 seconds) as it extracts files.
Subsequent launches are faster (2-3 seconds).

---

## Optimizing Build

### Reduce Size
```python
# In pipoo.spec, add to excludes:
excludes=[
    'matplotlib',
    'numpy',
    'pandas',
    'scipy',
    'PIL',
    'tkinter',
],
```

### Single File Build (Not Recommended)
```python
# In pipoo.spec:
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,  # Add this
    a.zipfiles,  # Add this
    a.datas,     # Add this
    [],
    name='Pipoo',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    onefile=True,  # Add this
)
```

Note: Single file is slower to start (extracts to temp each time)

---

## Signing Executable (Optional)

### Using SignTool (Windows SDK)
```powershell
# 1. Get code signing certificate
# Purchase from DigiCert, Sectigo, etc.

# 2. Sign executable
signtool sign /f certificate.pfx /p password /t http://timestamp.digicert.com dist\Pipoo\Pipoo.exe
```

Signed executables:
- Avoid antivirus warnings
- Show publisher name
- Increase user trust

---

## Distribution

### Method 1: Zip File
```powershell
# Compress dist\Pipoo folder
Compress-Archive -Path dist\Pipoo -DestinationPath Pipoo-Windows-1.0.0.zip
```

Users extract and run `Pipoo.exe`

### Method 2: Installer

Use Inno Setup installer (see above)

Users run `Pipoo-Setup-1.0.0.exe`

### Method 3: Microsoft Store

1. Create MSIX package
2. Register as Windows developer ($19)
3. Submit to Microsoft Store

---

## File Specifications

**Built Executable:**
- Name: Pipoo.exe
- Size: ~150-200 MB (with dependencies)
- Architecture: x64
- Min OS: Windows 10 (64-bit)
- Dependencies: Bundled in _internal/

**Installer:**
- Size: ~100 MB (compressed)
- Includes: All required files
- Creates: Start menu shortcut, desktop icon

---

## Testing Executable

### Test on Clean System

1. Copy `dist\Pipoo` to USB drive
2. Test on different Windows PC
3. Verify all features work:
   - Login/Signup
   - Notes CRUD
   - Reminders
   - Voice input
   - AI chat

### Common Test Issues

- **Voice not working**: Requires microphone permission
- **Database not saving**: Check folder write permissions
- **Slow startup**: Normal for first launch

---

## Updates and Versioning

### Update Version

1. Edit `pipoo.spec`:
```python
# Change in main.py or config/settings.py:
APP_VERSION = "1.0.1"
```

2. Rebuild:
```batch
build_windows.bat
```

### Update Installer

1. Edit `installer.iss`:
```ini
AppVersion=1.0.1
OutputBaseFilename=Pipoo-Setup-1.0.1
```

2. Recompile installer

---

## Auto-Update (Advanced)

Implement in future version:
```python
# Check for updates on startup
def check_updates():
    latest = requests.get("https://yourserver.com/latest_version.json")
    if latest['version'] > APP_VERSION:
        # Prompt user to download update
        pass
```

---

## Build Comparison

| Feature | PyInstaller | cx_Freeze | Nuitka |
|---------|-------------|-----------|--------|
| Ease | ✅ Easy | ⚠️ Medium | ❌ Complex |
| Size | 150 MB | 180 MB | 120 MB |
| Speed | Fast | Fast | Very Fast |
| Support | Excellent | Good | Good |

**Recommendation:** PyInstaller (already configured)

---

## Common Build Commands
```powershell
# Clean build
pyinstaller --clean pipoo.spec

# Build with console (for debugging)
# Edit pipoo.spec: console=True
pyinstaller pipoo.spec

# One-file build (not recommended)
pyinstaller --onefile main.py

# Check build size
Get-ChildItem dist\Pipoo -Recurse | Measure-Object -Property Length -Sum
```

---

## Support

**Build Issues:**
- PyInstaller Docs: https://pyinstaller.org/
- StackOverflow: Search "PyInstaller Kivy"

**Runtime Issues:**
- Run with console=True to see errors
- Check Windows Event Viewer
- Enable DEBUG_MODE in config/settings.py

---

## Notes

- First build takes 10-15 minutes
- Subsequent builds take 2-3 minutes
- Clean build recommended after major changes
- Test on clean Windows system before distribution
- Consider code signing for production release
- Bundle Visual C++ Redistributable for wider compatibility