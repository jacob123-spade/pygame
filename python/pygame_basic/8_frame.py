import pygame 
#########################################
#Basic initiation(must)
pygame.init() 

#화면 설정 
screen_width =  480
screen_height = 640 
screen = pygame.display.set_mode((screen_width,screen_height))

#캡션 설정 
pygame.display.set_caption("Nado Game")


#background 
background = pygame.image.load("/Users/john/Desktop/vscode/python/pygame_basic/white.png")


#FPS
clock = pygame.time.Clock() #툴 자체에서 제공하는 프레임관련 함수 존재/ 버젼마다 다르지만 Clock사용시에 괄호 무조건 사용(내 버전에서는)
###########################################

# 1.User game initiation(background, game_img, coordinates, fonts, speed etc)

#character(스프라이트라고도 함)
character = pygame.image.load("/Users/john/Desktop/vscode/python/pygame_basic/gun_man .tiff")
character_size = character.get_rect().size #이미지의 크기를 구해옴 
character_width = character_size[0] #캐릭터의 가로 크기 
character_height = character_size[1] #캐릭터의 세로 크기 
character_x_pos = (screen_width / 2) - (character_width/2) #화면 가로의 절반크기에 해당하는 곳에 위치 
character_y_pos = screen_height - 107 


#enemy 
enemy = pygame.image.load("/Users/john/Desktop/vscode/python/pygame_basic/enemy .tiff")
enemy_size = enemy.get_rect().size #이미지의 크기를 구해옴 
enemy_width = enemy_size[0] #캐릭터의 가로 크기 
enemy_height = enemy_size[1] #캐릭터의 세로 크기 
enemy_x_pos = (screen_width / 2) - (enemy_width/2) #화면 가로의 절반크기에 해당하는 곳에 위치 
enemy_y_pos = (screen_height/2) - (enemy_width/2)

#Moving 
to_x = 0 
to_y = 0

#이동속도 
char_sp = 0.6

#Font 
game_font = pygame.font.Font(None,40) 

#총 시간 
total_time = 10 
 
#시작 시간 
start_ticks = pygame.time.get_ticks()

#게임 러닝 
running = True 
while running:
    dt = clock.tick(60) #게임 화면의 초당 프레임 수(FPS)를 설정 
    #캐릭터가 1초 동안에 100만큼 이동을 해야함 
    # 10 fps: 1초 동안에 10번 동작 -> 1번에 10번만큼 동작해야 100만큼 이동 
    # 20 fps: 1초 동안에 20번 동작 -> 1번에 5번 만큼 동작해야 100만큼 이동 
    
#################################################################

#2.Events Treatment
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 
            if event.key == pygame.K_LEFT: 
                to_x -= char_sp
            elif event.key == pygame.K_RIGHT: 
                to_x += char_sp
            elif event.key == pygame.K_UP: 
                to_y -= char_sp 
            elif event.key == pygame.K_DOWN: 
                to_y += char_sp 
        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN: 
                to_y = 0
##########################################
#3. Characters' position 
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt 

#가로 경계값 처리(The wall horizon in entry)
    if character_x_pos < 0:
        character_x_pos = 0 
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width 
    
#세로 경계값 처리(The wall horizon in entry)
    if character_y_pos < 0: 
        character_y_pos = 0 
    elif character_y_pos > screen_height- character_height: 
        character_y_pos = screen_height- character_height
##############################################
#4. Collision treatment 
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos 

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

#충돌 체크 
    if character_rect.colliderect(enemy_rect): 
        print("Collide") 
        running = False 
    
################################################
#5. Drawing
    screen.blit(background,(0,0)) #배경실행 
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))

    #타이머 넣기 
    #경과시간 
    elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000 #밀리세컨드(ms)여서 1000으로 나눠 초 단위로 표시 
    timer = game_font.render(str(int(total_time - elapsed_time)),True,(0,0,0))
    if total_time - elapsed_time <= 0:
        running = False 

    screen.blit(timer,(10,10))
    
    pygame.display.update() #게임 화면 다시 그리기 (파이게임에서는 무조건 실행되어야 함)

    pygame.time.delay(2000)

    #screen.fill((R,G,B)) 색을 채워주는 기능 
    
    


pygame.quit()

