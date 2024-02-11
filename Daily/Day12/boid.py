# Do some setup;
import pygame
from time import sleep
import random
from random import randint

from pygame.draw import rect as draw_rect
from pygame.draw import line as draw_line
from pygame.draw import circle as draw_circle

#setup:
WIDTH = 800
HEIGHT = 800
BOID_MAX_SPEED = 4
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()


class Boid():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = randint(-5,5)
        self.dy = randint(-5,5)
        self.size = 5
        self.color = (30,120,255)

    def draw(self, screen):
        draw_circle(screen, self.color, [self.x, self.y], self.size)
        draw_line(screen, self.color, [self.x, self.y], [self.x+self.dx, self.y + self.dy], self.size )

    def distance(self, other):
        # get the distance between ourself and some other boid
        return ((self.x - other.x)**2  +  (self.y  - other.y)**2)**.5

    def filter_boids(self, other_boids, R):
        # take in a list of other boids, and only return those that are
        # closer than R

        to_return = []
        for boid in other_boids:
            dist = self.distance(boid)
            if dist < R and boid != self:
                to_return.append(boid)
        return to_return

    def sep_dxdy(self, r1_boids):
        if len(r1_boids) > 0:
            sum_x = 0
            sum_y = 0
            for boid in r1_boids:
                sum_x += boid.x
                sum_y += boid.y

            avg_x = sum_x / len(r1_boids)
            avg_y = sum_y / len(r1_boids)

            return self.x-1*avg_x, self.y-1*avg_y

        else:
            return 0.0, 0.0

    def coh_dxdy(self, r2_boids):
        if len(r2_boids) > 0:
            boid_x = []
            boid_y = []

            for boid in r2_boids:
                boid_x.append(boid.x)
                boid_y.append(boid.y)

            avg_x = sum(boid_x) / len(boid_x)
            avg_y = sum(boid_y) / len(boid_y)

            return avg_x - self.x, avg_y - self.y

        else:
            return 0,0

    def ali_dxdy(self, r3_boids):
        if len(r3_boids) > 0:
            boid_x = []
            boid_y = []

            for boid in r3_boids:
                boid_x.append(boid.dx)
                boid_y.append(boid.dy)

            avg_x = sum(boid_x) / len(boid_x)
            avg_y = sum(boid_y) / len(boid_y)

            return avg_x, avg_y

        else:
            return 0,0





    def update(self, other_boids):

        # get boids that are "crowding us"
        # get boids that are just nearby
        neighbors = self.filter_boids(other_boids, 100)
        crowders = self.filter_boids(neighbors, 30)


        # get separation dx and dy
        sep_dx, sep_dy = self.sep_dxdy(crowders)
        # get cohesion dx and dy
        coh_dx, coh_dy = self.coh_dxdy(neighbors)
        # get alignment dx and dy
        ali_dx, ali_dy = self.ali_dxdy(neighbors)

        # new direction = sum of our current dx and dy with those from each rule
        self.dx += 1.5*sep_dx + .1*coh_dx + 2.0*ali_dx
        self.dy += 1.5*sep_dy + .1*coh_dy + 2.0*ali_dy

        total_speed = (self.dx**2 + self.dy**2)**.5
        if total_speed > BOID_MAX_SPEED:
            self.dx *= (BOID_MAX_SPEED/total_speed)
            self.dy *= (BOID_MAX_SPEED/total_speed)

        self.x = self.x + self.dx
        self.y = self.y + self.dy

        if self.x + self.size > WIDTH or self.x < 0:
            self.dx = self.dx * -1

        if self.y + self.size > HEIGHT or self.y < 0:
            self.dy = self.dy * -1


running = True

all_boids = [Boid(randint(200,600), randint(200,600)) for i in range(100)]
obstacles = []
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
                genObstacle()
                all_boids.append(Boid(pos[0], pos[1]))
#      update the state of our game
    for boid in all_boids:
        boid.update(all_boids)



#      check if we're done
    clock.tick(60)


# cleanup
pygame.quit()
