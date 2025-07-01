import pygame 
import random, sys

speed = 15 

frame_size_x = 720 
frame_size_y = 480

check_errors = pygame.init() 
print(check_errors) 

if (check_errors[1] > 0): 
    print(f"Error {check_errors[1]}")

else: 
    print("Game Successfully initialized")


#initialize Game 

pygame.display.set_caption("Snake Game")
game_window = pygame.display.set_mode((frame_size_x,frame_size_y))


#Colors 
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)


fps_controller = pygame.time.Clock()

#one snake square size 
square_size = 20 


def init_vars(): #초기 변수를 설정하는 함수이다. 
    global head_pos, snake_body, food_pos, food_spawn, score, direction 
    direction = "RIGHT"
    head_pos = [120,60]
    snake_body = [[120, 60]]
    food_pos = [random.randrange(1,(frame_size_x // square_size)) * square_size,
                random.randrange(1,(frame_size_y // square_size)) * square_size] #food의 좌표를 리스트 안에 넣어서 [x,y]로 만들어 준 것 
    
    food_spawn = True 
    score = 0 

init_vars()

def show_score(choice, color, font, size): 
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f"Score: {str(score)}",True, color)
    score_rect = score_surface.get_rect()
    if choice == 1: 
        score_rect.midtop = (frame_size_x / 10, 15)

    else: 
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)

    game_window.blit(score_surface,score_rect)


#game loop 


while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
             
        elif event.type == pygame.KEYDOWN: 
            if (event.key == pygame.K_UP or event.key == ord("w")) and direction != "DOWN": 
                direction = "UP"

            elif (event.key == pygame.K_DOWN or event.key == ord("s")) and direction != "UP": 
                direction = "DOWN"

            elif (event.key == pygame.K_LEFT or event.key == ord("a")) and direction != "RIGHT": 
                direction = "LEFT"

            elif (event.key == pygame.K_RIGHT or event.key == ord("d")) and direction != "LEFT": 
                direction = "RIGHT"

    if direction == "UP": 
        head_pos[1] -= square_size 

    elif direction == "DOWN": 
        head_pos[1] += square_size 

    elif direction == "LEFT": 
        head_pos[0] -= square_size 

    else: 
        head_pos[0] += square_size

    
    if head_pos[0] < 0: 
        head_pos[0] = frame_size_x - square_size
    
    elif head_pos[0] > frame_size_x - square_size: 
        head_pos[0] = 0

    elif head_pos[1] < 0:
        head_pos[1] = frame_size_y - square_size 

    elif head_pos[1] > frame_size_y - square_size: 
        head_pos[1] = 0 

    
    #eating apple 
    snake_body.insert(0,list(head_pos)) # 머리를 새 위치에 추가함 -> snake 가 움직이는 것처럼 보이게 하기 위해서 그 다음에는 pop()을 통해서 snake의 꼬리를 잘라낸다. 그러면 snake가 움직인 것처럼 보인다. 
    if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]: #딱 맞아야 먹을 수 있다.
        score += 1 
        food_spawn = False
        
    else: 
        snake_body.pop()

    # spawn food 
    if not food_spawn: # food의 형태가 화면에 표시되지 않으면 food의 position을 갱신해주고 화면에 보이게 한다. 
        food_pos = [random.randrange(1,(frame_size_x // square_size)) * square_size,
                random.randrange(1,(frame_size_y // square_size)) * square_size]
        food_spawn = True
        
    # GFX -> Graphics의 준말로 보통 게임 개발자들이 화면에 객체를 그리는 부분에 대한 주석을 달때 사용된다. 
    game_window.fill(black)
    for pos in snake_body: 
        pygame.draw.rect(game_window,green,pygame.Rect(
            pos[0] + 2, pos[1] + 2, # 각 사각형이 살짝씩 여백을 두기 위한 코드. 
            square_size -2, square_size),2) #크기를 줄여서 격자처럼 보이게 한다.(그냥 디자인 부분)
        
    pygame.draw.rect(game_window,red, pygame.Rect(food_pos[0],food_pos[1],square_size,square_size))

    #game over conditions 

    for block in snake_body[1: ]: 
        if head_pos[0] == block[0] and head_pos[1] == block[1]: # 뱀의 몸통끼리 부딪치면 다시 모든 변수를 초기화 해버린다.  
            init_vars()

    show_score(1,white,'consolas', 20) # 화면에 score 를 표시해준다. 
    pygame.display.update()
    fps_controller.tick(speed)
    


    
#배운 점들 
# 1. pygame.init() 함수는 성공한 모듈의 개수와 실패한 모듈의 수를 튜플 형식으로 나타내준다.
# 2. (6,0) -> 6개의 모듈 성공작동, 0개의 모듈 오륲 라는 의미이다. 
# 3. ord(char) 함수는 입력받은 char의 유니코드(Unicode) 코드 포인트를 정수로 반환해준다.
# 4. sys module은 파이썬에서 기본제공하는 시스템관련 기능을 다루는 모듈이다. os와 파이썬 인터프리터 사이에서 다양한 정보를 주고 받고 제어하도록 도와준다.
# 5. sys.exit()는 게임이나 프로그램을 종료할때 사용한다. 
# 6. global은 함수 내에서 전역 변수에 접근해서 값을 수정하거나 재할당할때 사용된다. init_val()에서는 변수가 처음 등장하는 시점이지만 global을 사용함으로써 
# 함수내에서의 변수들이 함수 외부로까지 할당된다. 
# 7. 전역변수를 함수내에서 변경없이 사용하고 싶으면 global없이도 그냥 사용하면된다. global은 전역변수를 함수내에서 변경 및 재할당할때 사용하는 것이다.
# 8. pygame.Rect(x,y,width,height)인 사각형을 만들라는 함수 
# 9. 함수를 만들어놓고 호출하지 않으면 지역변수가 외부로 적용되지 않는다. 

#느낀 점 
#전반적으로 코드가 깔끔하고 세련됨, 넣어야 할것은 넣고 안 넣어도 될 것은 넣지 않음. 
#코드 모방하면서 다시 만들어 봐야겠음 