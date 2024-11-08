# %%
    self.x = random.randint(0, cell_number - 1)
    self.y = random.randint(0, cell_number - 1)
    self.pos = Vector2(self.x, self.y)


#%%
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


#%%
    self.positions = []
    for _ in range(5):  # Adjust the number of obstacles
        while True:
            x = random.randint(0, cell_number - 1)
            y = random.randint(0, cell_number - 1)
            pos = Vector2(x, y)
            if pos not in snake_body:
                self.positions.append(pos)
                break

#%%
    if self.new_block:
        body_copy = self.body[:]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
        self.new_block = False
    else:
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

#%%
    game_over_text = "Game Over! Press Enter to Restart"
    score_text = f"Final Score: {len(self.snake.body) - 3}"
    game_over_surface = game_font.render(game_over_text, True, (255, 0, 0))
    score_surface = game_font.render(score_text, True, (0, 0, 0))
    
    game_over_rect = game_over_surface.get_rect(center=(cell_size * cell_number / 2, cell_size * cell_number / 2 - 30))
    score_rect = score_surface.get_rect(center=(cell_size * cell_number / 2, cell_size * cell_number / 2 + 10))
    
    screen.blit(game_over_surface, game_over_rect)
    screen.blit(score_surface, score_rect)


#%%
    if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
        self.end_game()

    for block in self.snake.body[1:]:
        if block == self.snake.body[0]:
            self.end_game()
    
    for pos in self.obstacles.positions:
        if pos == self.snake.body[0]:
            self.end_game()

#%%
    tail_relation = self.body[-2] - self.body[-1]
    if tail_relation == Vector2(1,0): self.tail = self.tail_left
    elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
    elif tail_relation == Vector2(0,1): self.tail = self.tail_up
    elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

#%%
    head_relation = self.body[1] - self.body[0]
    if head_relation == Vector2(1,0): self.head = self.head_left
    elif head_relation == Vector2(-1,0): self.head = self.head_right
    elif head_relation == Vector2(0,1): self.head = self.head_up
    elif head_relation == Vector2(0,-1): self.head = self.head_down


#%%
    self.draw_grass()
    self.fruit.draw_fruit()
    self.snake.draw_snake()
    self.obstacles.draw_obstacles()
    self.draw_score()
    if self.game_over:
        self.draw_game_over_screen()

#%%
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
