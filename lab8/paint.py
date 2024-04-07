import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))
bet = pygame.Surface((600,600))

prevx = -1
prevy = -1
currentx = -1
currenty = -1

color = (255,255,255) #doesnt matter

pen = 'pen'
rec = 'rec'
eraser = 'eraser'
circle = 'circle'

tool = 'rec'
fps = pygame.time.Clock()
def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculateCircle(x1,y1,x2,y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

mouse = False
runnning = True
while runnning:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_1]:
        tool = pen
    elif pressed[pygame.K_2]:
        tool = rec
    elif pressed[pygame.K_3]:
        tool = eraser
    elif pressed[pygame.K_4]:
        tool = circle

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                mouse = True
                currentx =  event.pos[0]
                currenty =  event.pos[1]    
                prevx =  event.pos[0]
                prevy=  event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP:
            mouse = False
            bet.blit(screen, (0, 0))

        if event.type == pygame.MOUSEMOTION:
            if mouse:
                currentx = event.pos[0]
                currenty = event.pos[1]

        if tool == rec:
            if mouse and prevx != -1 and prevy != -1 and currentx != -1 and currenty != -1:
                screen.blit(bet, (0, 0))
                r = calculateRect(prevx, prevy, currentx, currenty)
                pygame.draw.rect(screen, color,pygame.Rect(r), 3)

        if tool == pen:
            if mouse:
                pygame.draw.line(screen, color, (prevx, prevy), (currentx, currenty), 3)
            prevx = currentx
            prevy = currenty

        if tool == circle:
            if mouse:
                screen.blit(bet,(0,0))
                r = calculateRect(prevx, prevy, currentx, currenty)
                pygame.draw.circle(screen,color,(prevx,prevy), (abs(prevx-currentx)),3)

        if tool == eraser:
            if mouse:
                pygame.draw.circle(screen,(0,0,0), (currentx,currenty), 25)

        pygame.display.flip()
        fps.tick(60)