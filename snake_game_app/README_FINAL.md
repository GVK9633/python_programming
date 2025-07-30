# 🐍 Snake Game with Streamlit

A classic Snake game built with Python and Streamlit. Play the game directly in your web browser with a beautiful, modern interface!

## 🎮 Features

- **Classic Snake Gameplay**: Control a snake to eat food and grow longer
- **Beautiful UI**: Modern, responsive design with gradient backgrounds
- **Interactive Controls**: Use on-screen buttons to control the snake
- **Game Settings**: Adjustable game speed
- **Score Tracking**: Current score and high score tracking
- **Pause/Resume**: Pause the game at any time
- **Auto Mode**: Let the snake move automatically
- **Game Over Handling**: Automatic game over detection and restart functionality

## 🚀 Quick Start

### Prerequisites

Make sure you have Python 3.7+ installed on your system.

### Installation & Running

#### Option 1: Simple Version (Recommended)
The simple version uses emojis and works reliably across all platforms:

```bash
cd snake_game_app
python run_simple_game.py
```

#### Option 2: Pygame Version (Advanced)
The Pygame version has better graphics but may have compatibility issues on some systems:

```bash
cd snake_game_app
python run_game.py
```

#### Option 3: Manual Installation
```bash
cd snake_game_app
pip install -r requirements_simple.txt  # For simple version
# OR
pip install -r requirements.txt         # For Pygame version

# Then run:
streamlit run simple_snake_game.py      # Simple version
# OR
streamlit run streamlit_app_v2.py       # Pygame version
```

## 🎯 How to Play

### Controls
- **Direction Buttons**: Click the arrow buttons to move the snake
- **Start Auto Button**: Begin automatic movement
- **Stop Auto Button**: Stop automatic movement
- **Reset Button**: Reset the game to initial state
- **Pause/Resume Button**: Pause or resume the game

### Game Rules
1. **Objective**: Eat the 🍎 food to grow your snake and increase your score
2. **Movement**: Use direction buttons to control the snake
3. **Growth**: Each food eaten adds 10 points and makes the snake longer
4. **Collision**: Avoid hitting the walls or your own body
5. **Game Over**: The game ends when you collide with walls or yourself
6. **Restart**: Press the Reset button to start a new game

## 📁 Project Structure

```
snake_game_app/
├── simple_snake_game.py     # Simple version (emoji-based, recommended)
├── snake_game.py            # Core game logic using Pygame
├── streamlit_app.py         # Basic Streamlit interface
├── streamlit_app_v2.py      # Improved Streamlit interface with Pygame
├── run_simple_game.py       # Launcher for simple version
├── run_game.py              # Launcher for Pygame version
├── requirements_simple.txt  # Dependencies for simple version
├── requirements.txt         # Dependencies for Pygame version
└── README_FINAL.md         # This file
```

## 🛠️ Technical Details

### Simple Version (`simple_snake_game.py`)
- **No external dependencies** beyond Streamlit and NumPy
- **Emoji-based graphics** for universal compatibility
- **Works on all platforms** including macOS, Windows, and Linux
- **No threading issues** - fully compatible with Streamlit
- **Fast and responsive** gameplay

### Pygame Version (`streamlit_app_v2.py`)
- **Better graphics** with Pygame rendering
- **More complex setup** with additional dependencies
- **May have compatibility issues** on some macOS systems
- **Requires proper threading** for smooth gameplay

### Key Features

- **Session State**: Game state persists across Streamlit reruns
- **Responsive Design**: Works on different screen sizes
- **Custom Styling**: Modern CSS for enhanced visual appeal
- **Error Handling**: Graceful handling of game states and user interactions
- **Auto Mode**: Automatic snake movement for demonstration

## 🎨 Customization

### Changing Game Speed
Adjust the speed slider in the sidebar to make the game faster or slower.

### Modifying Game Board Size
Edit the initialization parameters in the game files:
```python
# In simple_snake_game.py
game = SimpleSnakeGame(width=25, height=25)

# In snake_game.py
game = SnakeGame(width=500, height=500, cell_size=25)
```

### Changing Symbols (Simple Version)
Edit the symbols dictionary in `simple_snake_game.py`:
```python
symbols = {
    0: "⬜",  # Empty
    1: "🟦",  # Snake body
    2: "🟩",  # Snake head
    3: "🍎"   # Food
}
```

## 🐛 Troubleshooting

### Common Issues

1. **Import errors**: Make sure you've installed all requirements
   ```bash
   pip install -r requirements_simple.txt  # For simple version
   ```

2. **Pygame errors on macOS**: Use the simple version instead
   ```bash
   python run_simple_game.py
   ```

3. **Display issues**: Try running with a different Streamlit theme
   ```bash
   streamlit run simple_snake_game.py --theme.base="light"
   ```

4. **Performance issues**: Reduce the game board size or increase the update interval

### System Requirements

- **OS**: Windows, macOS, or Linux
- **Python**: 3.7 or higher
- **Memory**: At least 512MB RAM
- **Browser**: Modern web browser (Chrome, Firefox, Safari, Edge)

## 🎮 Game Modes

### Manual Mode
- Use direction buttons to control the snake manually
- Perfect for learning and precise control
- Good for beginners

### Auto Mode
- Snake moves automatically in the current direction
- Use direction buttons to change direction
- Great for demonstration and testing

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding new features
- Improving the UI/UX
- Fixing bugs
- Adding sound effects
- Creating different game modes
- Improving performance

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for the web interface
- Game logic powered by Python
- Numerical operations with [NumPy](https://numpy.org/)
- Graphics with [Pygame](https://www.pygame.org/) (advanced version)

---

## 🚀 Ready to Play?

Choose your preferred version and start playing!

**For most users**: `python run_simple_game.py` ✅
**For advanced users**: `python run_game.py` 🎮

**Enjoy playing Snake! 🐍🎮** 