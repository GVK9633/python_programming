#!/usr/bin/env python3
"""
Snake Game Launcher
A simple script to check dependencies and launch the Snake game.
"""

import subprocess
import sys
import os

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = ['streamlit', 'pygame', 'numpy', 'pillow']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} is installed")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} is missing")
    
    if missing_packages:
        print(f"\n📦 Installing missing packages: {', '.join(missing_packages)}")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing_packages)
            print("✅ All packages installed successfully!")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install packages. Please run: pip install -r requirements.txt")
            return False
    
    return True

def launch_game():
    """Launch the Snake game"""
    print("\n🚀 Launching Snake Game...")
    print("📱 The game will open in your default web browser")
    print("🔗 URL: http://localhost:8501")
    print("\n🎮 Game Controls:")
    print("   - Use arrow keys or on-screen buttons to move")
    print("   - Press Start to begin")
    print("   - Press Pause/Resume to pause the game")
    print("   - Press Reset to restart")
    print("\n" + "="*50)
    
    try:
        # Run the Streamlit app
        subprocess.run([sys.executable, '-m', 'streamlit', 'run', 'streamlit_app_v2.py'])
    except KeyboardInterrupt:
        print("\n👋 Game stopped by user")
    except Exception as e:
        print(f"❌ Error launching game: {e}")

def main():
    """Main launcher function"""
    print("🐍 Snake Game Launcher")
    print("="*30)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Launch the game
    launch_game()

if __name__ == "__main__":
    main() 