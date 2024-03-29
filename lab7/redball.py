import pygame
pygame.init()

width= 600
height= 600
white= (255, 255, 255) #color picker 
red  = (255, 0, 0)

rad=25
start_coord=[287, 287]
move_dist=20

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("RED Ball")
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(white)

    pygame.draw.circle(screen, red, start_coord, rad)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                start_coord[1] = max(start_coord[1] - move_dist, rad)
            elif event.key == pygame.K_DOWN:
                start_coord[1] = min(start_coord[1] + move_dist, height - rad)
            elif event.key == pygame.K_LEFT:
                start_coord[0] = max(start_coord[0] - move_dist, rad)
            elif event.key == pygame.K_RIGHT:
                start_coord[0] = min(start_coord[0] + move_dist, width - rad)

    pygame.display.flip()
    clock.tick(60)  #FPS
pygame.quit()