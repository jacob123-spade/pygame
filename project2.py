import pygame 
from random import*  

pygame.init()

#Music 

bgm = pygame.mixer.Sound("/Users/hamin/Desktop/pygame/python/project/Dig Dug (NES) Music - Stage Theme.mp3")
bgm.play()
#Screen 

screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))

#Caption 
name = pygame.display.set_caption("추억의 오락실 게임1")

#background 

background = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/background.jpg")
   
#Stage

stage = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/stage.tiff")
stage_amo = stage.get_rect().size
stage_height = stage_amo[1]

#Ball 

ball_images = [
    pygame.image.load("/Users/hamin/Desktop/pygame/python/project/5213872.png"),
    pygame.image.load("/Users/hamin/Desktop/pygame/python/project/5213872 복사본.png"),
    pygame.image.load("/Users/hamin/Desktop/pygame/python/project/5213872 복사본 2.png"),
    pygame.image.load("/Users/hamin/Desktop/pygame/python/project/5213872 복사본 3.png")

]

 #Speeds are different according to the size 
ball_speed_y = -18

#balls (first)
balls = [] 
balls.append({"pos_x": 50, "pos_y": 50, "img_idx": 0, "to_x": 3, "to_y": -6, "init_spd_y": ball_speed_y})

weapon_to_remove = -1 
ball_to_remove = -1 

#Font 
game_font = pygame.font.Font(None, 40)
total_time = 100
start_tick = pygame.time.get_ticks() #시작 시간 정의 

game_result = "Game Over"

#Bullet 
bullet = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/bullet.png")
bullet_size = bullet.get_rect().size
bullet_width = bullet_size[0]
 
#Bullet can be used several times at once 
weapons = []
weapons_speed = 20


#FPS
fps = pygame.time.Clock()


#Character 
m_char = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/gun_man .tiff")
m_char_size = m_char.get_rect().size 
m_char_width = m_char_size[0]
m_char_height = m_char_size[1]
m_char_xpos = screen_width/2 - m_char_width/2 
m_char_ypos = screen_height - m_char_height - stage_height #이거 y position 정확하게 어떻게 잡는지 확인하기 

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
            elif event.key == pygame.K_SPACE: 
                bullet_x_pos = m_char_xpos + (m_char_width/2) - (bullet_width/2)
                bullet_y_pos = m_char_ypos
                weapons.append([bullet_x_pos,bullet_y_pos])
                


        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or pygame.K_RIGHT: 
                to_x = 0
            

    m_char_xpos += to_x * dt


    if m_char_xpos <= 0: 
        m_char_xpos = 0 
    elif m_char_xpos >= screen_width - m_char_width:
        m_char_xpos = screen_width - m_char_width

    #weapon position
    weapons = [[w[0], w[1] - weapons_speed] for w in weapons]

    #천장에 총알이 닿으면 없애기 
    weapons = [[w[0],w[1]] for w in weapons if w[1] > 0]    
 
    #공 위치 정의 
    for ball_idx, ball_val in enumerate(balls): 
        ball_pos_x = ball_val["pos_x"] 
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]
        # 가로벽에 닿았을 때 공 이동 위치 변화 
        if ball_pos_x <= 0 or ball_pos_x > screen_width - ball_width: 
            ball_val["to_x"] *= -1 
        #위아래 벽에 닿았을때 공 이동 위치 변화 
        if ball_pos_y >= screen_height - ball_width - stage_height: 
            ball_val["to_y"] = ball_val["init_spd_y"]

        else: #그 외의 모든 경우에는 속도를 증가 
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    #collide
    character_rect = m_char.get_rect()
    character_rect.left = m_char_xpos
    character_rect.top = m_char_ypos

    for ball_idx, ball_val in enumerate(balls): 
        ball_pos_x = ball_val["pos_x"] 
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        #Updating ball rect 
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x 
        ball_rect.top = ball_pos_y

    if character_rect.colliderect(ball_rect):
        break 

    for weapon_idx, weapon_val in enumerate(weapons):
        weapon_pos_x = weapon_val[0]
        weapon_pos_y = weapon_val[1]

        weapon_rect = bullet.get_rect()
        weapon_rect.left = weapon_pos_x
        weapon_rect.top = weapon_pos_y
        
        if weapon_rect.colliderect(ball_rect):
            weapon_to_remove = weapon_idx #해당 무기 없애기
            ball_to_remove = ball_idx #해당 볼 없애기
            
            if ball_img_idx < 3: 
                #현재 공 크기 정보를 가지고 옴 
                ball_width = ball_rect.size[0]
                ball_height = ball_rect.size[1]
                #나눠진 공 정보 
                small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                small_ball_width = small_ball_rect.size[0]
                small_ball_height = small_ball_rect.size[1]

                balls.append({"pos_x": ball_pos_x + (ball_width/2) - (small_ball_width/2), 
                            "pos_y": ball_pos_y + (ball_height/2) - (small_ball_height/2), 
                            "img_idx": ball_img_idx + 1, 
                            "to_x": -3, 
                            "to_y": -6, 
                            "init_spd_y": ball_speed_y})  #왼쪽으로 튕겨나가는 작은 공 
                            
                balls.append({"pos_x": ball_pos_x + (ball_width/2) - (small_ball_width/2), 
                            "pos_y": ball_pos_y + (ball_height/2) - (small_ball_height/2), 
                            "img_idx": ball_img_idx + 1 , 
                            "to_x": +3, 
                            "to_y": -6, 
                            "init_spd_y": ball_speed_y})  #오른쪽으로 튕겨나가는 작은 공
                
                break 

    if ball_to_remove > -1: 
        del balls[ball_to_remove]
        ball_to_remove = -1 

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove] 
        weapon_to_remove = -1 

    
    #모든 공을 없앤 경우 게임 종료 
    if len(balls) == 0: 
        game_result = "Mission Complete"
        break 
    
    screen.blit(background,(0,0)) 
    for bullet_x_pos,bullet_y_pos in weapons: 
        screen.blit(bullet,(bullet_x_pos,bullet_y_pos))
    for idx, val in enumerate(balls): 
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x,ball_pos_y))
    screen.blit(stage,(0,screen_height - stage_height))
    screen.blit(m_char,(m_char_xpos,m_char_ypos))
    
    #경과 시간 계산 
    elapsed_time = (pygame.time.get_ticks() - start_tick) / 1000
    timer = game_font.render("Time: {}".format(int(total_time - elapsed_time)),True, (255,255,255))
    screen.blit(timer,(10,0))
    if total_time - elapsed_time <= 0: 
        game_result = "Time Over"
        break 
    pygame.display.update()
#게임 오버 메시지 저장 
msg = game_font.render(game_result,True, (255,255,0))
msg_rect = msg.get_rect(center= (int(screen_width/2), int(screen_height/2)))
screen.blit(msg,msg_rect)
pygame.display.update()
bgm.stop()
pygame.time.wait(2000)
pygame.quit()
