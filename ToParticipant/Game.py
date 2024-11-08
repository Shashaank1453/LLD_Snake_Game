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


    def check_collision(self):

    def check_fail(self):


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

    def draw_game_over_screen(self):

