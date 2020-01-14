import sys
import pygame

from game import player

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FPS = 30

class Main:
    """The entry point of the project"""

    def __init__(self):
        """Initialize the assembly class and provides the container for the IoC container"""
        pygame.init()
        fps_clock = pygame.time.Clock()

        screen = pygame.display.set_mode((800, 600), 0, 32)
        pygame.display.set_caption("Tutorial")

        self.first = player.Player(screen, (20, 20))
        self.first.direction = [0, 0]
        self._execute(screen, fps_clock)

    def _execute(self, screen, clock):
        while True:
            screen.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    try:
                        self.first.direction = self._mapKey(event.key)
                    except Exception:
                        continue
                if event.type == pygame.KEYUP:
                    try:
                        self.first.direction = self._mapKeyRelease(event.key)
                    except Exception:
                        continue

            # up -> 273
            # down -> 274
            # left -> 276
            # right -> 275
            self.first.move(self.first.direction, 2)
            self.first.draw()
            pygame.display.update()
            clock.tick(FPS)

    def _mapKey(self, key):
        return {
            273: [self.first.direction[0], -1],
            274: [self.first.direction[0], 1],
            275: [1, self.first.direction[1]],
            276: [-1, self.first.direction[1]]
        }[key]

    def _mapKeyRelease(self, key):
        return {
            273: [self.first.direction[0], 0],
            274: [self.first.direction[0], 0],
            275: [0, self.first.direction[1]],
            276: [0, self.first.direction[1]]
        }[key]


if __name__ == "__main__":
    Main()
