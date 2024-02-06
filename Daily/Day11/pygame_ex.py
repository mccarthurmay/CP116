# Do some setup;
import pygame
from time import sleep

from random import randint

from pygame.draw import rect as draw_rect

#setup:
WIDTH = 500
HEIGHT = 500
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

class MyRect():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 5
        self.y_speed = -5
        self.width = 100
        self.height = 100

    def draw(self, screen):
        draw_rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height) )

    def update(self):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed

        if self.x + self.width > WIDTH or self.x < 0:
            self.x_speed = self.x_speed * -1

        if self.y + self.height > HEIGHT or self.y < 0:
            self.y_speed = self.y_speed * -1

    def collide_pt(self,x,y):
        if self.x < x < self.x + self.width and self.y < y < self.y+self.height:
            return True
        else:
            return False

    def randomize(self):
        self.x_speed =0
        self.y_speed = 0

running = True

my_rect_obj = MyRect(200, 308)
all_rects = [my_rect_obj]

direction = []
# While loop that holds the main logic of the game
while running:
    # draw everything that needs to be drawn
    screen.fill("white")
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
                pos = event.pos
                all_rects.append(MyRect(pos[0], pos[1]))
                for rect in all_rects:
                    if rect.collide_pt(pos[0], pos[1]):
                        rect.randomize()

#      update the state of our game
    for rect in all_rects:
        rect.update()

#create a list of all directions
#avg of list
#move away from average


#      check if we're done
    clock.tick(60)

# cleanup
pygame.quit()
