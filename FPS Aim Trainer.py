import pygame
import random
pygame.init()
pygame.display.set_caption("FPS Aim Trainer")
screen = pygame.display.set_mode((1280,720))



white = (255,255,255)
red = (255,0,0)
black = (0, 0, 0)

screen.fill(white)
clock = pygame.time.Clock()


circleX = random.randint(0,1280)
circleY = random.randint(0,720)
circlePixels = random.randint(15,18)
target = pygame.draw.circle(screen, red, (circleX,circleY),(circlePixels))

score_total = 150
scoreX = 20
scoreY = 20
font = pygame.font.Font("freesansbold.ttf", 40)
def screenScore(x,y):
    score = font.render("Targets Left:" + str(score_total), True, black)
    screen.blit(score, (x,y))


open = True
while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False


    
    
    mousePos = pygame.mouse.get_pos()

    if target.collidepoint(mousePos):
        if pygame.mouse.get_pressed()[0] == 1:
            screen.fill(white)
            circleX = random.randint(0,1280)
            circleY = random.randint(0,720)
            circlePixels = random.randint(15,18)
            target = pygame.draw.circle(screen, red, (circleX,circleY),(circlePixels))
            score_total -= 1
        if score_total <= 0:
            open = False
    screenScore(scoreX,scoreY)
    pygame.display.update()
    clock.tick()
            


        

    
        


