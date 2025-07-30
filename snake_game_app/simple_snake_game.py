import streamlit as st
import time
import random
from typing import List, Tuple, Optional
import numpy as np

class SimpleSnakeGame:
    def __init__(self, width: int = 20, height: int = 20):
        """
        Initialize the Snake game
        
        Args:
            width: Width of the game board in cells
            height: Height of the game board in cells
        """
        self.width = width
        self.height = height
        self.reset_game()
    
    def reset_game(self):
        """Reset the game to initial state"""
        # Snake starts in the middle
        self.snake = [(self.width // 2, self.height // 2)]
        self.direction = [1, 0]  # Start moving right
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False
        self.paused = False
    
    def generate_food(self) -> Tuple[int, int]:
        """Generate food at a random position"""
        while True:
            food = (random.randint(0, self.width - 1), 
                   random.randint(0, self.height - 1))
            if food not in self.snake:
                return food
    
    def update(self, new_direction: Optional[List[int]] = None):
        """Update game state for one frame"""
        if self.game_over or self.paused:
            return
        
        # Update direction if provided
        if new_direction:
            # Prevent 180-degree turns
            if (new_direction[0] != -self.direction[0] or 
                new_direction[1] != -self.direction[1]):
                self.direction = new_direction
        
        # Move snake
        new_head = (self.snake[0][0] + self.direction[0],
                   self.snake[0][1] + self.direction[1])
        
        # Check for collisions
        if (new_head[0] < 0 or new_head[0] >= self.width or
            new_head[1] < 0 or new_head[1] >= self.height or
            new_head in self.snake):
            self.game_over = True
            return
        
        # Add new head
        self.snake.insert(0, new_head)
        
        # Check if food is eaten
        if new_head == self.food:
            self.score += 10
            self.food = self.generate_food()
        else:
            # Remove tail if no food eaten
            self.snake.pop()
    
    def get_board_state(self) -> np.ndarray:
        """Get the current board state as a numpy array"""
        # Create empty board
        board = np.zeros((self.height, self.width), dtype=int)
        
        # Add snake (head = 2, body = 1)
        for i, segment in enumerate(self.snake):
            if i == 0:  # Head
                board[segment[1], segment[0]] = 2
            else:  # Body
                board[segment[1], segment[0]] = 1
        
        # Add food (3)
        board[self.food[1], self.food[0]] = 3
        
        return board
    
    def handle_key_press(self, key: str):
        """Handle key presses"""
        if key == 'r' or key == 'R':
            self.reset_game()
        elif key == 'p' or key == 'P':
            self.paused = not self.paused
        elif key == 'UP' and not self.paused:
            self.update([0, -1])
        elif key == 'DOWN' and not self.paused:
            self.update([0, 1])
        elif key == 'LEFT' and not self.paused:
            self.update([-1, 0])
        elif key == 'RIGHT' and not self.paused:
            self.update([1, 0])

def create_game_display(board: np.ndarray) -> str:
    """Create a visual representation of the game board"""
    symbols = {
        0: "⬜",  # Empty
        1: "🟦",  # Snake body
        2: "🟩",  # Snake head
        3: "🍎"   # Food
    }
    
    display = ""
    for row in board:
        for cell in row:
            display += symbols[cell]
        display += "\n"
    
    return display

# Initialize session state
if 'game' not in st.session_state:
    st.session_state.game = SimpleSnakeGame()
if 'last_update' not in st.session_state:
    st.session_state.last_update = time.time()
if 'auto_move' not in st.session_state:
    st.session_state.auto_move = False

# Page configuration
st.set_page_config(
    page_title="Snake Game",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .game-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        margin: 1rem 0;
    }
    .score-display {
        background: rgba(255,255,255,0.1);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
    }
    .game-board {
        background: rgba(255,255,255,0.05);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        font-family: monospace;
        font-size: 1.2rem;
        line-height: 1.2;
    }
    .stButton > button {
        background: linear-gradient(45deg, #ff6b6b, #ee5a24);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
</style>
""", unsafe_allow_html=True)

# Main app
def main():
    # Header
    st.markdown('<h1 class="main-header">🐍 Snake Game 🐍</h1>', unsafe_allow_html=True)
    
    # Sidebar for controls
    with st.sidebar:
        st.markdown("### 🎮 Game Controls")
        
        # Game control buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("▶️ Start Auto", key="start_auto"):
                st.session_state.auto_move = True
        with col2:
            if st.button("⏹️ Stop Auto", key="stop_auto"):
                st.session_state.auto_move = False
        
        st.button("🔄 Reset", key="reset", on_click=lambda: st.session_state.game.reset_game())
        
        # Game settings
        st.markdown("### ⚙️ Game Settings")
        speed = st.slider("Game Speed", 1, 10, 5, help="Higher number = faster game")
        
        # Pause button
        if st.button("⏸️ Pause/Resume", key="pause"):
            st.session_state.game.paused = not st.session_state.game.paused
        
        # Instructions
        st.markdown("### 📋 How to Play")
        st.markdown("""
        - Use **Direction Buttons** to control the snake
        - Eat the **🍎 food** to grow and score points
        - Avoid hitting the walls or yourself
        - Press **Pause/Resume** to pause the game
        - Press **Reset** to restart when game over
        """)
        
        # High score (simple implementation)
        if 'high_score' not in st.session_state:
            st.session_state.high_score = 0
        
        if st.session_state.game.score > st.session_state.high_score:
            st.session_state.high_score = st.session_state.game.score
        
        st.markdown("### 🏆 High Score")
        st.markdown(f"**{st.session_state.high_score}**")
    
    # Main game area
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="game-container">', unsafe_allow_html=True)
        
        # Score display
        st.markdown(f"""
        <div class="score-display">
            <h3>Current Score: {st.session_state.game.score}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Game board
        board = st.session_state.game.get_board_state()
        game_display = create_game_display(board)
        
        st.markdown("### 🎮 Game Board")
        st.markdown(f"""
        <div class="game-board">
        {game_display}
        </div>
        """, unsafe_allow_html=True)
        
        # Game status
        if st.session_state.game.game_over:
            st.error("🎯 Game Over! Press Reset to play again.")
        elif st.session_state.game.paused:
            st.warning("⏸️ Game Paused")
        elif st.session_state.auto_move:
            st.success("🎮 Auto Mode Running")
        else:
            st.info("🚀 Use direction buttons to move!")
        
        # Direction controls
        st.markdown("### 🎮 Direction Controls")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("⬅️", key="left"):
                st.session_state.game.update([-1, 0])
        
        with col2:
            col_up, col_down = st.columns(1)
            with col_up:
                if st.button("⬆️", key="up"):
                    st.session_state.game.update([0, -1])
            with col_down:
                if st.button("⬇️", key="down"):
                    st.session_state.game.update([0, 1])
        
        with col3:
            if st.button("➡️", key="right"):
                st.session_state.game.update([1, 0])
        
        # Legend
        st.markdown("### 📋 Legend")
        st.markdown("""
        - 🟩 Snake Head
        - 🟦 Snake Body  
        - 🍎 Food
        - ⬜ Empty Space
        """)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Auto move logic
    if st.session_state.auto_move and not st.session_state.game.game_over and not st.session_state.game.paused:
        current_time = time.time()
        speed_interval = 0.5 - (speed * 0.04)  # Convert speed to interval
        if current_time - st.session_state.last_update >= speed_interval:
            st.session_state.game.update()
            st.session_state.last_update = current_time
            time.sleep(0.1)  # Small delay to prevent too fast updates
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>Built with ❤️ using Python and Streamlit</p>
        <p>🐍 Enjoy playing Snake! 🐍</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 