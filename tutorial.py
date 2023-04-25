import pygame
import pymunk
import pymunk.pygame_util # this sets up pygame to draw for pymunk
import math

pygame.init()

WIDTH, HEIGHT = 500, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))  # this sets up the window to view what is going on

def run(window, width, height):
    run = True
    clock = pygame.time.Clock  # dictates the speed at which the simulation runs

    while run:
        clock.tick(60)