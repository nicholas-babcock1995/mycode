#!/usr/bin/python3
import sys, pygame
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()
pygame.display.init()


gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()