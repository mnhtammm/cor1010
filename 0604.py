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
                          #x           y    r    vx  vy
circlegroup.append( [screen_width/2., 100., 40., 3., 0.] )

def EuclideanDistance(x1, x2, y1, y2):
    d2 = (x1 - x2)**2 + (y1-y2)**2
    d = np.sqrt(d2)
    return d

def collision_check(bc, rc):
    # if the two circles overlap, then return True
    # otherwise, return False
    x1 = bc[0]
    y1 = bc[1]
    r1 = bc[2]

    x2 = rc[0]
    y2 = rc[1]
    r2 = rc[2]

    d12 = EuclideanDistance(x1,x2,y1,y2)

    r12 = r1 + r2

    if d12 < r12:
        return True    
    else:
        return False
#end of overlap check

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
    if redcircle:
        for c in circlegroup:
            #check overlap
            if collision_check(c, redcircle) == True:
                #delete/remove circle and redcircle
                print("Collision!")
            pass
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