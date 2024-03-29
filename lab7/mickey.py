import pygame
import math
import datetime

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1400, 1050))

pygame.display.set_caption("Mickey Clock")

mike = pygame.image.load('imagess/mainclock.png').convert_alpha()
left = pygame.image.load('imagess/leftarm.png').convert_alpha()
right = pygame.image.load('imagess/rightarm.png').convert_alpha()

running = True
while running:
    screen.blit(mike, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    cur_time = datetime.datetime.now()
    minutes = cur_time.minute+10
    seconds = cur_time.second-3

    minute_angle = -math.radians((minutes / 60) * 360)
    second_angle = -math.radians((seconds / 60) * 360)

    minute_hand_rotated = pygame.transform.rotate(right, math.degrees(minute_angle))
    minute_hand_rect = minute_hand_rotated.get_rect(center=(700, 525))
    screen.blit(minute_hand_rotated, minute_hand_rect)

    second_hand_rotated = pygame.transform.rotate(left, math.degrees(second_angle))
    second_hand_rect = second_hand_rotated.get_rect(center=(700, 525))
    screen.blit(second_hand_rotated, second_hand_rect)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
