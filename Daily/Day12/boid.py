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

all_boids = [Boid(randint(200,600), randint(200,600)) for i in range(50)] #changed range to 50 for plot to run faster
import time
import matplotlib.pyplot as plt
overall_times = []
while running:          #loops while running

    overall_start = time.time()
    #start first loop timer
    #start_loop1 = time.time()

    screen.fill("dark grey")
    for boid in all_boids:          #O(N), first for loop
        boid.draw(screen)

    #after the loop is exited, stop time
    #end_loop1 = time.time()
    #print("first loop")
    #print(end_loop1 - start_loop1)

    pygame.display.flip()
    events = pygame.event.get()


    #start second loop timer
    #start_loop2 = time.time()

    if len(events) > 0:
        for event in events:            #O(N), first for loop within for loop  (Now, O(N^2) total)

            if event.type == pygame.QUIT:
                running=False
            elif event.type == pygame.MOUSEBUTTONDOWN:      #+ O(C) for number of times mouse clicked (O(N^2 + C + U))
                pos = event.pos
                all_boids.append(Boid(pos[0], pos[1]))

                #after the 2nd loop is exited, stop time
                #end_loop2 = time.time()
                print("Second loop")
                #print(end_loop2 - start_loop2)

    #start third loop timer
    #start_loop3 = time.time()


    for boid in all_boids:      #O(U), second for loop
        boid.update(all_boids)


    #after the 3rd loop is exited, stop time
    #end_loop3 = time.time()
    #print("Third loop")
    #print(end_loop3 - start_loop3)
    overall_stop = time.time()
    print("All loops")
    overall = (overall_stop - overall_start)
    print(overall)

    overall_times.append(overall_stop - overall_start)

    clock.tick(50) #changed tick to have plot run faster
plt.plot(overall_times)
plt.xlabel('Iteration')
plt.ylabel('Overall Time (seconds)')
plt.title('Overall Time per Iteration')
plt.show()
#The predicted complexity O(N) + O(C) + O(U).

#O(N^2) is the number of boids there are (first loop), then for each boid the code also reads each event.
 #Realistically, this is far less than O(N^2) and closer to O(N) as
 #the user is not usually clicking or quitting the pygame window.

#Since we are saying that we have O(N), we can account for the clicking action as O(C), whereas this will be added
 #not multiplied.

#Finally, we have one more loop that loops through all boids and updates the boid's position. This occurs O(U) times as it is
 #separate from all other loops. Note* O(U)>O(N)>O(C)

#After measuring times (at 1 tick per second, 1000 boids), here are my results:
#   - First 'for': .0014 seconds with 1000 boids
#   - Second 'for': adds .00099 seconds for each click
#   - Third 'for': adds .57379 seconds to update (drops as boids spread)
#   - Overall timer: .57 - .58 idle, but drops about .002 per tick as boids spread out.
        # - adds .025 after first click but immediately drops .01 and continues dropping until it reaches idle and drops at lower speeds.

#So, O(N) = .0014, O(C) = .00099, and O(U) = .57379. This checks out with my last little note saying taht U>N>C. This information also agrees that
# O(N) is not squared as the second for loop is rarely ran.


#PLOT#
#I changed the tick value and boid number to compare how "clicking" affects the time. After a few different trials, at 50 boids

pygame.quit()
