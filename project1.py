import pygame
from random import*  
pygame.init()

#background 
screen_height = 640 
screen_width = 480 
screen = pygame.display.set_mode((screen_width,screen_height))

#back_picture -> 배경 그림을 넣지 않으면 객체가 업로드 되는 게 가려지지 않는다. 즉 배경화면 뒤에서는 계속 스프라이트를 업로드 중이며 배경화면이 있을 때 움직인 결과가 찍히게 된다. 

back_picture = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/background1.jpg")

#caption 
caption = pygame.display.set_caption("Project")

#Main character 
m_char = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/man .tiff")
m_char_size = m_char.get_rect().size
m_char_width = m_char_size[0]
m_char_height = m_char_size[1] 
m_char_x_pos = (screen_width/2) - (m_char_width/2)
m_char_y_pos = screen_height - m_char_height

#moving of Main character 
to_x = 0 
Moving = 0.6

#FPS 
fps = pygame.time.Clock()


#barricade 
barricade = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/rock.png")
bar_size = barricade.get_rect().size 
bar_width = bar_size[0]
bar_height = bar_size[1]
bar_x_pos = randint(0,screen_width - bar_width)
bar_y_pos = 0

#Fonts 
game_font = pygame.font.Font(None,200) 

#running 
while True: 
    dt = fps.tick(30)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            break #변수를 bool값으로 설정했으면 변수를 반대 bool로 만드는 것으로 루프를 나갈 수 있으나 변수를 설정하지 않았다면 break를 이용해서 루프를 나가야 한다. 

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT: 
                to_x += Moving
            elif event.key == pygame.K_LEFT: 
                to_x -= Moving
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or pygame.K_LEFT: 
                to_x = 0
    
    bar_y_pos += 10
    m_char_x_pos += to_x * dt

# Wall colliding 
    if m_char_x_pos <= 0: 
        m_char_x_pos = 0 
    elif m_char_x_pos >= screen_width - m_char_width: 
        m_char_x_pos = screen_width - m_char_width

    if bar_y_pos > screen_height: 
        bar_y_pos = 0 
        bar_x_pos = randint(0,screen_width - bar_width)

# Colliding with each other 

    m_char_rect = m_char.get_rect()
    m_char_rect.left = m_char_x_pos 
    m_char_rect.top = m_char_y_pos

    bar_rect = barricade.get_rect()
    bar_rect.left = bar_x_pos
    bar_rect.top = bar_y_pos 

    if m_char_rect.colliderect(bar_rect):
        break 

    screen.blit(back_picture,(0,0))
    screen.blit(m_char,(m_char_x_pos,m_char_y_pos))
    screen.blit(barricade,(bar_x_pos,bar_y_pos))
    
    pygame.display.update()


pygame.quit() 




