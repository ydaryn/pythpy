import pygame 
import random

pygame.init()

width = 635
height = 650
screen = pygame.display.set_mode((width, height))
bg = pygame.image.load('imgs/bg_highway.png').convert_alpha()
myCar = pygame.image.load('imgs/myCar.png').convert_alpha()
myCar = pygame.transform.scale(myCar, (100, 200))
enemyCar = pygame.image.load('imgs/enemyCar.png').convert_alpha()
enemyCar = pygame.transform.scale(enemyCar, (100, 200))
coin = pygame.image.load('imgs/star.png').convert_alpha()
FPS = pygame.time.Clock()
pygame.display.set_caption("Race")   
font = pygame.font.SysFont("Verdana", 60)
accident_sound=pygame.mixer.Sound('imgs/caracc.mp3')

my_x = 300
my_y = 450
speed = 5
my_speed=9
enemy_cars = []
coins=[]
coin_x = random.randint(0, width - coin.get_width())
coin_y = -50
coin_collected = False
enemy_count = 0
coin_count = 0

enemy_spawn = pygame.USEREVENT + 1
coin_spawn=pygame.USEREVENT+1
pygame.time.set_timer(enemy_spawn, 2000)
pygame.time.set_timer(coin_spawn, 1000)

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE=(15, 81, 186)

lose_font = pygame.font.SysFont("Verdana", 100)
lose_label = lose_font.render("You Lose!", True, GREEN)

enemy_speed_inc = 0

game_over = False
running = True
while running:
    screen.blit(bg, (0, 0))
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        if event.type == coin_spawn:
            coin_x = random.randint(0, width - coin.get_width())
            coins.append(pygame.Rect(coin_x, -50, coin.get_width(), coin.get_height()))
        if event.type == enemy_spawn:
            random_enemy = random.randint(100, 600)
            enemy_cars.append(pygame.Rect(random_enemy, -50, enemyCar.get_width(), enemyCar.get_height()))
            enemy_count += 1 
            
            
    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            my_x -= my_speed
        if keys[pygame.K_RIGHT]:
            my_x += my_speed
        if keys[pygame.K_DOWN]:
            my_y += my_speed
        if keys[pygame.K_UP]:
            my_y -= my_speed

        if my_x < 0:
            my_x = 0
        elif my_x > width - myCar.get_width():
            my_x = width - myCar.get_width()
        if my_y < 0:
            my_y = 0
        elif my_y > height - myCar.get_height():
            my_y = height - myCar.get_height()

        for enemy in enemy_cars:
            enemy.y =enemy.y+speed+enemy_speed_inc
            screen.blit(enemyCar, (enemy.x, enemy.y))

            if enemy.colliderect(pygame.Rect(my_x, my_y, myCar.get_width(), myCar.get_height())):
                game_over = True
                accident_sound.play()

            if enemy.y > height:
                enemy_cars.remove(enemy)

        screen.blit(coin, (coin_x, coin_y))
        coin_y += 5
        for coin_rect in coins:
            coin_rect.y += 5
            screen.blit(coin, (coin_rect.x, coin_rect.y))
            if coin_rect.colliderect(pygame.Rect(my_x, my_y, myCar.get_width(), myCar.get_height())):
                coins.remove(coin_rect)
                coins_dif_w=random.randint(1, 5)
                coin_count += coins_dif_w
                coin_count_fs=coin_count
                if coin_count > 10:
                    enemy_speed_inc += 1
                    coin_count_fs

        if len(coins) == 0:
            coin_x = random.randint(0, width - coin.get_width())
            coins.append(pygame.Rect(coin_x, -50, coin.get_width(), coin.get_height()))


        screen.blit(myCar, (my_x, my_y))

        coin_text = font.render(f"Coins: {coin_count}", True, BLUE)
        screen.blit(coin_text, (10, 0))
        enemy_text = font.render(f"Enemies: {enemy_count}", True, BLUE)
        screen.blit(enemy_text, (10, 45))
    else:
        screen.fill(RED)
        screen.blit(lose_label, (width // 2 - lose_label.get_width() // 2, height // 2 - lose_label.get_height() // 2))
    
    pygame.display.flip()
    FPS.tick(60)
    
pygame.quit()    
