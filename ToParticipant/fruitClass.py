from imports import *
from constants import *

"""
This file defines the FRUIT class, which handles the creation, placement, and 
display of the fruit in the snake game. The FRUIT class is responsible for generating 
fruit at random positions on the grid and rendering it on the screen. By structuring 
fruit-related logic in its own class, this file enhances modularity and keeps the main 
game loop focused on game logic and flow.

Class: FRUIT
The FRUIT class has two primary functions:

Initialize a new fruit at a random location on the grid.
Draw the fruit on the screen for players to see and interact with.



1. __init__
   - Calls self.randomize() to set an initial random position for the fruit.

2. draw_fruit
   - Creates a rectangle for the fruit based on its position and cell size.
   - Renders the fruit image (apple) at the calculated position on the screen.

3. randomize
   - Sets self.x and self.y to random coordinates within grid bounds.
   - Updates self.pos with a new Vector2 position based on these coordinates.

"""
class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)

    def randomize(self):


