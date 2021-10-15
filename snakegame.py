import pygame
from random import randint
import winsound
from random import randrange

pygame.init()


# Game color
white = (255,255,255)
red = (255,0,0)
green = (0,200,0)
black = (0,0,0)
blue = (0,0,255)
yellow = (255, 255, 0)

screen_width = 700
screen_height = 700


# Creating window
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game - Blank")
pygame.display.update()

# Game specific variables

font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text,[x, y])


def snake(gameWindow, snk_list,color,  size):
    for X, Y in snk_list:
        pygame.draw.rect(gameWindow, color, [X, Y, size, size])
def snakeCircle(gameWindow, snk_list, color, size):
    for x,y in snk_list:
        pygame.draw.circle(gameWindow, color, (x,y), size)

clock = pygame.time.Clock()

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,210,229))
        welcome_img = pygame.image.load('welcomdeimg.jfif')
        welcome_img = pygame.transform.scale(welcome_img, (screen_width,screen_height))
        gameWindow.blit(welcome_img, (0,0))
        text_screen("Welcome to Snakes", white, 160, 450)
        text_screen("Press Space Bar To Play", white, 132, 490)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # pygame.mixer.music.load('back.mp3')
                    # pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)

def gameloop():
    exit_game = False
    game_over = False
    score = 0
    
    snake_X = 200
    snake_Y = 200
    snake_size = 15
    food_size = 15
    fps = 30
    init_velocity = 10
    velocity_x = 4
    velocity_y = 4
    food_x = randint(0, screen_width)
    food_y = randint(0, screen_height)

    snk_lenth = 1
    snk_list = []
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            gameover_img = pygame.transform.scale(gameover_img, (screen_width, screen_height))
            gameWindow.blit(gameover_img,  (0,0))
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
            # winsound.PlaySound('Game over sound effect HD.wav', winsound.SND_FILENAME)

        else : 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if snake_X >= screen_width or snake_Y >= screen_width : 
                    exit_game == True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0
            snake_X += velocity_x
            snake_Y += velocity_y
            eaten = 10
            if abs(snake_X - food_x)<eaten and abs(snake_Y - food_y)<eaten:
                score += 10
                food_x = randint(20, screen_width / 2)
                food_y = randint(20, screen_height / 2)
                snk_lenth += 2
                winsound.Beep(500, 70)
                

        
            gameWindow.fill(white)
            img = pygame.image.load('Download Flat Snake Background for free.jfif')
            img = pygame.transform.scale(img, (screen_width,screen_height))
            gameWindow.blit(img, (0, 0))
            text_screen("score + :" + str(score), green, 5, 5)
            pygame.draw.circle(gameWindow, red, (food_x,food_y), food_size)

            head = []
            head.append(snake_X)
            head.append(snake_Y)
            snk_list.append(head)

            if len(snk_list)>snk_lenth:
                del snk_list[0]
            if head in snk_list[:-1]:
                gameover_img = pygame.image.load('Gameover Electronic Sound Wind Hi Burst Video Game Background Map.jfif')
                game_over = True   
                winsound.PlaySound('Game over sound effect HD.wav', winsound.SND_FILENAME)
            if snake_X<0 or snake_X>screen_width or snake_Y<0 or snake_Y>screen_height:
                game_over = True
                gameover_img = pygame.image.load('Gameover Electronic Sound Wind Hi Burst Video Game Background Map.jfif')
                winsound.PlaySound('Game over sound effect HD.wav', winsound.SND_FILENAME)


            snakeCircle(gameWindow, snk_list,  black, snake_size)
            
           
        pygame.display.update()
        clock.tick(fps)
            
        


        
    pygame.quit()
    quit()
# gameloop()
welcome()
