import pygame 
pygame.init()

#화면 설정 
screen_width =  480
screen_height = 640 
screen = pygame.display.set_mode((screen_width,screen_height))

#캡션 설정 
pygame.display.set_caption("Nado Game")

#background 
background = pygame.image.load("/Users/john/Desktop/vscode/python/pygame_basic/background.png")


#게임 러닝 
running = True 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

    screen.blit(background,(0,0)) #배경실행 
    pygame.display.update() #게임 화면 다시 그리기 파이게임에서는 무조건 실행되어야 함
    #screen.fill((R,G,B)) 색을 채워주는 기능 

pygame.quit()