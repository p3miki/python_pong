import sys
import pygame

class Player:
    def __init__(self, screen=None, position=(10, 0)):

        self.posx = position[0]
        self.posy = position[1]
        self.rect = pygame.Rect((self.posx, self.posy), (10, 30))
        self.screen = screen

        self.maxPos = self.screen.get_size()

    def move(self, direction, speed):
        self.posx += direction[0] * speed
        self.posy += direction[1] * speed

        self.exceptBoundaries()

        self.rect = pygame.Rect((self.posx, self.posy), (10, 30))

    def exceptBoundaries(self):
        if (self.posx < 0):
            self.posx = 0
        if (self.posy < 0):
            self.posy = 0
        if (self.posx + 10 > self.maxPos[0]):
            self.posx = self.maxPos[0] - 10
        if (self.posy + 30 > self.maxPos[1]):
            self.posy = self.maxPos[1] - 30

    def draw(self):
        if (not self.screen is None):
            pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 2)


if __name__ == "__main__":
    sys.exit(-1)
