
import pygame, time
pygame.display.init()
canvas = pygame.display.set_mode((800,240),pygame.FULLSCREEN)
img = pygame.image.load("res/kitten.png")

for x in range(-50,300):
canvas.blit(img,(x*3,80))
pygame.display.update()

pygame.display.quit()
