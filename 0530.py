import numpy as np
import pygame

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
PINK = (255, 182, 193)

screen_width = 800
screen_height = 900

screen = pygame.display.set_mode( (screen_width, screen_height))

done = False
FPS = 60
clock = pygame.time.Clock()

player = [screen_width/2., screen_height - 100, 30, 15]

circlegroup = []
                          #x           y         vx  vy
circlegroup.append( [screen_width/2., 100., 40., 3., 0.] )

def update_large_circles():
    for c in circlegroup:
        c[0] += c[3]
        if (c[0]-c[2]) < 0 or (c[0]+c[2]) >= screen_width:
            c[3] *= -1
    pass
#end of update_large_circles()
    
def draw_large_circles(screen):
    for c in circlegroup:
        pygame.draw.circle(screen, BLACK, [c[0], c[1]], c[2])
    pass
#end of draw_large_circles(scrn)

redcircle = None

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] == True:
        #left key pressed
        player[0] -= 3
        pass
    elif keys[pygame.K_RIGHT]:
        #right key pressed, move the player to the right
        player[0] += 3
        pass
    elif keys[pygame.K_SPACE]:
        #shoot
        if redcircle:
            pass
        else:
            redcircle = [ player[0], player[1], 5, 0, -6]
        pass
    
    #update large circles
    update_large_circles()

    #update for red circle if there is

    if redcircle:
        redcircle[1] += redcircle[4]

        if redcircle[1] < 0:
            redcircle = None

    #check overlap
    for c in circlegroup:
        #check overlap
        pass

    #draw
    screen.fill( WHITE )

    pygame.draw.rect(screen, PINK, player)

    if redcircle:
        pygame.draw.circle(screen, RED, [redcircle[0], redcircle[1]], radius= redcircle[2])

    draw_large_circles(screen)

    #refresh
    pygame.display.flip()
    clock.tick(FPS)

#

pygame.quit()
print("bye~~")