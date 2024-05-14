import pygame
import numpy as np

pygame.init()

screen_WIDTH = 1100
screen_HEIGHT = 900
screen_size = (screen_WIDTH, screen_HEIGHT)
screen = pygame.display.set_mode(screen_size, )

clock = pygame.time.Clock()
FPS = 60 #Frames Per Second
done = False

def makeRandomCircle():
    x = np.random.randint(0, screen_WIDTH)
    y = np.random.randint(0, screen_HEIGHT)
    radius = np.random.uniform(low=5, high=100)
    spx = np.random.uniform(low=1, high=10)
    spy = np.random.uniform(low=1, high=10)
    color = np.random.randint(low=0, high=256, size=3)
    color[1] = 200
    color[2] = 100
    return x, y, radius, spx, spy, color


list_of_circle = []
for i in range (100):
    x, y, radius, spx, spy, color = makeRandomCircle()

    list_of_circle.append( [ [x,y], radius, [spx,spy], color])

def draw_circles(screen, circles ):
    for circle in circles:
        pygame.draw.circle(screen, 
                           color = circle[3], 
                           center = circle[0], 
                           radius = circle[1])
    return

def update_circles(circles):
    for c in circles:
        xy = c[0]
        sp = c[2]
        
    return

#main loop
while not done:
    #
    #1 event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #2 state update
    update_circles(list_of_circle)

    #3 draw
    screen.fill( (255, 255, 255) )

    draw_circles(screen, list_of_circle)


    #4 refresh the screen
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
print("pygame finished.")