import pygame
class Bullet:
    def __init__(self, bWidth, bHeight, speed, playerX, playerY, pWidth, screen):
        self.bWidth, self.bHeight = bWidth, bHeight
        self.speed = speed
        self.x = playerX + pWidth / 2
        self.y = playerY
        self.bulletShape = None
        self.screen = screen

    def initRectangle(self):
        self.bulletShape = pygame.draw.rect(self.screen, "blue", pygame.Rect((self.x, self.y), (self.bWidth, self.bHeight)))

    