import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
purple = (138, 43, 226)

# Display size
dis_width = 600
dis_height = 400

# Game speed and snake size
snake_block = 10
initial_snake_speed = 15

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Screen
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Snake Class
class Snake:
    def __init__(self):
        self.body = [[dis_width / 2, dis_height / 2]]
        self.length = 1
        self.x_change = 0
        self.y_change = 0

    def move(self, direction):
        if direction == "LEFT" and self.x_change != snake_block:
            self.x_change = -snake_block
            self.y_change = 0
        if direction == "RIGHT" and self.x_change != -snake_block:
            self.x_change = snake_block
            self.y_change = 0
        if direction == "UP" and self.y_change != snake_block:
            self.y_change = -snake_block
            self.x_change = 0
        if direction == "DOWN" and self.y_change != -snake_block:
            self.y_change = snake_block
            self.x_change = 0

    def update(self):
        x1 = self.body[0][0] + self.x_change
        y1 = self.body[0][1] + self.y_change
        new_head = [x1, y1]
        self.body.insert(0, new_head)

        if len(self.body) > self.length:
            self.body.pop()

    def draw(self):
        for block in self.body:
            pygame.draw.rect(dis, black, [block[0], block[1], snake_block, snake_block])

    def check_collision(self):
        head = self.body[0]
        # Check if snake hits itself
        for block in self.body[1:]:
            if block == head:
                return True
        # Check if snake hits the wall
        if head[0] >= dis_width or head[0] < 0 or head[1] >= dis_height or head[1] < 0:
            return True
        return False

# Food Class
class Food:
    def __init__(self):
        self.respawn()

    def draw(self):
        pygame.draw.rect(dis, green, [self.x, self.y, snake_block, snake_block])

    def respawn(self):
        self.x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

# Obstacle Class
class Obstacle:
    def __init__(self):
        self.x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    def draw(self):
        pygame.draw.rect(dis, purple, [self.x, self.y, snake_block, snake_block])

# Game Class
class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.obstacles = [Obstacle() for _ in range(3)]  # Add 3 obstacles
        self.game_over = False
        self.game_close = False
        self.snake_speed = initial_snake_speed

    def show_score(self):
        value = score_font.render("Your Score: " + str(self.snake.length - 1), True, yellow)
        dis.blit(value, [0, 0])

    def show_message(self, msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])

    def check_obstacle_collision(self):
        for obs in self.obstacles:
            if [obs.x, obs.y] == self.snake.body[0]:
                return True
        return False

    def game_loop(self):
        while not self.game_over:

            while self.game_close:
                dis.fill(blue)
                self.show_message("You Lost! Press Q-Quit or C-Play Again", red)
                self.show_score()
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.game_over = True
                            self.game_close = False
                        if event.key == pygame.K_c:
                            self.__init__()  # Reset game
                            self.game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake.move("LEFT")
                    elif event.key == pygame.K_RIGHT:
                        self.snake.move("RIGHT")
                    elif event.key == pygame.K_UP:
                        self.snake.move("UP")
                    elif event.key == pygame.K_DOWN:
                        self.snake.move("DOWN")

            self.snake.update()

            # Check collisions
            if self.snake.check_collision() or self.check_obstacle_collision():
                self.game_close = True

            if self.snake.body[0] == [self.food.x, self.food.y]:
                self.food.respawn()
                self.snake.length += 1
                if self.snake.length % 5 == 0:  # Add more obstacles after every 5 foods
                    self.obstacles.append(Obstacle())
                self.snake_speed += 1  # Increase speed after every food eaten

            dis.fill(blue)
            self.food.draw()
            for obs in self.obstacles:
                obs.draw()
            self.snake.draw()
            self.show_score()

            pygame.display.update()
            clock.tick(self.snake_speed)

        pygame.quit()
        quit()

# Start the game
if __name__ == "__main__":
    game = Game()
    game.game_loop()
