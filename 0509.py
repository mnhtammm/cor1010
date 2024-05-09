import pygame
import numpy as np

pygame.init()

RED = (255, 0, 0)
WHITE = (255, 255, 255)

screen_size = (1000,850)
screen = pygame.display.set_mode(screen_size)
 
pygame.display.set_caption("0509")

done = False
clock = pygame.time.Clock()
FramePerSecond = 60

# x, y, radius, spx, spy, red, green, blue
list_of_circles = [ [ [10, 20], 50, 5, 4, [255, 0, 0]],
                    [ [100, 520], 10, -5, -4, [0, 0, 255]],
                  ]

while not done:
    #1. event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #2 clear the display
    screen.fill (WHITE)

    #3 state update

    for circle in list_of_circles:
        spx = circle[2]
        spy = circle[3]
        #color = circle[4]
        circle[0][0] += spx #x
        circle[0][1] += spy #y

        if (circle[0][0] >= screen_size[0]) or (circle[0][0] < 0):
            spx = -spx
        if (circle[0][1] >= screen_size[1]) or (circle[0][1] < 0):
            spy = -spy
    
    #4 draw
    for circle in list_of_circles:
        color = circle[4]
        center = circle[0]
        radius = circle[1]
        pygame.draw.circle( screen,
                            color,
                            center=center,
                            radius=radius)
    
    #5 update the screen
    pygame.display.flip()
    clock.tick(FramePerSecond)

pygame.quit()