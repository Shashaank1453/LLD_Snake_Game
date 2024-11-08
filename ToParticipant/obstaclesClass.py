from imports import *
from constants import *

"""
This file defines the OBSTACLE class, which manages the creation and 
rendering of obstacles on the game grid. Obstacles serve as barriers 
for the snake, adding difficulty by restricting movement. By centralizing 
obstacle logic in this file, the code remains modular, allowing obstacles 
to be easily configured or modified independently of other game mechanics.

Class: OBSTACLE
The OBSTACLE class is responsible for generating obstacles at random positions 
on the grid and rendering them on the screen.

Methods:
    1. __init__
        - Initializes an empty list of obstacle positions and calls generate_obstacles() to populate it based on the current snake position.

    2. generate_obstacles
        - Clears any existing obstacles and generates new obstacle positions at random.
        - Ensures each obstacle is placed at a location that does not overlap with the snake's body.

    3. draw_obstacles
        - Iterates over each obstacle position and draws it on the screen using the rock image at the corresponding grid position.
"""

class OBSTACLE:
    def __init__(self, snake_body):
        self.positions = []
        self.generate_obstacles(snake_body)

    def generate_obstacles(self, snake_body):

    def draw_obstacles(self):
        for pos in self.positions:
            obstacle_rect = pygame.Rect(int(pos.x * cell_size), int(pos.y * cell_size), cell_size, cell_size)
            screen.blit(rock, obstacle_rect)
