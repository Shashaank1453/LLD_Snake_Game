from imports import *
from constants import *
from snakeClass import SNAKE
from fruitClass import FRUIT
from obstaclesClass import OBSTACLE

"""
This file defines the GAME class, which manages the overall game logic, including the snake’s movement, fruit collection, obstacle generation, and game over conditions. 
It controls the flow of the game by updating elements, handling collisions, and rendering the game state.

Class: GAME
The GAME class is responsible for managing the state of the game, updating game elements, checking for collisions, and handling game over and restart scenarios.

Methods:
1. __init__
   - Initializes the game by creating instances of the snake, fruit, and obstacles, and setting up initial game state variables.

2. update
   - Updates the game state by moving the snake and checking for collisions if the game is active.

3. draw_elements
   - Renders the game elements: the grass, fruit, snake, obstacles, and score. Displays the game over screen if the game is over.

4. check_collision
   - Checks if the snake eats the fruit or collides with itself.
   - If the snake eats the fruit, it grows, and a new obstacle may be generated.

5. check_fail
   - Checks if the snake hits the wall, its own body, or an obstacle, in which case the game ends.

6. end_game
   - Ends the game by setting the game state to inactive and marking it as game over.

7. restart_game
   - Resets the game to its initial state, including the snake's position and obstacles.

8. draw_grass
   - Draws a grid-like background for the game, alternating grass-colored cells.

9. draw_score
   - Displays the current score (based on the snake’s length) at the top-right of the screen.

10. draw_game_over_screen
    - Displays the "Game Over" message and the final score on the screen when the game ends.
"""

class GAME:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.obstacles = OBSTACLE(self.snake.body) 
        self.fruits_eaten = 0
        self.game_active = False
        self.game_over = False

    def update(self):
        if self.game_active:
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.obstacles.draw_obstacles()
        self.draw_score()
        if self.game_over:
            self.draw_game_over_screen()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()
            self.fruits_eaten += 1
            
            if self.fruits_eaten % 5 == 0:
                self.obstacles.generate_obstacles(self.snake.body)

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.end_game()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.end_game()
        
        for pos in self.obstacles.positions:
            if pos == self.snake.body[0]:
                self.end_game()

    def end_game(self):
        self.game_active = False
        self.game_over = True

    def restart_game(self):
        self.snake.reset()
        self.fruits_eaten = 0
        self.game_active = True
        self.game_over = False
        self.obstacles = OBSTACLE(self.snake.body)

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            for col in range(cell_number):
                if (row + col) % 2 == 0:
                    grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6, apple_rect.height)

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)

    def draw_game_over_screen(self):
        game_over_text = "Game Over! Press Enter to Restart"
        score_text = f"Final Score: {len(self.snake.body) - 3}"
        game_over_surface = game_font.render(game_over_text, True, (255, 0, 0))
        score_surface = game_font.render(score_text, True, (0, 0, 0))
        
        game_over_rect = game_over_surface.get_rect(center=(cell_size * cell_number / 2, cell_size * cell_number / 2 - 30))
        score_rect = score_surface.get_rect(center=(cell_size * cell_number / 2, cell_size * cell_number / 2 + 10))
        
        screen.blit(game_over_surface, game_over_rect)
        screen.blit(score_surface, score_rect)
