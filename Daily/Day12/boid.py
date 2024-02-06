# Do some setup;
import pygame
from time import sleep

from random import randint

from pygame.draw import rect as draw_rect
from pygame.draw import line as draw_line
from pygame.draw import circle as draw_circle

#setup:
WIDTH = 800
HEIGHT = 800
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

class Boid():

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.dx = randint(-5,5)
        self.dy = randint(-5,5)
        self.size = 15
        self.color = (30,120,255)

    def draw(self, screen):
        boid_dir_x = 1
        boid_dir_y = 1
        draw_circle(screen, self.color, [self.x * boid_dir_x, self.y * boid_dir_y], self.size)
        draw_line(screen, self.color, [self.x, self.y], [self.x+5*self.dx, self.y + 5*self.dy], self.size )


    def update(self):

        self.x = self.x + self.dx *  boid_dir_x
        self.y = self.y + self.dy *  boid_dir_y

        if self.x + self.size > WIDTH or self.x < 0:
            self.dx = self.dx + boid_dir_x * -1

        if self.y + self.size > HEIGHT or self.y < 0:
            self.dy = self.dy + boid_dir_y * -1


running = True

boid_1 = Boid(200, 308)
all_boids = [boid_1]

boid_direction_x = []
boid_direction_y = []

# While loop that holds the main logic of the game
while running:
    # draw everything that needs to be drawn
    screen.fill("dark grey")
    for boid in all_boids:
        boid.draw(screen)
    pygame.display.flip()
    #process any events that have happened
    events = pygame.event.get()
    if len(events) > 0:
        for event in events:
            # check if the user closed the window
            if event.type == pygame.QUIT:
                running=False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                all_boids.append(Boid(pos[0], pos[1]))
#      update the state of our game


    for boid in all_boids:
        boid_direction_x.append(boid.dx)
        boid_direction_y.append(boid.dy)
        boid_dir_x = (sum(boid_direction_x) / len(boid_direction_x))
        boid_dir_y = ( sum(boid_direction_y) / len(boid_direction_y))
        if boid_dir_x > 0:
            boid_dir_x = boid_dir_x + 0.5
        elif boid_dir_x < 0:
            boid_dir_x = boid_dir_x - 0.5
        if boid_dir_y > 0:
            boid_dir_y = boid_dir_y + 0.5
        elif boid_dir_y < 0:
            boid_dir_y = boid_dir_y - 0.5
        print (boid_dir_x)
        print (boid_dir_y)
    for boid in all_boids:
        boid.update()









#      check if we're done
    clock.tick(60)

# cleanup
pygame.quit()
