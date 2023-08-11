import pygame, time
from planet import *

pygame.init()

class World:

    def __init__(self):
        self.running = True
        self.resolution = (1280,720)
        self.screen = pygame.display.set_mode([self.resolution[0], self.resolution[1]])
        self.mainClock = pygame.time.Clock()
        self.FPS = 60
        self.backgroundColor = [0, 0, 0]
        self.position = [0, 0]


        self.objects = []

        self.position = [0, 0]
        self.zoom = .000001
        self.speed = 5
        self.prev_time = time.time()

        #   WORLD LOAD

        Earth = Planet(self, "Earth", [0, 360], 5.972 * 10**24, 6365000 *2, [0, 255, 150], [0, 0], True, True, True, True)
        Moon = Planet(self, "Moon", [384467000, 360], 7.35 * 10**22, 1737400 *2, [100, 100, 100], [0, 40000], True, True, True, True)



    def update(self):
        self.screen.fill(self.backgroundColor)
        #   TIME   
        self.mainClock.tick(self.FPS)
        self.now = time.time()
        self.deltaTime = (self.now - self.prev_time) * 100
        self.prev_time = self.now
        
        self.control()
        for object in self.objects:
            object.update()

        

        pygame.display.flip()


    def control(self):
        
        speed = self.speed

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RSHIFT]:
            speed += (self.deltaTime*self.zoom**-1) /10000

        if keys[pygame.K_LEFT]:
            self.position[0] += speed * self.deltaTime * self.zoom**-1

        if keys[pygame.K_RIGHT]:
            self.position[0] -= speed * self.deltaTime * self.zoom**-1


        if keys[pygame.K_UP]:
            self.position[1] += speed * self.deltaTime * self.zoom**-1


        if keys[pygame.K_DOWN]:
            self.position[1] -= speed * self.deltaTime * self.zoom**-1

        if keys[pygame.K_y]:
            self.position[0] = -self.objects[0].position[0] + self.resolution[0]/2 - self.resolution[0] * (self.zoom - 1) / self.zoom / 2
            self.position[1] = -self.objects[0].position[1] + self.resolution[1]/2 - self.resolution[1] * (self.zoom - 1) / self.zoom / 2

        if keys[pygame.K_x]:
            self.position[0] = -self.objects[1].position[0] + self.resolution[0]/2 - self.resolution[0] * (self.zoom - 1) / self.zoom / 2
            self.position[1] = -self.objects[1].position[1] + self.resolution[1]/2 - self.resolution[1] * (self.zoom - 1) / self.zoom / 2

        zoom = 0.00000001


        if keys[pygame.K_KP_PLUS]:
            self.zoom += zoom*10

        if keys[pygame.K_KP_MINUS]:
            if not self.zoom <= zoom:
                self.zoom -= zoom


world = World()


while world.running:

    world.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            world.running = False