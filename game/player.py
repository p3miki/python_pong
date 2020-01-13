import sys
import pygame

class Player:
  def __init__(self, screen = None, position = (10,0)):
    self.INIT = True

    self.posX = position[0]
    self.posY = position[1]
    self.rect = pygame.Rect((self.posX, self.posY), (10, 30))
    self.screen = screen

    self.maxPos = self.screen.get_size()

  def move(self, direction, speed):
    self.posX += direction[0] * speed
    self.posY += direction[1] * speed

    self.exceptBoundaries()

    self.rect = pygame.Rect((self.posX, self.posY), (10, 30))

  def exceptBoundaries(self):
    if (self.posX < 0):
      self.posX = 0
    if (self.posY < 0):
      self.posY = 0
    if (self.posX + 10 > self.maxPos[0]):
      self.posX = self.maxPos[0] - 10
    if (self.posY + 30 > self.maxPos[1]):
      self.posY = self.maxPos[1] - 30

  def draw(self):
    if (not self.screen is None):
      pygame.draw.rect(self.screen, (0,0,0), self.rect, 2)

if __name__ == "__main__":
    sys.exit(-1)
