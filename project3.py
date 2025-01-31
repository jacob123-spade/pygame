import pygame 
from random import* 

pygame.init() 

#Screen
screen_width = 640 
screen_height = 480 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("project3")

#Background & stage 
background = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/neumorphic-style-blank-white-banner-with-slanting-lines-design_1017-53841.jpg 복사본.tiff")
stage = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/stage.tiff")
stage_height = stage.get_rect().size[1]

#Game Block 
block = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/block-512 .tiff")
block_width = block.get_rect().size[0]
block_height = block.get_rect().size[1]
block_x_pos = randint(0,screen_width - block_width)
block_y_pos = 0
block_spd = 5

#main character 
m_char = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/gun_man .tiff")
m_char_width = m_char.get_rect().size[0]
m_char_height = m_char.get_rect().size[1]
m_char_x_pos = screen_width/2 - m_char_width/2 
m_char_y_pos = screen_height - stage_height - m_char_height
to_x = 0 
char_spd = 0.5

#weapon 
weapon = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/bullet.png")
weapon_width = weapon.get_rect().size[0]
weapon_height = weapon.get_rect().size[1]
to_y = 0 
weapons = []
weapon_spd = 20
weapon_to_remove = -1 

# FPS
fps = pygame.time.Clock()

#Font 
game_ending = "Game Over"
font = pygame.font.Font(None, 40)
full_time = 100
start_tick = pygame.time.get_ticks()
count = 0 


#Functions

def Moving():
    global to_x,char_spd,fps,dt 
    dt = fps.tick(30)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                to_x -= char_spd 
            if event.key == pygame.K_RIGHT: 
                to_x += char_spd
            if event.key == pygame.K_SPACE:
                weapon_x_pos = m_char_x_pos + (m_char_width/2) - weapon_width/2
                weapon_y_pos = m_char_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
           
                


        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or pygame.K_RIGHT: 
                to_x = 0

def Weapons():
    global weapons
    weapons = [[w[0], w[1] - weapon_spd] for w in weapons] #w는 weapons안에서 한꺼풀 벗겨낸 것이기 때문에 리스트 안의 리스트를 의미한다. 
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]


def Drawing(): 
    screen.blit(background,(0,0))
    screen.blit(counter,(screen_width-counter_width - 5 ,0))
    screen.blit(timer,(0,0))
    screen.blit(stage,(0,screen_height - stage_height))
    for weapon_pos_x, weapon_pos_y in weapons: 
        screen.blit(weapon,(weapon_pos_x,weapon_pos_y))
    screen.blit(block,(block_x_pos,block_y_pos))
    screen.blit(m_char,(m_char_x_pos,m_char_y_pos))
    pygame.display.update()




while True: 

    Moving()

    #Main character moving 
    m_char_x_pos += to_x * dt 
    m_char_rect = m_char.get_rect()
    m_char_rect.left = m_char_x_pos
    m_char_rect.top = m_char_y_pos

    if m_char_x_pos <= 0:
        m_char_x_pos = 0 
    elif m_char_x_pos >= screen_width - m_char_width:
        m_char_x_pos = screen_width - m_char_width


    Weapons()

    for weapon_idx,weapon_val in enumerate(weapons): 
        weapon_left = weapon_val[0]
        weapon_top = weapon_val[1]

        weapon_rect = weapon.get_rect()
        weapon_rect.left = weapon_left 
        weapon_rect.top = weapon_top 

        if weapon_rect.colliderect(block_rect): 
            count += 1
            weapon_to_remove = 0
            block_x_pos = randint(0,screen_width - block_width)
            block_y_pos = 0
            if count >= 10: 
                block_spd = 10
    
    #Blocks moving 
    block_y_pos += block_spd  
    if block_y_pos >= screen_height - stage_height: 
        block_y_pos = 0 
        block_x_pos = randint(0,screen_width - block_width)

    block_rect = block.get_rect()
    block_rect.left = block_x_pos 
    block_rect.top = block_y_pos
    
    if m_char_rect.colliderect(block_rect): 
        break

    #Collision 
    if weapon_to_remove == 0: 
        del weapons[weapon_to_remove]
        weapon_to_remove = -1
    if count == 15: 
        game_ending = "You Win"
        break 

    
    loading_time = int(pygame.time.get_ticks() - start_tick) / 1000
    timer = font.render(f"Timer: {int(full_time - loading_time)}",True,(0,0,255))
    if full_time - loading_time <= 0:
        game_ending = "Time Over"
        break 
    counter = font.render("Count: {0}".format(count), True, (0,0,0))
    counter_width = counter.get_rect().size[0]

    Drawing()
    
    


msg = font.render(game_ending,True,(0,0,255))
msg_rect = msg.get_rect(center = (screen_width/2,screen_height/2))
screen.blit(msg,msg_rect)
pygame.display.update()
pygame.time.wait(1000)

pygame.quit()



#Questions
#1. 왜 총알을 이중리스트를 쓰는가? 한줄 포문의 의미는 무엇인가?
#2. 타이머 정의에서 쓰이는 함수 get_ticks()는 무엇인가? 