import streamlit as st
import time
import threading
from snake_game import SnakeGame
import streamlit.components.v1 as components

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
    .controls-info {
        background: rgba(255,255,255,0.05);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
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
    .direction-buttons {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin: 1rem 0;
    }
    .direction-btn {
        background: rgba(255,255,255,0.2);
        border: 2px solid rgba(255,255,255,0.3);
        border-radius: 10px;
        padding: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .direction-btn:hover {
        background: rgba(255,255,255,0.3);
        transform: scale(1.1);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'game' not in st.session_state:
    st.session_state.game = SnakeGame()
if 'game_running' not in st.session_state:
    st.session_state.game_running = False
if 'last_update' not in st.session_state:
    st.session_state.last_update = time.time()
if 'game_speed' not in st.session_state:
    st.session_state.game_speed = 0.15

def game_loop():
    """Game loop that runs in a separate thread"""
    while st.session_state.game_running:
        current_time = time.time()
        if current_time - st.session_state.last_update >= st.session_state.game_speed:
            st.session_state.game.update()
            st.session_state.last_update = current_time
        time.sleep(0.01)

def start_game():
    """Start the game"""
    st.session_state.game_running = True
    st.session_state.game.reset_game()
    # Start game loop in a separate thread
    game_thread = threading.Thread(target=game_loop, daemon=True)
    game_thread.start()

def stop_game():
    """Stop the game"""
    st.session_state.game_running = False

def reset_game():
    """Reset the game"""
    st.session_state.game.reset_game()

def move_up():
    """Move snake up"""
    if st.session_state.game_running and not st.session_state.game.paused:
        st.session_state.game.update([0, -1])

def move_down():
    """Move snake down"""
    if st.session_state.game_running and not st.session_state.game.paused:
        st.session_state.game.update([0, 1])

def move_left():
    """Move snake left"""
    if st.session_state.game_running and not st.session_state.game.paused:
        st.session_state.game.update([-1, 0])

def move_right():
    """Move snake right"""
    if st.session_state.game_running and not st.session_state.game.paused:
        st.session_state.game.update([1, 0])

def toggle_pause():
    """Toggle pause state"""
    st.session_state.game.paused = not st.session_state.game.paused

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
            if st.button("▶️ Start", key="start"):
                start_game()
        with col2:
            if st.button("⏹️ Stop", key="stop"):
                stop_game()
        
        st.button("🔄 Reset", key="reset", on_click=reset_game)
        
        # Game settings
        st.markdown("### ⚙️ Game Settings")
        speed = st.slider("Game Speed", 1, 10, 5, help="Higher number = faster game")
        st.session_state.game_speed = 0.2 - (speed * 0.015)  # Convert to actual speed
        
        # Pause button
        if st.button("⏸️ Pause/Resume", key="pause"):
            toggle_pause()
        
        # Instructions
        st.markdown("### 📋 How to Play")
        st.markdown("""
        - Use **Arrow Keys** or **Direction Buttons** to control the snake
        - Eat the **red food** to grow and score points
        - Avoid hitting the walls or yourself
        - Press **Pause** to pause/unpause
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
        
        # Game display
        game_placeholder = st.empty()
        
        # Game status
        if st.session_state.game.game_over:
            st.error("🎯 Game Over! Press Reset to play again.")
        elif st.session_state.game.paused:
            st.warning("⏸️ Game Paused")
        elif st.session_state.game_running:
            st.success("🎮 Game Running")
        else:
            st.info("🚀 Press Start to begin!")
        
        # Direction controls
        st.markdown("### 🎮 Direction Controls")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.button("⬅️", key="left", on_click=move_left)
        
        with col2:
            col_up, col_down = st.columns(1)
            with col_up:
                st.button("⬆️", key="up", on_click=move_up)
            with col_down:
                st.button("⬇️", key="down", on_click=move_down)
        
        with col3:
            st.button("➡️", key="right", on_click=move_right)
        
        # Controls info
        st.markdown("""
        <div class="controls-info">
            <h4>🎮 Controls:</h4>
            <p>↑ ↓ ← → Arrow Keys to move</p>
            <p>Or use the direction buttons above</p>
            <p>Pause/Resume button to pause</p>
            <p>Reset to restart</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Game rendering loop
    if st.session_state.game_running:
        # Draw the game
        st.session_state.game.draw()
        game_image = st.session_state.game.get_surface_as_image()
        
        # Display the game
        with game_placeholder.container():
            st.image(game_image, caption="Snake Game", use_column_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>Built with ❤️ using Python, Pygame, and Streamlit</p>
        <p>🐍 Enjoy playing Snake! 🐍</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 