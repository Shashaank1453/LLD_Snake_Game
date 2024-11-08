from imports import *
from Game import GAME
from constants import *


"""
This file acts as the controller for the entire game, managing the main game loop, user input, and interactions between the various game components (like the snake, fruit, and obstacles).
 It initializes the game, handles keypresses, updates the game state, and renders the game elements to the screen.

1. Main Game Loop (while True)
   - The game continuously runs in a loop, processing events, updating the game state, and rendering to the screen.

2. Event Handling
   - Quit Event: Handles quitting the game when the close window button is pressed.
   - Game Update Event: Triggers the main_game.update() method at regular intervals to update the game state.
   - Key Press Events: Detects key presses (UP, DOWN, LEFT, RIGHT) to change the snake's direction. If the game is over and the Enter key is pressed, it restarts the game.

3. Screen Management
   - Clears the screen with a grass-like background color ((175, 215, 70)) and then renders the updated game elements using main_game.draw_elements().

4. Frame Rate Control
   - Limits the game to run at 60 frames per second using clock.tick(60) to ensure consistent gameplay speed. 

This file coordinates the flow of the game, managing inputs and refreshing the screen while interacting with the core game logic defined in other classes (like GAME, SNAKE, and FRUIT).

"""

main_game = GAME()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if main_game.game_over and event.key == pygame.K_RETURN:
                main_game.restart_game()
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
                    main_game.game_active = True
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
                    main_game.game_active = True
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
                    main_game.game_active = True
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
                    main_game.game_active = True

    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)

