import pygame 
from random import* 


pygame.init()

#BGM
main_theme_music = pygame.mixer.Sound("/Users/hamin/Desktop/pygame/python/project/project3/Star Wars main theme - 1 hour - (John Williams).mp3")
main_theme_music.play()
explosion = pygame.mixer.Sound("/Users/hamin/Desktop/pygame/python/project/project3/Explosion Sound.mp3")

#Sound Effect 
firing = pygame.mixer.Sound("/Users/hamin/Desktop/pygame/python/project/project3/Blaster Shot - Sound Effect for editing.mp3")
#screen 
screen_width = 1080
screen_height = 640 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Star Wars")


#Background
background =  pygame.image.load("/Users/hamin/Desktop/pygame/python/project/project3/스타워즈.jpeg")
back_width = background.get_rect().size[0]
back_height = background.get_rect().size[1]

#Main character 
m_char = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/project3/전투기.png")
m_char_width = m_char.get_rect().size[0]
m_char_height = m_char.get_rect().size[1]
m_char_x_pos = m_char_width
m_char_y_pos = screen_height/2

#Enemy 
enemy = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/project3/enemy .png")
enemy_width = enemy.get_rect().size[0]
enemy_height = enemy.get_rect().size[1]
enemy_x_pos = screen_width/2 
enemy_y_pos = screen_height/7

enemy_spdx = int(uniform(-30,30))
enemy_spdy = int(uniform(-30,30))

#Assiter 
assister = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/project3/Star-Wars Empire Ship-48.png")
assister_width = assister.get_rect().size[0]
assister_height = assister.get_rect().size[1]
assister_spdx = int(uniform(-10,10))
assister_spdy = int(uniform(-10,10))

assister_x_pos = screen_width/5 
assister_y_pos = screen_height/3



#Weapon(Main Character)
weapon = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/project3/beam1.png")
weapon_width = weapon.get_rect().size[0]
weapon_height = weapon.get_rect().size[1]
weapons = []
weapons1 = []

#Weapon(Enemy)
weapon1 = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/project3/beam3.jpg")
weapon1_width = weapon1.get_rect().size[0]
weapon1_height = weapon1.get_rect().size[1]
weapon1_pos_x = enemy_x_pos
weapon1_pos_y = enemy_y_pos

#Weapon(Assister)
weapon2 = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/project3/beam1.png")
weapon2_width = weapon2.get_rect().size[0]
weapon2_height = weapon2.get_rect().size[1]
weapon2_x_pos = assister_x_pos 
weapon2_y_pos = assister_y_pos 



#Coin(items)
coins = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/project3/game-coin_17879907.png")            
coin_weapon_width = coins.get_rect().size[0]
coin_weapon_height = coins.get_rect().size[1]
coin_weapon_x_pos = int(uniform(0,screen_width/2 - coin_weapon_width))
coin_weapon_y_pos = int(uniform(0,screen_height - coin_weapon_height))

#Explosion 
expl = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/project3/폭발.png")
expl1 = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/project3/폭발_비행기.png")
expl2 = pygame.image.load("/Users/hamin/Desktop/pygame/python/project/project3/폭발_적비행기 복사본.png")

#Removing
weapon_to_remove = -1 

#Moving 
to_x = 0 
to_y = 0  
char_spd = 0.5
weapon_spd = 30
weapon_spd1 = 60 

#FPS
fps = pygame.time.Clock()

#Font & Game Ending & Timer 
font = pygame.font.Font(None, 40)
ending = "Game Over"
start_tick = pygame.time.get_ticks()
full_time = 100
stamina_enemy = 10
stamina_main = 10 


#Functions 

def Moving():

    global fps, to_x, to_y, char_spd,m_char_x_pos,m_char_y_pos,m_char_width,m_char_height,weapons,coin_rect,m_char_rect
    dt = fps.tick(30)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            break 

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                to_x -= char_spd
            elif event.key == pygame.K_RIGHT: 
                to_x += char_spd
            elif event.key == pygame.K_UP: 
                to_y -= char_spd
            elif event.key == pygame.K_DOWN: 
                to_y += char_spd
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = m_char_x_pos + m_char_width/2 - weapon_width/2
                weapon_y_pos = m_char_y_pos + m_char_height/3
                weapons.append([weapon_x_pos,weapon_y_pos])
                firing.play()
         

            if event.key == pygame.K_s:
                to_x -= char_spd
            elif event.key == pygame.K_f: 
                to_x += char_spd
            elif event.key == pygame.K_e: 
                to_y -= char_spd
            elif event.key == pygame.K_d: 
                to_y += char_spd
                
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  
                to_x = 0 
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN: #이렇게 event.key == 으로 구분하지 않으면 애러가 날 수 있으므로 주의 
                to_y = 0
            if event.key == pygame.K_s or event.key == pygame.K_f:  
                to_x = 0 
            elif event.key == pygame.K_e or event.key == pygame.K_d: #이렇게 event.key == 으로 구분하지 않으면 애러가 날 수 있으므로 주의 
                to_y = 0
    m_char_x_pos += to_x * dt
    m_char_y_pos += to_y * dt

    if m_char_x_pos <= 0: 
        m_char_x_pos = 0 
    
    elif m_char_x_pos >= screen_width/2 - m_char_width:
        m_char_x_pos = screen_width/2 - m_char_width

    
    if m_char_y_pos <= 0: 
        m_char_y_pos = 0 
    elif m_char_y_pos >= screen_height - m_char_height: 
        m_char_y_pos = screen_height - m_char_height

def Weapons():
    global weapons,weapons1
    weapons = [[w[0]+ weapon_spd, w[1]] for w in weapons] 
    weapons = [[w[0], w[1]] for w in weapons if w[0] <= screen_width - weapon_width]
    


def Weapon_Ene():
    global weapon1_pos_x,weapon1_pos_y, weapon_spd, enemy_x_pos,enemy_y_pos
    weapon1_pos_x -= weapon_spd1
    if weapon1_pos_x <= 0: 
        weapon1_pos_x = enemy_x_pos 
        weapon1_pos_y = enemy_y_pos
   
    
def Assister_Moving(): 
    global assister_spdx,assister_spdy,assister_x_pos,assister_y_pos,assister_width,assister_height

    assister_x_pos += assister_spdx 
    assister_y_pos += assister_spdy 

    if assister_x_pos <= 0 or assister_x_pos >= screen_width/2 - assister_width: 
        assister_x_pos += -(assister_spdx)
        assister_spdx = int(uniform(-10,10))
        assister_spdy = int(uniform(-10,10))

    elif assister_y_pos <= 0 or assister_y_pos >= screen_height - assister_height: 
        assister_y_pos += -(assister_spdy)
        assister_spdx = int(uniform(-10,10))
        assister_spdy = int(uniform(-10,10))

    if assister_spdx == 0 or assister_spdy == 0: 
        assister_spdx = int(uniform(-10,10))
        assister_spdy = int(uniform(-10,10))

def Weapon_Assis():
    global weapon2_width,weapon2_height,assister_width,assister_x_pos,assister_y_pos,screen_width,weapon2_x_pos,weapon2_y_pos
    weapon2_x_pos += weapon_spd
    
    if weapon2_x_pos >= screen_width- weapon2_width: 
        weapon2_x_pos = assister_x_pos
        weapon2_y_pos = assister_y_pos 


    

    
while True: 
    Moving()
    Weapons()
    Weapon_Ene()
    Assister_Moving()
    Weapon_Assis()
    
    
    
    enemy_x_pos += enemy_spdx 
    enemy_y_pos += enemy_spdy 

    if enemy_x_pos <= screen_width/2 or enemy_x_pos >= screen_width - enemy_width: 
        enemy_x_pos += -(enemy_spdx) 
        enemy_spdx = int(uniform(-30,30)) 
        enemy_spdy = int(uniform(-30,30))

        
    elif enemy_y_pos <=0 or enemy_y_pos >= screen_height - enemy_height: 
        enemy_y_pos += -(enemy_spdy)
        enemy_spdx = int(uniform(-30,30))
        enemy_spdy = int(uniform(-30,30))

    if enemy_spdx == 0 or enemy_spdy == 0:
            enemy_spdx = int(uniform(-30,30)) 
            enemy_spdy = int(uniform(-30,30))
    
    #Collision 

    m_char_rect = m_char.get_rect() 
    m_char_rect.left = m_char_x_pos 
    m_char_rect.top = m_char_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos 
    enemy_rect.top = enemy_y_pos 

    coin_rect = coins.get_rect()
    coin_rect.left = coin_weapon_x_pos
    coin_rect.top = coin_weapon_y_pos

    for weapon_idx, weapon_val in enumerate(weapons):
        weapon_rect = weapon.get_rect() 
        weapon_rect.left = weapon_val[0]
        weapon_rect.top = weapon_val[1]

        if weapon_rect.colliderect(weapon1_rect):
            weapon_to_remove = 0
            expl_x_pos = weapons[0][0]
            expl_y_pos = weapons[0][1]
            weapon1_pos_x = enemy_x_pos
            weapon1_pos_y = enemy_y_pos 
            screen.blit(expl, (expl_x_pos,expl_y_pos))
            pygame.display.update()
            pygame.time.wait(30)
            explosion.play()
            break
        if weapon_rect.colliderect(enemy_rect): 
            weapon_to_remove = 0 
            expl2_x_pos = enemy_x_pos 
            expl2_y_pos = enemy_y_pos 
            screen.blit(expl2,(expl2_x_pos,expl2_y_pos))
            pygame.display.update()
            pygame.time.wait(30)
            explosion.play()
            stamina_enemy -= 0.5
            break 
            

    if weapon_to_remove == 0: 
        del weapons[weapon_to_remove]
        weapon_to_remove = -1 
        
    
    weapon1_rect = weapon1.get_rect()
    weapon1_rect.left = weapon1_pos_x 
    weapon1_rect.top = weapon1_pos_y 

    weapon2_rect = weapon2.get_rect()
    weapon2_rect.left = weapon2_x_pos 
    weapon2_rect.top = weapon2_y_pos 

    if weapon1_rect.colliderect(weapon2_rect):
            expl_x_pos = weapon1_pos_x
            expl_y_pos = weapon1_pos_y 
            weapon2_pos_x = assister_x_pos
            weapon2_pos_y = assister_y_pos
            weapon1_pos_x = assister_x_pos
            weapo2_pos_y = assister_y_pos
            screen.blit(expl, (expl_x_pos,expl_y_pos))
            pygame.display.update()
            pygame.time.wait(30)
            explosion.play()

    if weapon2_rect.colliderect(enemy_rect):
        expl2_x_pos = enemy_x_pos 
        expl2_y_pos = enemy_y_pos
        weapon2_x_pos = assister_x_pos
        weapon2_y_pos = assister_y_pos
        screen.blit(expl2,(expl2_x_pos,expl2_y_pos))
        pygame.display.update()
        pygame.time.wait(30)
        explosion.play()
        stamina_enemy -= 0.5

            

    if m_char_rect.colliderect(weapon1_rect):
        screen.blit(expl1,(m_char_x_pos,m_char_y_pos))
        pygame.display.update()
        pygame.time.wait(30)
        explosion.play()
        weapon1_pos_x = enemy_x_pos
        weapon1_pos_y = enemy_y_pos 
        stamina_main -= 1

    if m_char_rect.colliderect(coin_rect):
        coin_weapon_x_pos = -(coin_weapon_width)
        coin_weapon_y_pos = 0
        weapon_spd = 80
        

#Timer 
    loading_tick = int(pygame.time.get_ticks() - start_tick) /1000
    clock = font.render(f"Time: {int(full_time - loading_tick)}",True,(0,0,255))
    clock_width = clock.get_rect().size[0]

    damage_enemy = font.render(f"Enemy: {stamina_enemy}",True, (0,255,255))
    damage_enemy_width = damage_enemy.get_rect().size[0]


    damage_main = font.render(f"Main: {stamina_main}",True,(0,255,255))
    damage_main_width = damage_main.get_rect().size[0]


    if stamina_enemy < 0:
        ending ="You Win"
        break
    elif stamina_main < 0: 
        ending = "You lose"
        break
    elif stamina_enemy < 0 and stamina_main < 0:
        ending = "Draw"
        break 

    
    if int(full_time - loading_tick) < 0: 
        ending = "Time Over"
        break
    
    
    screen.blit(background,(0,0))
    for weapon_pos_x, weapon_pos_y in weapons:
        screen.blit(weapon,(weapon_pos_x,weapon_pos_y))
    for weapon_x,weapon_y in weapons1: 
        screen.blit(weapon,(weapon_x,weapon_y))
    screen.blit(m_char,(m_char_x_pos,m_char_y_pos))
    screen.blit(weapon1,(weapon1_pos_x,weapon1_pos_y))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    screen.blit(weapon2,(weapon2_x_pos,weapon2_y_pos))
    screen.blit(assister,(assister_x_pos,assister_y_pos))
    screen.blit(coins,(coin_weapon_x_pos,coin_weapon_y_pos))
    screen.blit(clock,(10,0))
    screen.blit(damage_enemy,(screen_width- damage_enemy_width,0))
    screen.blit(damage_main,(screen_width/2 - damage_main_width,0))
    
    pygame.display.update()

msg = font.render(ending,True,(255,0,255))
msg_rect = msg.get_rect(center = (screen_width/2,screen_height/2))
screen.blit(msg,msg_rect)
pygame.display.update()
pygame.time.wait(1000)
main_theme_music.stop()
    


pygame.quit()