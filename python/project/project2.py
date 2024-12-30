import pygame 
from random import*  

pygame.init()

#Screen 

screen_width = 640 
screen_height = 480 
screen = pygame.display.set_mode((screen_width,screen_height))

#Caption 
name = pygame.display.set_caption("project2")

#background 

background = pygame.image.load("/Users/john/Desktop/vscode/python/project/background.jpg")

#Stage

stage = pygame.image.load("/Users/john/Desktop/vscode/python/project/stage.tiff")
stage_amo = stage.get_rect().size
stage_height = stage_amo[1]


#FPS
fps = pygame.time.Clock()


#Character 
m_char = pygame.image.load("/Users/john/Desktop/vscode/python/project/gun_man .tiff")
m_char_size = m_char.get_rect().size 
m_char_width = m_char_size[0]
m_char_height = m_char_size[1]
m_char_xpos = screen_width/2 - m_char_width/2 
m_char_ypos = screen_height/2 - stage_height + (m_char_height * 1.26) #이거 y position 정확하게 어떻게 잡는지 확인하기 

char_sp = 0.6
to_x = 0 


while True:
    dt = fps.tick(30)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            break 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= char_sp 
            elif event.key == pygame.K_RIGHT: 
                to_x += char_sp 

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or pygame.K_RIGHT: 
                to_x = 0

    m_char_xpos += to_x * dt

    if m_char_xpos <= 0: 
        m_char_xpos = 0 
    elif m_char_xpos >= screen_width - m_char_width:
        m_char_xpos = screen_width - m_char_width



    

    
    
    
    screen.blit(background,(0,0)) 
    screen.blit(stage,(0,screen_height - stage_height))
    screen.blit(m_char,(m_char_xpos,m_char_ypos))
    pygame.display.update()


pygame.quit()
