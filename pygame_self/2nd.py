import pygame

image_path='/data/data/org.test.firstgame/files/app/'
clock=pygame.time.Clock()
pygame.init() 

screen=pygame.display.set_mode((758,379))  

pygame.display.set_caption("DaraGame")   

icon=pygame.image.load('images/ava.png').convert_alpha()
pygame.display.set_icon(icon)        

bg=pygame.image.load('images/Game_Background_190.png').convert_alpha()

ghost=pygame.image.load('images/ghost.png').convert_alpha()
ghost_x=760
ghost_list_in_game=[]

walk_left=[
    pygame.image.load('images/mainleft/mainleft1.png').convert_alpha(),
    pygame.image.load('images/mainleft/mainleft2.png').convert_alpha(),
    pygame.image.load('images/mainleft/mainleft3.png').convert_alpha(),
    pygame.image.load('images/mainleft/mainleft4.png').convert_alpha()
]
walk_right=[
    pygame.image.load('images/mainright/mainright1.png').convert_alpha(),
    pygame.image.load('images/mainright/mainright2.png').convert_alpha(),
    pygame.image.load('images/mainright/mainright3.png').convert_alpha(),
    pygame.image.load('images/mainright/mainright4.png').convert_alpha()
]

player_anim_count=0 #change images
bg_x=0   #slide bg coor

player_speed=10
player_x= 150   #coord
player_y=285

is_jump=False
jump_height=9

bg_sound=pygame.mixer.Sound('music/bg_mus.mp3')
bg_sound.play()

ghost_spawn=pygame.USEREVENT+1
pygame.time.set_timer(ghost_spawn,2500)

label=pygame.font.Font('fonts/MadimiOne-Regular.ttf', 50)
lose_label=label.render('You loooooose', True, (36,152,179))
restart_label=label.render('RESTART', True, (152,96,121))
restart_label_rect=restart_label.get_rect(topleft=(270,250))

bullet=pygame.image.load('images/bullet.png').convert_alpha()
bullets=[]
bullets_left=5 #ogranicheniye

gameplay=True

run=True
while run:
    
    screen.blit(bg,(bg_x,0))
    screen.blit(bg,(bg_x+758,0))
    
    if gameplay:
        player_rect=walk_left[0].get_rect(topleft=(player_x,player_y))
        
        if ghost_list_in_game:
            for (el, i) in enumerate (ghost_list_in_game):
                screen.blit(ghost, i)
                i.x-=10
                if i.x<-10:
                    ghost_list_in_game.pop(el)
                if player_rect.colliderect(i):
                    gameplay=False

        keys=pygame.key.get_pressed()
        
        if keys [pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count],(player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count],(player_x, player_y))
            
        if keys [pygame.K_LEFT] and player_x>1:
            player_x-=player_speed
        elif keys[pygame.K_RIGHT] and player_x<725:
            player_x+=player_speed
            
        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump=True
        else:
            if jump_height>=-9:
                if jump_height>0:
                    player_y-=(jump_height**2)/2
                else:
                    player_y+=(jump_height**2)/2
                jump_height-=1
            else:
                is_jump=False
                jump_height=9
        
        if player_anim_count==3:
            player_anim_count=0
        else:
            player_anim_count+=1
        
        bg_x-=5
        if bg_x<=-758:
            bg_x=0
            
         
        if bullets:
            for (i, el) in enumerate (bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x+=5
                if el.x>385:
                    bullets.pop(i)   
                
                if ghost_list_in_game:
                    for (j, ghosst) in enumerate (ghost_list_in_game):
                        if el.colliderect(ghosst):
                            ghost_list_in_game.pop(j)
                            bullets.pop() 
                    
               
    else:
        screen.fill((128,36,36))        
        screen.blit(lose_label, (227,120))
        screen.blit(restart_label, restart_label_rect)
        mouse=pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay=True
            player_x=150
            player_y=285
            jump_height=9
            is_jump=False
            ghost_list_in_game.clear()
            bullets.clear()
        
    pygame.display.update()   

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()  
        if event.type==ghost_spawn:
            ghost_list_in_game.append(ghost.get_rect(topleft=(760,275)))
        if gameplay and event.type==pygame.KEYUP and event.key==pygame.K_d :
            bullets.append(bullet.get_rect(topleft=(player_x+20, player_y+8)))
            bullets_left-=1
            
    clock.tick(30)
    
    
    