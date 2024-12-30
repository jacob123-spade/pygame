import pygame 
pygame.init()

#화면 설정 
screen_width =  480
screen_height = 640 
screen = pygame.display.set_mode((screen_width,screen_height))

#캡션 설정 
pygame.display.set_caption("Nado Game")

#background 
background = pygame.image.load("/Users/john/Desktop/vscode/python/pygame_basic/white.png")

#character(스프라이트라고도 함)
character = pygame.image.load("/Users/john/Desktop/vscode/python/pygame_basic/gun_man 복사본.tiff")
character_size = character.get_rect().size #이미지의 크기를 구해옴 
character_width = character_size[0] #캐릭터의 가로 크기 
character_height = character_size[1] #캐릭터의 세로 크기 
character_x_pos = (screen_width / 2) - (character_width/2) #화면 가로의 절반크기에 해당하는 곳에 위치 
character_y_pos = screen_height - 107 


#Moving 
to_x = 0 
to_y = 0

#게임 러닝 
running = True 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 
            if event.key == pygame.K_LEFT: 
                to_x -= 5
            elif event.key == pygame.K_RIGHT: 
                to_x += 5 
            elif event.key == pygame.K_UP: 
                to_y -= 5 
            elif event.key == pygame.K_DOWN: 
                to_y += 5 
        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN: 
                to_y = 0

    character_x_pos += to_x 
    character_y_pos += to_y 

#가로 경계값 처리(The wall horizon in entry)
    if character_x_pos< 0:
        character_x_pos = 0 
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width 
    
#세로 경계값 처리(The wall horizon in entry)
    if character_y_pos < 0: 
        character_y_pos = 0 
    elif character_y_pos > screen_height- character_height: 
        character_y_pos = screen_height- character_height

    screen.blit(background,(0,0)) #배경실행 
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update() #게임 화면 다시 그리기 파이게임에서는 무조건 실행되어야 함

    #screen.fill((R,G,B)) 색을 채워주는 기능 
    
    


pygame.quit()

