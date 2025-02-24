import pygame
from random import* 

pygame.init()

#Music 

bgm = pygame.mixer.Sound("/Users/hamin/Desktop/pygame/python/project/project_mario/1 HOUR Super Mario Bros Theme Song.mp3")
bgm.play()

#Screen
screen_width = 1080
screen_height = 640 
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Mario")

#background 

background = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/project_mario/mario_bg.png")
floor = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/project_mario/360_F_558845370_KSbrqdaVqLZ2VmlaIuhsRacZZ4gdnCVG.jpg")
floor_height = floor.get_rect().size[1]

#Mario 
mario = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/project_mario/main_character.png")
mario_width = mario.get_rect().size[0]
mario_height = mario.get_rect().size[1]
mario_x_pos = screen_width/2 - mario_width
mario_y_pos = screen_height - floor_height - mario_height 

#Barricades
barricade = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/project_mario/Brick_Block 복사본.tiff")
    

barricade_width = barricade.get_rect().size[0]
barricade_height = barricade.get_rect().size[1]
barricade_x_pos = screen_width/2 - barricade_width
barricade_y_pos = screen_height/2 - barricade_height
barricade_rect_left = []

#Item Box 
item_box = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/project_mario/Question_Block_NSMB 복사본.tiff")
item_box_width = item_box.get_rect().size[0]
item_box_height = item_box.get_rect().size[1]

item_box_x_pos = screen_width/2 
item_box_y_pos = screen_height/2 - item_box_height

#Moving
to_x = 0
to_y = 0
to_y_ela = 0 
char_spd_x = 5 
is_jumping = False 
jump_count = 10 

is_jumping1 = False


#FPS 
fps = pygame.time.Clock()

#Screen 
message = "You Win"
font = pygame.font.Font(None,40)
init_ticks = pygame.time.get_ticks()


#Functions 


def Moving():
    global mario_x_pos,mario_y_pos,to_x,to_y,char_spd,to_y_ela,elastic,is_jumping,jump_count,is_jumping1
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            break

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                to_x -= char_spd_x
            elif event.key == pygame.K_RIGHT: 
                to_x += char_spd_x
            elif event.key == pygame.K_SPACE:
                is_jumping = True 
            elif event.key == pygame.K_UP: 
                is_jumping1 = True 


        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                to_x = 0
                
    mario_x_pos += to_x
    
    if mario_x_pos <= 0:
        mario_x_pos = 0
    elif mario_x_pos >= screen_width - mario_width: 
        mario_x_pos = screen_width - mario_width
    if mario_y_pos <= 0:
        mario_y_pos = 0 
    elif mario_y_pos + mario_height >= screen_height - floor_height:
        mario_y_pos = screen_height - floor_height - mario_height
        

def Jumping():
    global is_jumping,jump_count,mario_y_pos,is_jumping1
    if is_jumping:  
            if jump_count >= -10:
                neg = 1 
                if jump_count < 0:
                    neg = -1 
                mario_y_pos -= (jump_count ** 2) * neg * 0.5 
                jump_count -= 1 
                pygame.time.wait(5)
            else: 
                jump_count = 10 
                is_jumping = False 

    if is_jumping1: 
            if jump_count <= -10: 
                neg1 = 1 
                if jump_count < 0: 
                    neg1 = -1

                mario_y_pos -= (jump_count **2 ) * neg1 * 2
                jump_count -= 1
                pygame.time.wait(5)
            else: 
                jump_count = 10 
                is_jumping1 = False 
        






while True: 
    
    Moving()
    Jumping()

    #Collision 

    mario_rect = mario.get_rect()
    mario_rect.left = mario_x_pos 
    mario_rect.top = mario_y_pos

    barricade_rect1 = barricade.get_rect()
    barricade_rect2 = barricade.get_rect()
    barricade_rect3 = barricade.get_rect()
    barricade_rect4 = barricade.get_rect()
    barricade_rect5 = barricade.get_rect()

    barricade_rect1.left = screen_width/2 - (barricade_width) 
    barricade_rect2.left = screen_width/2 - (barricade_width) * 2
    barricade_rect3.left = screen_width/2 - (barricade_width) * 3
    barricade_rect4.left = screen_width/2 - (barricade_width) * 4
    barricade_rect5.left = screen_width/2 - (barricade_width) * 5 


    barricade_rect1.top = barricade_y_pos
    barricade_rect2.top = barricade_y_pos
    barricade_rect3.top = barricade_y_pos
    barricade_rect4.top = barricade_y_pos
    barricade_rect5.top = barricade_y_pos

    item_rect = item_box.get_rect()
    item_rect.left = item_box_x_pos
    item_rect.top = item_box_y_pos 

    if mario_rect.colliderect(item_rect):
        mario_y_pos = item_box_y_pos + item_box_height
        
    
    if mario_rect.colliderect(barricade_rect1): 
        mario_y_pos = barricade_y_pos + barricade_height

    if mario_rect.colliderect(barricade_rect2): 
        mario_y_pos = barricade_y_pos + barricade_height
    
    if mario_rect.colliderect(barricade_rect3): 
        mario_y_pos = barricade_y_pos + barricade_height

    if mario_rect.colliderect(barricade_rect4): 
        mario_y_pos = barricade_y_pos + barricade_height

    if mario_rect.colliderect(barricade_rect5): 
        mario_y_pos = barricade_y_pos + barricade_height

    
    
    screen.blit(background,(0,0))
    screen.blit(floor,(0,screen_height - floor_height))
    for i in range(1,6):
        screen.blit(barricade,(screen_width/2 - (barricade_width) * i ,barricade_y_pos))
    screen.blit(item_box,(item_box_x_pos,item_box_y_pos))
    screen.blit(mario,(mario_x_pos,mario_y_pos))
    pygame.display.update() 






pygame.quit()