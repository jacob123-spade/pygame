import pygame 
import sys, random 


speed = 15
 
#frame size 

frame_size_x = 720 
frame_size_y = 480

# Error check 

checking_error = pygame.init()

if checking_error[1] > 0:
    print("Error Occurs")

else: 
    print("Game Successfully initiated")

#Game initializing 

frame = pygame.display.set_mode((frame_size_x,frame_size_y))
pygame.display.set_caption("Snake Game")


#Colors 
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)


fps_controller = pygame.time.Clock()

square_size = 20 


#initialize Values



def init_val():
    global head_pos, snake_body, food_pos, food_spawn, score, direction 
    head_pos = [120,60]
    snake_body = [[120,60]]
    food_pos = [random.randrange(1,(frame_size_x // square_size)) * square_size, random.randrange(1,(frame_size_y// square_size))*square_size]
    food_spawn = True 
    score = 0
    direction = "RIGHT"

init_val()


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font,size)
    score_surface = score_font.render(f"Score: {str(score)}",True,color)
    score_rect = score_surface.get_rect()
    if choice == 1: 
        score_rect.midtop = (frame_size_x/10, 15)
    else: 
        score_rect.midtop = (frame_size_x/2,frame_size_y/1.25)

    frame.blit(score_surface,score_rect)
        

#Main loop  

while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == ord("e")) and direction != "DOWN":
                direction = "UP"

            elif (event.key == pygame.K_DOWN or event.key == ord("d")) and direction != "UP": 
                direction = "DOWN"
            
            elif (event.key == pygame.K_LEFT or event.key == ord("s")) and direction != "RIGHT": 
                direction = "LEFT"

            elif (event.key == pygame.K_RIGHT or event.key == ord("f")) and direction != "LEFT":
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
    snake_body.insert(0,list(head_pos))
    if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]: 
        score += 1 
        food_spawn = False 
    
    else: 
        snake_body.pop()

    if food_spawn == False:
        food_pos = [random.randrange(1,(frame_size_x // square_size)) * square_size, random.randrange(1,(frame_size_y// square_size))*square_size]
        food_spawn = True 

    
    #GFX
    frame.fill(black)
    for pos in snake_body: 
        pygame.draw.rect(frame,green,pygame.Rect(pos[0]+ 2, pos[1]+2, square_size -2,square_size),2)

    pygame.draw.rect(frame, red, pygame.Rect(food_pos[0],food_pos[1], square_size,square_size))

    # Game over conditions 
    for block in snake_body[1: ]: 
        if head_pos[0] == block[0] and head_pos[1] == block[1]: 
            init_val()

    #Update images 

    show_score(1,white,'consolas',20)
    pygame.display.update()
    fps_controller.tick(speed)

    




