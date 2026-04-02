# -*- mode: python ; coding: utf-8 -*-

import os
from kivy_deps import sdl2, glew, angle
from kivymd import hooks_path as kivymd_hooks_path

block_cipher = None

# Get the app directory
app_dir = os.path.dirname(os.path.abspath(SPEC))

# Collect all .kv files
kv_files = []
for root, dirs, files in os.walk(os.path.join(app_dir, 'ui', 'kv')):
    for file in files:
        if file.endswith('.kv'):
            kv_files.append((os.path.join(root, file), 'ui/kv'))

# Collect all data files
data_files = [
    (os.path.join(app_dir, 'config'), 'config'),
]

a = Analysis(
    ['main.py'],
    pathex=[app_dir],
    binaries=[],
    datas=kv_files + data_files,
    hiddenimports=[
        'pkg_resources.py2_warn',
        'win32timezone',
        'plyer.platforms.win.notification',
        'google.generativeai',
        'google.ai.generativelanguage',
        'google.api_core',
        'google.auth',
        'kivymd.uix.behaviors',
        'kivymd.uix.button',
        'kivymd.uix.card',
        'kivymd.uix.dialog',
        'kivymd.uix.label',
        'kivymd.uix.textfield',
        'kivymd.uix.toolbar',
        'kivymd.uix.spinner',
        'kivymd.uix.boxlayout',
        'kivymd.uix.floatlayout',
        'kivymd.uix.gridlayout',
        'kivymd.icon_definitions',
    ],
    hookspath=[kivymd_hooks_path],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Pipoo',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Set to True for debugging
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if os.path.exists('icon.ico') else None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins + angle.dep_bins)],
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Pipoo',
)