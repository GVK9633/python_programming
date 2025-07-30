#!/usr/bin/env python3
"""
Simple Snake Game Launcher
A launcher for the simplified Snake game without Pygame.
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
    required_packages = ['streamlit', 'numpy']
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
            print("❌ Failed to install packages. Please run: pip install -r requirements_simple.txt")
            return False
    
    return True

def launch_game():
    """Launch the Snake game"""
    print("\n🚀 Launching Simple Snake Game...")
    print("📱 The game will open in your default web browser")
    print("🔗 URL: http://localhost:8501")
    print("\n🎮 Game Controls:")
    print("   - Use direction buttons to move the snake")
    print("   - Press Start Auto for automatic movement")
    print("   - Press Pause/Resume to pause the game")
    print("   - Press Reset to restart")
    print("\n" + "="*50)
    
    try:
        # Run the Streamlit app
        subprocess.run([sys.executable, '-m', 'streamlit', 'run', 'simple_snake_game.py'])
    except KeyboardInterrupt:
        print("\n👋 Game stopped by user")
    except Exception as e:
        print(f"❌ Error launching game: {e}")

def main():
    """Main launcher function"""
    print("🐍 Simple Snake Game Launcher")
    print("="*35)
    
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