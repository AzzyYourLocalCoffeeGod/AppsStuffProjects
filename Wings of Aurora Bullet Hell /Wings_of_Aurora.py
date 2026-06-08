import pygame
import math
import random
import time
import sys

pygame.init()
pygame.mixer.init()

W,H = 1000, 700 
screen = pygame.display.set_mode((W, H)) 
pygame.display.set_caption("Covenant Bullet Symphony - Wings of Aurora")
Clock = pygame.time.Clock()

AURUM = (255, 215, 0)
SAPPHIRE = (10, 30, 100)
SHADOWFIRE = (200, 0, 255)
CRYSTAL = (220, 255, 255)
SUN = (255, 240, 120)
ABYSS = (5, 0, 30)
VEIL = (80, 80, 100)
WHITE = (255, 255, 225)

font_big = pygame.font.Font(None, 80)
font_med = pygame.font.Font(None, 50)
font_small = pygame.font.Font(None, 32)

class Azrael:
 def __init__(self):
     self.x = W//2
     self.y = H-100
     self.speed = 9
     self.size = 18
     self.lives = 9
     self.bombs = 3
     self.upgrades = []

def update(self):
        
    keys = pygame.keys_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]: self.x -= self.speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]: self.x += self.speed
    if keys[pygame.K_UP] or keys[pygame.K_w]: self.y -= self.speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]: self.y += self.speed

    self.x = max(self.size, min(W - self.size, self.x))
    self.y = max(self.size,min(H - self.size, self.y))
    

    def draw(self):
        pygame.draw.circle(screen, AURUM, (self.x,self.y), self.size)
        if "lunareth" in self.upgrades:
            pygame.draw.circle(screen, SAPPHIRE, (self.x, self.y), self.size + 25, 5)

    player = Azrael()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()
    screen.fill(BLACK)
    player.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
                                    
