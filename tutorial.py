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
    fps = 60 # frames per second

    # for pymunk, you need to create a space
    space = pymunk.Space()  # this is where we put all our objects
    space.gravity = (0, 981) # gravity for both x and y direction

    while run:
        for event in pygame.event.get(): # this is for any and all pygame events
            if event.type == pygame.QUIT:  # these enables us to turn the sim off by breaking out of the for loop
                run = False
                break

        clock.tick(fps) # regulates the speed

    pygame.quit() # if we fall out of the while loop above, we will (obviously) want to quit.

# to call the run function
if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)

