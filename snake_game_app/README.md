# 🐍 Snake Game with Streamlit

A classic Snake game built with Python, Pygame, and Streamlit. Play the game directly in your web browser with a beautiful, modern interface!

## 🎮 Features

- **Classic Snake Gameplay**: Control a snake to eat food and grow longer
- **Beautiful UI**: Modern, responsive design with gradient backgrounds
- **Interactive Controls**: Use arrow keys or on-screen buttons
- **Game Settings**: Adjustable game speed
- **Score Tracking**: Current score and high score tracking
- **Pause/Resume**: Pause the game at any time
- **Game Over Handling**: Automatic game over detection and restart functionality

## 🚀 Quick Start

### Prerequisites

Make sure you have Python 3.7+ installed on your system.

### Installation

1. **Clone or download the project files**
2. **Navigate to the snake_game_app directory**:
   ```bash
   cd snake_game_app
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run streamlit_app_v2.py
   ```

5. **Open your browser** and go to the URL shown in the terminal (usually `http://localhost:8501`)

## 🎯 How to Play

### Controls
- **Arrow Keys**: Move the snake in four directions
- **Direction Buttons**: Click the on-screen arrow buttons
- **Start Button**: Begin a new game
- **Stop Button**: Stop the current game
- **Reset Button**: Reset the game to initial state
- **Pause/Resume Button**: Pause or resume the game

### Game Rules
1. **Objective**: Eat the red food to grow your snake and increase your score
2. **Movement**: Use arrow keys or direction buttons to control the snake
3. **Growth**: Each food eaten adds 10 points and makes the snake longer
4. **Collision**: Avoid hitting the walls or your own body
5. **Game Over**: The game ends when you collide with walls or yourself
6. **Restart**: Press the Reset button to start a new game

## 📁 Project Structure

```
snake_game_app/
├── snake_game.py          # Core game logic using Pygame
├── streamlit_app.py       # Basic Streamlit interface
├── streamlit_app_v2.py    # Improved Streamlit interface (recommended)
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🛠️ Technical Details

### Core Components

1. **SnakeGame Class** (`snake_game.py`):
   - Handles all game logic
   - Manages snake movement, food generation, collision detection
   - Renders the game using Pygame
   - Converts Pygame surface to PIL Image for Streamlit display

2. **Streamlit Interface** (`streamlit_app_v2.py`):
   - Beautiful, responsive web interface
   - Real-time game rendering
   - Interactive controls and settings
   - Session state management for game persistence

### Key Features

- **Threading**: Game loop runs in a separate thread for smooth performance
- **Session State**: Game state persists across Streamlit reruns
- **Responsive Design**: Works on different screen sizes
- **Custom Styling**: Modern CSS for enhanced visual appeal
- **Error Handling**: Graceful handling of game states and user interactions

## 🎨 Customization

### Changing Game Speed
Adjust the speed slider in the sidebar to make the game faster or slower.

### Modifying Colors
Edit the color constants in `snake_game.py`:
```python
self.BLACK = (0, 0, 0)      # Background
self.WHITE = (255, 255, 255) # Text
self.GREEN = (0, 255, 0)     # Snake head
self.RED = (255, 0, 0)       # Food
self.BLUE = (0, 0, 255)      # Snake body
```

### Changing Game Board Size
Modify the initialization parameters in `snake_game.py`:
```python
game = SnakeGame(width=500, height=500, cell_size=25)
```

## 🐛 Troubleshooting

### Common Issues

1. **Pygame not found**: Make sure you've installed all requirements
   ```bash
   pip install -r requirements.txt
   ```

2. **Display issues**: Try running with a different Streamlit theme
   ```bash
   streamlit run streamlit_app_v2.py --theme.base="light"
   ```

3. **Performance issues**: Reduce the game board size or increase the update interval

### System Requirements

- **OS**: Windows, macOS, or Linux
- **Python**: 3.7 or higher
- **Memory**: At least 512MB RAM
- **Browser**: Modern web browser (Chrome, Firefox, Safari, Edge)

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding new features
- Improving the UI/UX
- Fixing bugs
- Adding sound effects
- Creating different game modes

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for the web interface
- Game logic powered by [Pygame](https://www.pygame.org/)
- Image processing with [Pillow](https://python-pillow.org/)
- Numerical operations with [NumPy](https://numpy.org/)

---

**Enjoy playing Snake! 🐍🎮** 