# Do some setup;
import pygame
from time import sleep

import random
from random import randint
from pygame.draw import rect as draw_rect

#setup:
WIDTH = 800
HEIGHT = 800
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

class MyRect():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 5
        self.y_speed = -5
        self.width = 50
        self.height = 50
        self.color = (0,0,255)

    def draw(self, screen):
        draw_rect(screen, self.color, (self.x, self.y, self.width, self.height) )

    def update(self):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed

        if self.x + self.width > WIDTH or self.x < 0:
            self.x_speed = self.x_speed * -1

        if self.y + self.height > HEIGHT or self.y < 0:
            self.y_speed = self.y_speed * -1

        #if self.x + self.width == first_rect

    def collide_pt(self,x,y):
        if self.x < x < self.x + self.width and self.y < y < self.y+self.height:
            return True
        else:
            return False
    def collide_rect(self, sec_rect):
        if self.x < sec_rect.x + sec_rect.width and self.x + self.width > sec_rect.x and self.y < sec_rect.y + sec_rect.height and self.y + self.height > sec_rect.y:
            return True
        else:
            return False
        #def collide_rect(self, other_rect):
    #    if self.x <

    def randomize(self):
        self.x_speed = randint(-5,5)
        self.y_speed = randint(-5,5)

    def bounce_first(self):
        self.x_speed = randint(-8,-1)
        self.y_speed = randint(-8,-1)
        self.color = (randint(0,255), randint(0,255) ,randint(0,255) )
        self.width = self.width - random.uniform(0,1)
        self.height = self.height -random.uniform(0,1)
    def bounce_second(self):
        self.x_speed = randint(1,8)
        self.y_speed = randint(1,8)
        self.color = (randint(0,255), randint(0,255) ,randint(0,255) )
        self.width = self.width + random.uniform(0,.75)
        self.height = self.height + random.uniform(0,.75)


running = True

my_rect_obj = MyRect(200, 308)
all_rects = [my_rect_obj]
color = "white"
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
fps =  int(input("What would you like your fps to be: "))
# While loop that holds the main logic of the game
while running:
    # draw everything that needs to be drawn
    screen.fill(color)
    for rect in all_rects:
        rect.draw(screen)
    pygame.display.flip()

    #process any events that have happened
    events = pygame.event.get()
    if len(events) > 0:
        for event in events:
            # check if the user closed the window
            if event.type == pygame.QUIT:
                running=False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("Number of squares:" , len(all_rects))
                print("FPS:", int(clock.get_fps()))
                pos = event.pos
                for i in range(0,5):
                    all_rects.append(MyRect(pos[0], pos[1]))

                for rect in all_rects:
                    if rect.collide_pt(pos[0], pos[1]):
                        rect.randomize()

            #adds a numb
    for i, first_rect in enumerate(all_rects):
        for k, sec_rect in enumerate(all_rects):
            if i != k and first_rect.collide_rect(sec_rect):
                first_rect.bounce_second()
                sec_rect.bounce_first()

#      update the state of our game
    for rect in all_rects:
        rect.update()

#create a list of all directions
#avg of list
#move away from average

#      check if we're done

    clock.tick(fps)

# cleanup
pygame.quit()
