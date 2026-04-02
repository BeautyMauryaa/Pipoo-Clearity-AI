"""
Pipoo - AI Voice Desk
Entry Point
"""
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.app import PipooApp


def main():
    """
    Application entry point
    """
    try:
        app = PipooApp()
        app.run()
    except Exception as e:
        print(f"❌ Fatal Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()