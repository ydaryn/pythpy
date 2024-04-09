import pygame
import math
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
square='square'
triangle = 'triangle'
eqtrian= 'eqtrian'
rhombus='rhombus'


tool = 'rec'
fps = pygame.time.Clock()
def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculateCircle(x1,y1,x2,y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculateSquare(x1,y1,x2,y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), min(abs(x1 - x2), abs(y1 - y2)), min(abs(x1 - x2), abs(y1 - y2)))

def calculateTriangle(x1, y1, x2):
        side_len = x2-x1                   
        h = math.pow(side_len**2 * 0.75, 0.5) 
        if side_len < 0: h *= -1
        vertex_1 = (x1, y1)
        vertex_2 = (x2, y1)
        vertex_3 = (x1 + side_len/2, y1 - h)
        vertices = [vertex_1, vertex_2, vertex_3]
        pygame.draw.polygon(screen,color, vertices, width = 3)
        
def calculateEqTriangle(x1,y1,x2,y2):
    eqPoints=[(x1, y1), (x2, y2), ((x1-(x2-x1)), y1 + abs(y1 - y2))]
    pygame.draw.polygon(screen, color,eqPoints, 3)
    
def calculateRhombus(x1,y1,x2,y2):
    len=math.pow((x2-x1)**2 + (y2-y1)**2, 0.5)
    vertex1 = (x1, y1)
    vertex2 = (x2, y2)
    vertex3=(x1-len//2,(y1+y2)//2)
    vertex4=(x2+len//2,(y1+y2)//2)
    vertices=[vertex1,vertex3,vertex2,vertex4]
    pygame.draw.polygon(screen,color, vertices, 3)
    
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
    elif pressed[pygame.K_5]:
        tool = square
    elif pressed[pygame.K_6]:
        tool = triangle
    elif pressed[pygame.K_7]:
        tool = eqtrian   
    elif pressed[pygame.K_8]:
        tool = rhombus 

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
        
        if tool == square:
            if mouse:
                screen.blit(bet, (0, 0))
                s = calculateSquare(prevx, prevy, currentx, currenty)
                pygame.draw.rect(screen, color, s, 3)
                
        if tool == triangle:
            if mouse:
                screen.blit(bet, (0, 0))
                calculateTriangle(prevx,prevy,currentx)
        
        if tool == eqtrian:
            if mouse:
                screen.blit(bet, (0, 0))
                calculateEqTriangle(prevx,prevy,currentx,currenty)
                
        if tool == rhombus:
            if mouse:
                screen.blit(bet, (0, 0))
                calculateRhombus(prevx,prevy,currentx,currenty)
        pygame.display.flip()
        fps.tick(60)
