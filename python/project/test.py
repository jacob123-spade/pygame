import pygame 
import os 
#########################################
#Basic initiation(must)
pygame.init() 

#화면 설정 
screen_width =  640
screen_height = 480 
screen = pygame.display.set_mode((screen_width,screen_height))

#캡션 설정 
pygame.display.set_caption("Nado Pang")


#background 
current_path = os.path.dirname(__file__) #현재 파일의 위치 반환 
image_path = os.path.join(current_path,"images") #images 폴더 위치 반환 

background = pygame.image.load(os.path.join(image_path,"background.jpg"))

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            break 
    





    screen.blit(background,(0,0))
    pygame.display.update()











pygame.quit()