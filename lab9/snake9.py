import pygame
import random

pygame.init()

bg=pygame.image.load('imgs/snakebg.png')
apple=pygame.image.load('imgs/apple.png')
WIDTH, HEIGHT = 700, 600
CELL_SIZE = 20
gridw = WIDTH // CELL_SIZE
gridh = HEIGHT // CELL_SIZE
FPS = 10

font = pygame.font.SysFont(None, 25)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
score = 0
level = 1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

RIGHT = (1, 0)
LEFT = (-1, 0)
UP = (0, -1)
DOWN = (0, 1)


class Snake:
    def __init__(self):
        self.body = [(gridw // 2, gridh // 2)]
        self.direction = RIGHT

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        tail = self.body[-1]
        new_tail = (tail[0] - self.direction[0], tail[1] - self.direction[1])
        self.body.append(new_tail)

    def change_direction(self, direction):
        if direction[0] != -self.direction[0] or direction[1] != -self.direction[1]:
            self.direction = direction

    def check_collision(self):
        head = self.body[0]
        if (
            head[0] < 3.5 or head[0] >= gridw - 3.5
            or head[1] < 3.5 or head[1] >= gridh - 3.5
        ):
            return True
        if head in self.body[1:]:
            return True
        return False

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN,(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                             


class Food:
    def __init__(self):
        self.position = self.randomize_position()

    def randomize_position(self):
        position = (
            random.randint(4, gridw - 4),
            random.randint(4, gridh - 4)
        )
        while position in snake.body:
            position = (
                random.randint(4, gridw - 4),
                random.randint(4, gridh - 4)
            )
        return position

    def draw(self, surface):
        pygame.draw.rect(surface, RED,(self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))



snake = Snake()
food = Food()
running = True

food_timer = 0 #new
while running:
    screen.blit(bg, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(UP)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(DOWN)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(RIGHT)

    snake.move()

    if snake.check_collision():
        running = False

    if snake.body[0] == food.position:
        snake.grow()
        food.position = food.randomize_position()
        food_weight=random.randint(1,5)
        score += food_weight
        score_for_lvl=score
        if score_for_lvl>10:
            level += 1
            FPS += 2
        food_timer = 0
    food_timer += 1
    if food_timer >= 70:  #7sec
        food.position = food.randomize_position()
        food_timer = 0
        
    snake.draw(screen)
    food.draw(screen)

    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 100, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
quit()
