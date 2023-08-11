import pygame
from object import *


class Planet(Object):

    def __init__(self, world, name, startingPosition, mass, size = 50, color = None, velocity = [0, 0], showOrbit = False, gravitationalField = True, affectedByGravity = True, isSphere = True):

        super().__init__(world, startingPosition, mass, size, color, velocity, showOrbit, gravitationalField, affectedByGravity, isSphere)
        self.name = name

    def update(self):
        self.updateOrbit()
        self.renderOrbit()
        self.render()
        self.applyGravity()
        self.applyForce()
        self.updatePosition()


    def render(self):

        offsetX = (self.position[0] + self.world.position[0]) * self.world.zoom
        offsetY = (self.position[1] + self.world.position[1]) * self.world.zoom
        offsetZoom = self.radius * self.world.zoom
        pygame.draw.circle(self.world.screen, self.color, [offsetX, offsetY], offsetZoom)