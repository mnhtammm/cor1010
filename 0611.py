import pygame
import numpy as np

pygame.init()

swidth = 900
sheight = 800
screen = pygame.display.set_mode( (swidth, sheight))
done = False
FPS = 60
clock = pygame.time.Clock()

class Circle():
    def __init__(self, x, y, radius=10, color=(200, 0, 0), vx=0, vy=0):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vx = vx
        self.vy = vy
        self.sy = .5
    
    def update(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.vy += self.sy
        # if self.x < 0 or self.x >= swidth:
        #     self.vx = -self.vx
        # if self.y < 0 or self.y >= sheight:
        #     self.vy = -self.vy
    
    def draw(self, screen):
        pygame.draw.circle (screen, 
                            color=self.color, 
                            center=(self.x, self.y), 
                            radius=self.radius)

circ = Circle(200, 100, vx = 6, vy = -2)

clist = []
for i in range(1000):
    color = np.random.randint(low=0, high=256, size=3)
    vx = np.random.uniform(low=-7, high=8)
    vy = np.random.uniform(low=-10, high=11)
    c = Circle(swidth//2, 100,
               color= color,
               vx= vx,
               vy= vy)
    clist.append(c)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True        
    screen.fill( (255, 255, 255) )

    circ.draw(screen)

    for c in clist:
        c.draw(screen)

    circ.update()
    for c in clist:
        c.update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()


    
