import pygame
from random import*
from math import*
from time import*



pygame.init()



screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))



back = pygame.image.load("/Users/hamin/Desktop/pygame/게임배경 .jpeg")
back_width = back.get_width()
back_height = back.get_height()

dino_images = [pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Dinosaur-1.png"),
               pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Dinosaur-3.png"),
                pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Dinosaur-4.png"),] # 움직이는 그림을 구현할 때 이렇게 필요한 그림들을 리스트로 만들어 놓으면 인덱스만 가지고 놀면 돼서 편리하다 

dino_duckings = [pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Dinosaur-7.png"),
                pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Dinosaur-8.png")]

dino_jumpings = [pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Dinosaur-5.png")]

dino_enemies_fly = [pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Enemies Obstacles and Objects-0.png"),
                    pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Enemies Obstacles and Objects-1.png")]

dino_enemies_cactus = [pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Enemies Obstacles and Objects-95.png"),
                       pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Enemies Obstacles and Objects-96.png"),
                       pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Enemies Obstacles and Objects-97.png"),
                       pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Enemies Obstacles and Objects-98.png"),
                       pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Enemies Obstacles and Objects-99.png"),
                       pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Enemies Obstacles and Objects-100.png"),
                       ]

tiles = ceil(screen_width/back_width) + 1
scroll = 0

fps = pygame.time.Clock()
running = True
#Moving class

class Dinosaur:
    def __init__(self):
        self.index = 0 
        self.timer= 0
        self.images = dino_images
        self.ducking_images = dino_duckings
        self.index_ducking = 0
        self.timer_duck = 0
        self.is_ducking = False # 기본적으로 서 있는 상태에서 시작한다. 
        self.is_jumping = False
        self.jumping_img = dino_jumpings
        self.velocity = 0
        self.gravity = 0.5
        self.dino_y_pos = (screen_height - 100 - self.ducking_images[self.index_ducking].get_height())
        self.jump_power = -12 

    def running(self):
        current_image = self.images[self.index]
        screen.blit(current_image,(10,screen_height - 100 - current_image.get_height()))

        self.timer += 0.1
        if self.timer >= 0.5:
            self.timer = 0
            self.index = int((self.index+1) % len(self.images)) # 이렇게 해놓으면 인덱스 애러를 방지할 수 있다. 계속 self.index 에 +1씩 하면 인덱스 애러가 발생하므로/ 유용하니까 기억해두자 

    def ducking(self):
        ducking_image = self.ducking_images[self.index_ducking]
        screen.blit(ducking_image,(10,screen_height - 100 - ducking_image.get_height()))

        self.timer_duck += 0.1
        if self.timer_duck >= 0.5: 
            self.timer_duck = 0 
            self.index_ducking = int((self.index_ducking+1) % len(self.ducking_images))

    def jumping(self):
        jumping_img = self.jumping_img[0]
        if self.is_jumping:
            self.dino_y_pos += self.velocity 
            self.velocity += self.gravity
            

            if self.dino_y_pos >= screen_height - 100 - jumping_img.get_height(): #지면에 닿으면 초기화해야한다. 
                self.dino_y_pos = screen_height - 100 - jumping_img.get_height()
                self.is_jumping = False
                self.velocity = 0 
               
        screen.blit(jumping_img,(10,self.dino_y_pos)) #항상 공룡을 그린다.
    
    def running_division(self): # 공룡의 상태를 구분해줘야 한다. 그렇지 않으면 ducking 중에 달리는 그림이 깜빡이면서 나오는 등의 애러가 발생하게 된다. 
        if self.is_ducking: # is_ducking 이 True이면 
            self.ducking()

        elif self.is_jumping: 
            self.jumping()

        else: 
            self.running()

    def set_ducking(self,is_ducking):
        self.is_ducking = is_ducking #self.is_ducking 의 상태를 변환하는 코드

    def set_jumping(self,is_jumping):
        if is_jumping and not self.is_jumping: #is_jumping 이 True로 들어오고 동시에 점프중이 아닐때 
            self.velocity = self.jump_power
            self.is_jumping = True

class Enemies: 
    def __init__(self):
        self.is_flying = choice([True,False])

        self.flying_img = dino_enemies_fly
        self.dino = dino_images
        self.flying_xpos = screen_width - self.flying_img[0].get_height()
        self.flying_ypos = screen_height - 200 - self.dino[0].get_height()
        self.to_x1 = -5
        self.index_flying = 0
        self.flytimer = 0
    #------------------------------------------------------------#
        self.cactus_img = dino_enemies_cactus
        self.cactus_idx = randint(0,len(self.cactus_img)-1) 
        self.cactus_x_pos = screen_width - randrange(int(self.cactus_img[0].get_width()),int(screen_width/2))
        self.cactus_y_pos = screen_height - 100 - self.cactus_img[0].get_height()
        self.to_x2 = -3

    def fly(self):
        flying_img = self.flying_img[self.index_flying] 
        self.flying_xpos += self.to_x1
        screen.blit(flying_img,(self.flying_xpos,self.flying_ypos))

        self.flytimer += 0.1
        if self.flytimer >= 1: 
            self.index_flying = int((self.index_flying + 1) % len(self.flying_img))
            self.flytimer = 0 

        if self.flying_xpos <= 0:
            self.flying_xpos = screen_width - self.flying_img[0].get_height()

    def cactus(self):
        cactus_img = self.cactus_img[self.cactus_idx]
        self.cactus_x_pos += self.to_x2
        screen.blit(cactus_img,(self.cactus_x_pos,self.cactus_y_pos))
        if self.cactus_x_pos<= 0: 
            self.cactus_x_pos = screen_width - self.cactus_img[0].get_width()
            self.cactus_idx = randint(0,len(self.cactus_img)-1)

   
class Background:
    def __init__(self):
        self.surface = pygame.image.load("/Users/hamin/Desktop/pygame/게임배경 .jpeg")
      
    
    def Moving(self):
        global running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino.set_ducking(True) # self.is_ducking의 상태를 True 로 받은 다음에 반영하라
                
                elif event.key == pygame.K_UP: 
                    dino.set_jumping(True)

            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_SPACE:
                    dino.set_ducking(False) #self.is_ducking의 상태를 False로 받은 다음에 반영하라

                elif event.key == pygame.K_UP: 
                    dino.set_jumping(False)
            
            
dino = Dinosaur()
back = Background()
enemies = [Enemies() for _ in range(5)]
while running:
    fps.tick(60) #1초에 최대 60프레임으로 제한함
   
    back.Moving()
    
    for i in range(tiles):
        screen.blit(back.surface,(i * back_width + scroll,0)) # 화면을 그리는데 scroll 만큼 왼쪽으로 이동한 그림들을 그린다. 그리고 scroll을 갱신해주면 화면이 움직이는 것처럼 보인다. 

    scroll -= 5

    if abs(scroll) > back_width:
        scroll = 0
    
    pygame.draw.rect(screen,(139, 69, 19),(0,screen_height-100,800,100))

    dino.running_division() #여기에는 그냥 이 함수만 반영해 주면 알아서 ducking 과 running을 할 수 있다.
    for enemy in enemies:  
        enemy.fly()
        enemy.cactus()
    
    pygame.display.update()


pygame.quit()


#배운점 
# 1. randint(a,b)는 a 이상 b이하의 정수중 하나를 랜덤으로 불러온다.
# 2. 그림이 움직이는 것처럼 보이게 하고 싶다면 리스트에 필요한 그림들을 넣고 인덱스와 타이머를 이용해서 움직이는 효과를 낼 수 있다.
# 3. 한 캐릭터가 여러가지 동작을 할때, 이를테면 점프, 숙이기, 달리기 등을 할수 있다면 각각의 동작들이 겹치지 않게 하기 위해서 그것을 구분해야 한다. 이 때 사용할 수 있는 변수가 is_moving = False 이다.
# 4. randint()는 range()와는 달리 argument가 2개가 필요하다 range는 arg가 1개면 자동으로 0부터 시작하지만 randint()함수는 그렇지 않다. 0부터 시작하라고 정해줘야 한다.  