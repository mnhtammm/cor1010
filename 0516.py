import pygame
import numpy as np

pygame.init()

screen_width = 800
screen_height = 900
screen_size = (screen_width, screen_height)

screen = pygame.display.set_mode (screen_size, )

done = False
FPS = 60
clock = pygame.time.Clock()

#------------------------------------------------------------------------
list_of_circles = []

def makerandomcircle():
    x = np.random.randint(0, screen_width)
    y = np.random.randint(0, screen_height)
    xy = np.array([x, y])
    vxy = np.random.uniform(low=1., high=15., size = 2)
    color = np.random.randint(low=0, high=256, size =3)
    radius = np.random.uniform(low=2., high=50.)

    monster = [xy, radius, vxy, color]
    return monster

def draw_circles(scrn, circles):
    for c in circles:
        pygame.draw.circle(surface=scrn,
                           color=c[3],
                           center=c[0],
                           radius=c[1])
    return

def update_circles(circles):
    for t in circles:
        xy = t[0]
        vxy = t[2]
        xy = xy + vxy
        t[0] = xy

        # print("---")

    pass

for i in range(10):
    circ = makerandomcircle()
    list_of_circles.append(circ)
#------------------------------------------------------------------------

while not done:
    #1. event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #2 draw
    screen.fill((255, 255, 255))
    
    draw_circles(screen, list_of_circles)

    #3 state update

    update_circles(list_of_circles)

    #4 refresh
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
print("bai bai")