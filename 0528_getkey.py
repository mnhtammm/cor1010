
# 1. Source code 1: confine the tree inside the screen. It cannot go outside
# 2. Source code 2: when the tree goes beyond the side boundaries, then it shoulf come in ar the left boundary
import numpy as np
import pygame

pygame.init()

screen_width = 800
screen_height = 900
BROWN = (150, 75, 0)
GREEN = (0, 128, 0)

screen = pygame.display.set_mode( (screen_width, screen_height))

done = False
FPS = 60
clock = pygame.time.Clock()

def draw_trees(x=0, y=0, green=(0,128,0)):
    pygame.draw.polygon(screen, green, [[x + 150, y + 150], 
                                        [x +  75, y +   0], 
                                        [x +   0, y + 150]])
    pygame.draw.rect(screen, BROWN, [x + 60, y+ 150, 30, 45])

    return
# end of draw_trees(x,y)

xtree = 200
ytree = 300

while not done:
    #1. Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        xtree -= 5
    if keys[pygame.K_RIGHT]:
        xtree += 5
    if keys[pygame.K_UP]:
        ytree -= 5
    if keys[pygame.K_DOWN]:
        ytree += 5
    if xtree < 0 :
        xtree = screen_width
    if xtree >= screen_width:
        xtree = 0
    

    #2. draw
    screen.fill( (255, 255, 255) )

    draw_trees(xtree, ytree, green= (0,128,0))
    
    # for i in range(10):
    #     for j in range(10):
    #         x0 = 150 * i
    #         y0 = -200 + 150 * j
    #         gr = np.random.randint(100,255)
    #         draw_trees(x0,y0, green=(0,gr,0))

    # update
    # x = x + dx

    #3. refresh
    pygame.display.flip()
    clock.tick(FPS)

#

pygame.quit()
print("bye~~")