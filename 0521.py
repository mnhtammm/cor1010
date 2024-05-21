import numpy as np
import pygame

pygame.init()

screen_width = 800
screen_height = 900

screen = pygame.display.set_mode( (screen_width, screen_height))

done = False
FPS = 60
clock = pygame.time.Clock()

def makeRandomCircle():
    x = np.random.randint(0, screen_width)
    y = np.random.randint(0, screen_height)
    xy = np.array( [x, y] ,dtype="float")
    vxy = np.random.uniform(low = 1, high = 13, size = 2)
    color = np.random.randint(low = 0, high = 256, size = 3)
    radius = np.random.uniform(low = 2, high = 50)

    monster = {
        "loc" : xy,
        "radius" : radius,
        "velocity" : vxy,
        "rgb" : color
    }

    return monster

def draw_circles(myscreen, circles):
    for circ in circles:
        pygame.draw.circle(surface=myscreen,
                           color= circ["rgb"],
                           center= circ["loc"],
                           radius= circ["radius"])
    #
    return

list_of_circle = []

for i in range(100):
    c = makeRandomCircle()
    list_of_circle.append( c )

while not done:
    #1. Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #2. draw
    screen.fill( [255, 255, 255])

    draw_circles(screen, list_of_circle)

    #3. state update

    for circ in list_of_circle:
        #1 update
        circ["loc"] += circ["velocity"]
        #2 check the location
        if circ["loc"][0] >= screen_width or circ["loc"][0] < 0:
            circ["velocity"][0] *= -1
        if circ["loc"][1] >= screen_height or circ["loc"][1] < 0:
            circ["velocity"][1] *= -1
    # xy = circ["loc"]
    #x = xy[0]
    #y = xy[1]

    #x = circ["loc"][0]
    #y = circ["loc"][1]
    
        circ["velocity"][1] += .5

    #4. refresh
    pygame.display.flip()
    clock.tick(FPS)
#

#save things

#

pygame.quit()
print("bye~~")