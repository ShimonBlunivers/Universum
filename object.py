import pygame, math


class Object:

    G = 6.67430 * 10**-11
    PI = 3.1415926535

    def __init__(self, world, startingPosition, mass, size = [50, 50], color = None, velocity = [0, 0], showOrbit = False, gravitationalField = True, affectedByGravity = True, isSphere = True):
        self.world = world
        self.startingPosition = startingPosition
        self.position = self.startingPosition
        self.mass = mass
        self.gravitationalField = gravitationalField
        self.affectedByGravity = affectedByGravity
        self.isSphere = isSphere
        if type(size) == int:
            self.size = [size, size]
        else:
            self.size = size
        self.radius = self.size[0]/2
        self.color = color
        self.velocity = velocity
        self.force = [0, 0]
        self.orbit = []
        self.showOrbit = showOrbit
        self.world.objects.append(self)

    def updateOrbit(self):
        if self.isSphere:
            self.orbit.append([self.position[0], self.position[1]])
        else:
            x = self.position[0] + self.size[0]/2
            y = self.position[1] + self.size[1]/2
            self.orbit.append([x, y])

    def applyForce(self):
        self.velocity[0] += self.force[0]/self.mass
        self.velocity[1] += self.force[1]/self.mass


    def updatePosition(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def applyGravity(self):
        if self.affectedByGravity:
            touching = []
            for object in self.world.objects:
                if object != self and object.gravitationalField:
                    r = math.sqrt((self.position[0] - object.position[0])**2 + (self.position[1] - object.position[1])**2).real
                    if r <= self.radius + object.radius:
                        touching.append(object)
                        

                    F = (self.G * self.mass * object.mass / (r**2)) 
                    

                    alpha = math.atan2(object.position[1] - self.position[1], object.position[0] - self.position[0])

                    self.force[0] += (F * math.cos(alpha)) 
                    self.force[1] += (F * math.sin(alpha))

                    

    def renderOrbit(self):
        if self.showOrbit:
            if self.color == None:
                color = [255, 255, 255]
            else:
                color = self.color
            orbitPoints = []
            if len(self.orbit) > 2:
                for point in self.orbit[-100000::]:
                    offsetX = (point[0] + self.world.position[0]) * self.world.zoom
                    offsetY = (point[1] + self.world.position[1]) * self.world.zoom
                    orbitPoints.append([offsetX, offsetY])
                offsetZoom = round((self.size[0]/8) * self.world.zoom)

                pygame.draw.lines(self.world.screen, color, False, orbitPoints, offsetZoom)

    