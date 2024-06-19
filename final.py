import pygame
import numpy as np

pygame.init()

swidth = 900
sheight = 800
screen = pygame.display.set_mode( (swidth, sheight))
done = False
FPS = 60
clock = pygame.time.Clock()

class Rectangle():
    def __init__(self, x, y, w, h, color, vy=0, sy=0):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.color = color
        self.vy = vy
        self.sy = sy

    def update(self):
        self.y = self.y + self.vy
        self.vy += self.sy
        if self.y >= sheight:
            self.y = -self.height
            self.vy = vy
    
    def draw(self,screen):
        pygame.draw.rect (screen,
                          self.color,
                          [self.x, self.y, self.width, self.height])

rlist =[]
for i in range(100):
    color = np.random.randint(low=0, high=256, size=3)
    x = np.random.randint(0,swidth)
    vy = np.random.uniform(low=-10, high=11)
    sy = np.random.uniform(0., .5)
    r = Rectangle(x, 100, 50, 30, color, vy,sy)
    rlist.append(r)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill( (255, 255, 255) )

    for r in rlist:
        r.draw(screen)
        r.update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()