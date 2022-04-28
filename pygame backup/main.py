import pygame
from entities import Bullet

pygame.init()

# Screen 
sWidth = 800
sHeight = 700
                           #    ((width,height))
screen = pygame.display.set_mode((sWidth,sHeight))

# Title and Logo
pygame.display.set_caption("PyGame Test")
icon = None

# pygame.set_icon(icon)

# Player 
# For images [width, height]
playerImg = pygame.image.load(r"ursina-project\ursina-project\pygame backup\pythonPygameTest.png")
playerImg = pygame.transform.scale(playerImg, (100, 100))

pWidth, pHeight = playerImg.get_size()
playerX = (sWidth / 2) - pWidth / 2
playerY = sHeight - pHeight - 50

deltaX = 0.3
deltaY = 0.3

bulletSpeed = 0.01

def player(x, y):
    screen.blit(playerImg, (playerX, playerY))

# Main Game Loop
run = True
while run:
    bullets = []
    screen.fill((255,0,0))
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    if keys[pygame.K_DOWN] and playerY + pHeight < sHeight:
        playerY += 1
    if keys[pygame.K_UP] and playerY > 0:
        playerY -= 1
    if keys[pygame.K_LEFT] and playerX > 0:
        playerX -= 1
    if keys[pygame.K_RIGHT] and playerX + pWidth < sWidth:
        playerX += 1
    

    player((sWidth / 2) + pWidth / 2, (sHeight) - pHeight)
    pygame.display.update()