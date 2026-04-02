#!/bin/bash

echo "🚀 Building Pipoo Android APK..."
echo ""

# Check if buildozer is installed
if ! command -v buildozer &> /dev/null
then
    echo "❌ Buildozer not installed!"
    echo "Install with: pip3 install buildozer"
    exit 1
fi

# Clean previous build
echo "🧹 Cleaning previous build..."
buildozer android clean

# Build debug APK
echo "🔨 Building debug APK..."
buildozer -v android debug

# Check if build succeeded
if [ -f "bin/pipoo-1.0.0-arm64-v8a-debug.apk" ]; then
    echo ""
    echo "✅ Build successful!"
    echo "📦 APK Location: bin/pipoo-1.0.0-arm64-v8a-debug.apk"
    echo ""
    echo "To install on device:"
    echo "  adb install bin/pipoo-1.0.0-arm64-v8a-debug.apk"
    echo ""
    echo "Or run:"
    echo "  buildozer android deploy run"
else
    echo ""
    echo "❌ Build failed!"
    echo "Check the output above for errors"
    exit 1
fi