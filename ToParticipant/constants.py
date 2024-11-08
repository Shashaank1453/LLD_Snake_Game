from imports import *


"""
This file defines essential game settings and assets for quick reference.

Core Elements:
- Grid & Screen: cell_size, cell_number, and screen set game dimensions.
- Assets: apple (fruit image), rock (obstacle image), game_font (score display font).
- Event: SCREEN_UPDATE triggers game updates every 150ms.

This structure keeps game parameters centralized for easy updates.
"""

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 30
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/apple.png').convert_alpha()
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)
rock = pygame.image.load('Graphics/obstacle.png').convert_alpha()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
