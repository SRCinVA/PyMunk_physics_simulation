from turtle import position
import pygame
import pymunk
import pymunk.pygame_util # this sets up pygame to draw for pymunk
import math

pygame.init()

WIDTH, HEIGHT = 500, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))  # this sets up the window to view what is going on

def draw(space, window, draw_options): # to manually draw the items in the space
    window.fill("white") # clear the window by filling out the entire screen
    space.debug_draw(draw_options)
    pygame.display.update()

def create_ball(space, radius, mass):
    body = pymunk.Body()
    body.position = (300,300)
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (255, 0, 0, 100)  # rgb color plus opacity measure
    space.add(body, shape) # thsi actually adds teh shape to the sim
    return shape

def create_boundaries(space, width, height):
    rects = [ # here we define the rectangles we'll draw onto the screen
            # x and y position of the (a) center of the rectangle and (b) the width and height
        [(width/2, height - 10), (width, 20)],  # height - 10 so it's flush at the bottom of the screen
        [(width/2, 10), (width, 20)], # don't understand why this is just 10
        [(10, height/2), (20, height)], # not following this ...
        [(width - 10, height/2), (20, height)]
    ]

    for pos, size in rects: # this is how we draw the rectangles
        body = pymunk.Body(body_type=pymunk.Body.STATIC) # we want this to not move
        body.position = pos # after creating the body, then we need to posiiton it
        shape = pymunk.Poly.create_box(body, size)
        space.add(body, shape)

def run(window, width, height):
    run = True
    clock = pygame.time.Clock() # dictates the speed at which the simulation runs
    fps = 60 # frames per second
    dt = 1 / fps # "delta time," this is so that you sync up the clock with how frequently the simulation runs

    # for pymunk, you need to create a space
    space = pymunk.Space()  # this is where we put all our objects
    space.gravity = (0, 981) # gravity for both x and y direction

    ball = create_ball(space, 30, 10)
    create_boundaries(space, width, height)

    draw_options = pymunk.pygame_util.DrawOptions(window) # we pass in the pygame window as a surface to draw on

    while run:
        for event in pygame.event.get(): # this is for any and all pygame events
            if event.type == pygame.QUIT:  # these enables us to turn the sim off by breaking out of the for loop
                run = False
                break
        draw(space, window, draw_options) # need to call draw() here
        space.step(dt) # how fast you run the sim
        clock.tick(fps) # regulates the speed

    pygame.quit() # if we fall out of the while loop above, we will (obviously) want to quit.

# to call the run function
if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)

