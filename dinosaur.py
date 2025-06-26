import pygame
import random

pygame.init()

#Screen 
screen_width = 640
screen_height = 320
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Dino")


#Background
white = (255,255,255) #하얀색 배경을 만들 것이다. 원래는 움직이는 화면을 만들려고 했으나 sprite찾기가 너무 힘들어서 관둔다.

#FPS
clock = pygame.time.Clock()
FPS = 60

#Dinosaur running,jumping, ducking 
dino_running = [pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Dinosaur-3.png"),
                pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Dinosaur-4.png")]

dino_jumping = [pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Dinosaur-1.png"),
                pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Dinosaur-2.png")]

dino_ducking = [pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Dinosaur-7.png"),
                pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Dinosaur-8.png")]


#Pteranodon(Enemy)
ptera = [pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Enemies Obstacles and Objects-0.png"),
         pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Enemies Obstacles and Objects-1.png")]



cactus = [pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Enemies Obstacles and Objects-101.png"),
          pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Enemies Obstacles and Objects-102.png"),
          pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Enemies Obstacles and Objects-103.png"),
          pygame.image.load("/Users/hamin/Desktop/pygame/Sprites/Browser Games - Google Dinosaur Run Game - Enemies Obstacles and Objects-104.png")
          ]

#cloud 

cloud1 = pygame.image.load("/Users/hamin/Desktop/pygame/cloud_pixel  복사본.tiff")
cloud2 = pygame.image.load("/Users/hamin/Desktop/pygame/cloud_pixel  복사본.tiff")
cloud3= pygame.image.load("/Users/hamin/Desktop/pygame/cloud_pixel  복사본.tiff")


#font, timer 
font = pygame.font.Font(None,40)
start_tick = pygame.time.get_ticks()
game_ending_mg = "GAME OVER"
score = 0

#------------------------------------------------------------------
#Class of Game
class Dino: 
    def __init__(self): 
        self.dino_running = dino_running
        self.dino_running_idx = 0
        self.dino_width = self.dino_running[0].get_width()
        self.dino_height = self.dino_running[0].get_height()
        self.dino_y_pos = screen_height - self.dino_height
        self.timer_running = 0
        #--------------------------- 
        self.timer_jumping = 0
        self.dino_jumping = dino_jumping
        self.velocity = -17
        self.jump = 0.8 #위로 올라갔다가 내려오는 속도를 조절하기 위해서는 중력과 탄력성을 조절하면 된다. 여기서는 중력의 크기를 줄임으로써 점프 속도를 느리게 했다. 
        self.isjumping = False
        self.dino_jumping_idx = 0 
        #---------------------------
        self.timer_ducking = 0
        self.dino_ducking = dino_ducking 
        self.dino_ducking_idx = 0
        self.isducking = False 
        

    def running(self):
        screen.blit(self.dino_running[self.dino_running_idx],(10,self.dino_y_pos))

        self.timer_running += 1 
        if self.timer_running >= 5: 
            self.dino_running_idx = (self.dino_running_idx + 1) % len(self.dino_running)
            self.timer_running = 0

    def jumping(self): 
        if self.isjumping:
            screen.blit(self.dino_jumping[self.dino_jumping_idx],(10,self.dino_y_pos))
            self.dino_y_pos += self.velocity
            self.velocity += self.jump

            self.timer_jumping += 1 
            if self.timer_jumping >= 10: 
                self.dino_jumping_idx = (self.dino_jumping_idx + 1) % len(self.dino_jumping)
                self.timer_jumping = 0 


            if self.dino_y_pos >= screen_height - self.dino_height: 
                self.dino_y_pos = screen_height - self.dino_height
                self.isjumping = False #착지한 뒤에는 점프 여부를 False로 만들어줘야 공중에 떠 있지 않고 정상 작동 한다.
                self.velocity = -17 #이걸 초기화 해주지 않으면 한번 점프하고 난 다음에는 velocity가 너무 커져서 위로 올라가지를 못한다.  

    def ducking(self): 
        if self.isducking: 
            screen.blit(self.dino_ducking[self.dino_ducking_idx],(10,screen_height - self.dino_ducking[0].get_height()))

            self.timer_ducking += 1 
            if self.timer_ducking >= 5: 
                self.dino_ducking_idx = (self.dino_ducking_idx + 1) % len(self.dino_ducking)
                self.timer_ducking = 0

    def discaction(self): 
        if self.isjumping: 
            self.jumping()

        elif self.isducking: 
            self.ducking()

        else: 
            self.running()


class Ptera: 
    def __init__(self): 
        self.ptera = ptera
        self.ptera_idx = 0 
        self.ptera_width = self.ptera[0].get_width()
        self.ptera_height = self.ptera[0].get_height()
        self.ptera_x_pos = screen_width - self.ptera_width
        self.ptera_y_pos = 250 #정확한 좌표는 내가 계산함 
        self.timer_ptera = 0 
        self.to_x = -5 
        self.isptera = False

    def ptera_fly(self): 
        if self.isptera:
            screen.blit(self.ptera[self.ptera_idx],(self.ptera_x_pos,self.ptera_y_pos))


            self.ptera_x_pos += self.to_x
            if self.ptera_x_pos <= 0: 
                self.ptera_x_pos = screen_width - self.ptera_width
                self.isptera = False 
                

            self.timer_ptera += 1 
            if self.timer_ptera >= 15: #self.timer_ptera의 시간을 늘리면 이미지 변환 속도가 느려진다. 
                self.ptera_idx = (self.ptera_idx + 1) % len(self.ptera)
                self.timer_ptera = 0 

class Cactus: 
    def __init__(self):
        self.cactus = cactus 
        self.timer_cactus = 0 
        self.cactus_idx = random.randint(0,3) 
        self.cactus_width = self.cactus[0].get_width()
        self.cactus_height = self.cactus[0].get_height()
        self.iscactus = False
        self.cactu_x = -8 
        self.cactus_x_pos = screen_width - self.cactus_width
        self.cactus_y_pos = screen_height - self.cactus_height
        

    def cactus_moving(self): 
        if self.iscactus:
            screen.blit(self.cactus[self.cactus_idx],(self.cactus_x_pos,self.cactus_y_pos))
            self.cactus_x_pos += self.cactu_x

            if self.cactus_x_pos <= 0: 
                self.cactus_x_pos = screen_width - self.cactus_width
                self.cactus_idx = random.randint(0,3)
                self.iscactus = False

class Cloud: 
    def __init__(self): 
        self.cloud1 = cloud1
        self.cloud2 = cloud2
        self.cloud3 = cloud3 
        self.cloud_width = self.cloud1.get_width()
        self.cloud_height = self.cloud1.get_height()
        self.cloud_x_pos1 = self.cloud_width*2
        self.cloud_x_pos2 = self.cloud_width *4 
        self.cloud_x_pos3 = screen_width - self.cloud_width*2
        self.cloud_y_pos1 = self.cloud_height*2
        self.cloud_y_pos2 = self.cloud_height*2
        self.cloud_y_pos3 = self.cloud_height*2

        self.cloud_to_x = -7

    def draw_cloud(self): 
        screen.blit(self.cloud1,(self.cloud_x_pos1,self.cloud_y_pos1))
        screen.blit(self.cloud2,(self.cloud_x_pos2,self.cloud_y_pos2))
        screen.blit(self.cloud3,(self.cloud_x_pos3,self.cloud_y_pos3))

        self.cloud_x_pos1 += self.cloud_to_x
        self.cloud_x_pos2 += self.cloud_to_x
        self.cloud_x_pos3 += self.cloud_to_x 

        if self.cloud_x_pos3 <= 0:
            self.cloud_x_pos1 = screen_width + self.cloud_width*2
            self.cloud_x_pos2 = screen_width + self.cloud_width*4
            self.cloud_x_pos3 = screen_width*2 - self.cloud_width*4

class Collision: #공룡이 뛸때, 엎드렸을때, 점프했을 때의 모든 경우에 충돌처리를 해줘야 한다. 
    def check(self,dino,ptera,cactus): 
        #dino의 현재 이미지를 기반으로 rect를 생성한다. 
        if dino.isjumping:
            dino_image = dino.dino_running[dino.dino_running_idx] 
        elif dino.isducking: 
            dino_image = dino.dino_ducking[dino.dino_ducking_idx]
        else: 
            dino_image = dino.dino_running[dino.dino_running_idx]

        if dino.isducking: #공룡이 숙일때의 rect가 머리위로 올라가서 공룡테두리에 rect가 딱 맞게 숙일때하고 나머지를 나눠서 rect정보를 수정했다. 
            dino_height = dino_image.get_height()
            dino_rect = dino_image.get_rect()
            dino_rect.topleft = (10, screen_height - dino_height)
        else:
            dino_rect = dino_image.get_rect() 
            dino_rect.topleft = (10,dino.dino_y_pos)
         #dino_rect의 사각형 크기를 수동으로 줄여줄 수 있다. 너비, 높이 순 
        # pygame.draw.rect(screen,(255,0,0),dino_rect,2)

        #cactus의 존재여부로 cactus의 이미지 rect설정 및 cactus의 활성화 여부로 충돌 확인  
        if cactus.iscactus: 
            cactus_image = cactus.cactus[cactus.cactus_idx]
            cactus_rect = cactus_image.get_rect()
            cactus_rect.topleft = (cactus.cactus_x_pos + 10 ,cactus.cactus_y_pos)
            # pygame.draw.rect(screen,(0,255,0),cactus_rect,2)

            if dino_rect.colliderect(cactus_rect): 
                return True 
            
        if ptera.isptera: 
            ptera_image = ptera.ptera[ptera.ptera_idx]
            ptera_rect = ptera_image.get_rect()
            ptera_rect.topleft = (ptera.ptera_x_pos + 5,ptera.ptera_y_pos)
            # pygame.draw.rect(screen,(0,0,255),ptera_rect,2) #화면에 색깔이 ~인 ptera_rect의 사각형을 너비가 2가 되도록 그려라/ ptera_y 포지션을 디버깅하기 위해서 rect정보를 가시적으로 그렸다. 

            if dino_rect.colliderect(ptera_rect): 
                return True #부딪쳤다는 것을 말함 
            
        return False #부딪치지 않았다는 것을 말함

#----------------------------------------------------------------------#
#Functions
def spawn_enemy(): 
    choice = random.choice(["cactus","ptera"])
    if choice == "cactus": 
        cactus.iscactus = True 
        ptera.isptera = False 
    
    else: 
        ptera.isptera = True
        cactus.iscactus = False

def message():
    global font, game_ending_mg
    msg = font.render(game_ending_mg,True,(255,0,255))
    msg_rect = msg.get_rect(center=(screen_width/2,screen_height/2))
    screen.blit(msg,msg_rect)

#--------------------------------------------------------------------#

#--------------------------------------------------------------------#
#variables about moving 
running = True 

dino = Dino()
ptera = Ptera()
cactus = Cactus()
cloud = Cloud()
collision = Collision()
timer_enemy = 0
#---------------------------------------------------------------------#
#Main loop
while running: 
    clock.tick(FPS)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if dino.isjumping == False: #다이노가 점프했을때 다시 점프키를 누르면 문제가 생길수도 있어서 중복 점프 방지를 위해서 추가했다. 
                    dino.isjumping = True 

            elif event.key == pygame.K_DOWN:
                dino.isducking = True

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_DOWN: 
                dino.isducking = False 

    


    screen.fill(white)
    timer_enemy += 1 
    if timer_enemy >= 180: #적의 변환시간을 정해준다. 
        spawn_enemy()
        timer_enemy = 0 
    dino.discaction() #이렇게 하면 key 여부에 따라서 적당하게 코드가 작동할 것이다.
    ptera.ptera_fly()
    cactus.cactus_moving()
    cloud.draw_cloud()

    #drawing timer
    loading_time = int(pygame.time.get_ticks()- start_tick) // 1000 
    timer =  font.render(f"{loading_time}".zfill(2),True, (0,0,0))
    screen.blit(timer,(10,0))
    if loading_time >= 30: 
        ptera.to_x = -15
        cactus.cactu_x = -15

    #Collision checking
    if collision.check(dino,ptera,cactus):
        message()
        pygame.display.update() #update()함수가 꼭 한번만 쓰이라는 법은 없다. 고정관념을 버려라 
        pygame.time.delay(2000) #GAME OVER라는 글자가 너무 빨리 없어져서 추가했다. 
        running = False
    pygame.display.update()
    



pygame.quit()









#배운점 
# 1. randint(a,b)는 a 이상 b이하의 정수중 하나를 랜덤으로 불러온다.
# 2. 그림이 움직이는 것처럼 보이게 하고 싶다면 리스트에 필요한 그림들을 넣고 인덱스와 타이머를 이용해서 움직이는 효과를 낼 수 있다.
# 3. 한 캐릭터가 여러가지 동작을 할때, 이를테면 점프, 숙이기, 달리기 등을 할수 있다면 각각의 동작들이 겹치지 않게 하기 위해서 그것을 구분해야 한다. 이 때 사용할 수 있는 변수가 is_moving = False 이다.
# 4. randint()는 range()와는 달리 argument가 2개가 필요하다 range는 arg가 1개면 자동으로 0부터 시작하지만 randint()함수는 그렇지 않다. 0부터 시작하라고 정해줘야 한다.
# 5. choice = random.choice(["객체 이름1","객체 이름2"])을 통해서 장애물을 랜덤하게 나타나도록 만들 수 있다. 
# 6. 장애물을 선택하는데 있어서 타이머를 준비하여 그 타이머에 따라서 장애물이 나타날 수 있도록 만든다.
# 7. 이 get_rect()라는 함수는 기본적으로 (0,0)에 위치한 rect의 위치정보가 나온다. 그래서 정확한 충돌처리를 위해서는 충돌처리에 필요한 객체를 둘러싸고 있는 사각형의 정확한 위치를 정의해줘야 한다.
# 8. 이미지 자체가 아니라 이미지를 둘러싸고 있는 사각형의 왼쪽위 모서리의 좌표를 정의해준것. python에서 이미지의 위치의 기본 철학은 user가 객체의 이미지를 직접 설정해야 한다는 것이다. 
# 9. Dino 클래스의 변수에 접근하기 위해서는 dino.variable_name으로 접근해야 한다.(아주 중요한 개념)
# 10. rect.inflate_ip(-n,-m)을 함으로써 rect의 크기를 너비는 -n, 높이는 -m 만큼 줄일 수 있다. 
# 11. pygame.draw.rect(surface,color,rect,widht)로 image를 감싸고 있는 rect를 가시적으로 표현할 수 있다. -> 디버깅할 때 유용할 것. 
# 12. 함수를 드래그해서 우클릭하면 함수의 정의 및 정보들을 볼 수 있다. -> 유용 