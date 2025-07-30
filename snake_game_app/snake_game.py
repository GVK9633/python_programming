import pygame
import random
import numpy as np
from typing import List, Tuple, Optional
import io
from PIL import Image

class SnakeGame:
    def __init__(self, width: int = 400, height: int = 400, cell_size: int = 20):
        """
        Initialize the Snake game
        
        Args:
            width: Width of the game board
            height: Height of the game board
            cell_size: Size of each cell in pixels
        """
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid_width = width // cell_size
        self.grid_height = height // cell_size
        
        # Initialize Pygame
        pygame.init()
        self.screen = pygame.Surface((width, height))
        self.clock = pygame.time.Clock()
        
        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.GRAY = (128, 128, 128)
        
        # Game state
        self.reset_game()
    
    def reset_game(self):
        """Reset the game to initial state"""
        # Snake starts in the middle
        self.snake = [(self.grid_width // 2, self.grid_height // 2)]
        self.direction = [1, 0]  # Start moving right
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False
        self.paused = False
    
    def generate_food(self) -> Tuple[int, int]:
        """Generate food at a random position"""
        while True:
            food = (random.randint(0, self.grid_width - 1), 
                   random.randint(0, self.grid_height - 1))
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
        if (new_head[0] < 0 or new_head[0] >= self.grid_width or
            new_head[1] < 0 or new_head[1] >= self.grid_height or
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
    
    def draw(self):
        """Draw the current game state"""
        # Clear screen
        self.screen.fill(self.BLACK)
        
        # Draw grid
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, self.GRAY, (x, 0), (x, self.height), 1)
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, self.GRAY, (0, y), (self.width, y), 1)
        
        # Draw snake
        for i, segment in enumerate(self.snake):
            color = self.GREEN if i == 0 else self.BLUE  # Head is green, body is blue
            rect = pygame.Rect(segment[0] * self.cell_size + 1,
                             segment[1] * self.cell_size + 1,
                             self.cell_size - 2,
                             self.cell_size - 2)
            pygame.draw.rect(self.screen, color, rect)
        
        # Draw food
        food_rect = pygame.Rect(self.food[0] * self.cell_size + 1,
                               self.food[1] * self.cell_size + 1,
                               self.cell_size - 2,
                               self.cell_size - 2)
        pygame.draw.rect(self.screen, self.RED, food_rect)
        
        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {self.score}', True, self.WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw game over message
        if self.game_over:
            font = pygame.font.Font(None, 48)
            game_over_text = font.render('GAME OVER!', True, self.RED)
            text_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(game_over_text, text_rect)
            
            font = pygame.font.Font(None, 24)
            restart_text = font.render('Press R to restart', True, self.WHITE)
            restart_rect = restart_text.get_rect(center=(self.width // 2, self.height // 2 + 40))
            self.screen.blit(restart_text, restart_rect)
        
        # Draw pause message
        if self.paused and not self.game_over:
            font = pygame.font.Font(None, 36)
            pause_text = font.render('PAUSED', True, self.WHITE)
            text_rect = pause_text.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(pause_text, text_rect)
    
    def get_surface_as_image(self) -> Image.Image:
        """Convert the Pygame surface to a PIL Image for Streamlit"""
        # Get the surface data
        view = pygame.surfarray.array3d(self.screen)
        # Convert from (width, height, channel) to (height, width, channel)
        view = view.transpose([1, 0, 2])
        # Convert to PIL Image
        return Image.fromarray(view)
    
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
    
    def quit(self):
        """Clean up Pygame"""
        pygame.quit() 