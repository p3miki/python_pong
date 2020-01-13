import pygame, sys
from pygame import gfxdraw

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
FPS = 30

def init():
  pygame.init()
  fpsClock = pygame.time.Clock()

  screen = pygame.display.set_mode((400, 300), 0, 32)
  pygame.display.set_caption("Tutorial")
  execute(screen, fpsClock)

def execute(screen, clock):
  direction = "right"
  first = [False, False, False, False]
  posX = 20
  posY = 20

  screen.fill(WHITE)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit(0)
      if event.type == pygame.KEYDOWN:
        print(event)
      if event.type == pygame.KEYUP:
        print(event)
    
    pygame.display.update()
    clock.tick(FPS)

if __name__ == "__main__":
  init()
