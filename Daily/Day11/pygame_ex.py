import pygame
#do some setup
from time import sleep
from pygame.draw import rect as draw_rect

pygame.init()
WIDTH = 400
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

running = True

class MyRect():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 5
        self.y_speed = -5
        self.width = 100
        self.height = 100
    def draw(self, screen):
        draw_rect(screen, (0,0,255), (self.x,self.y,self.width,self.height))
    def update(self):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed
        if self.x + self.width> WIDTH or self.x < 0: #right and left
            self.x_speed = self.x_speed * -1

        if self.y + self.height> HEIGHT or self.y < 0: #bottom, top
            self.y_speed = self.y_speed * -1


my_rect_obj = MyRect(200,308) #makes myrect a defined object
all_rects = [my_rect_obj]
#while loop that holds main logic of the game
while running:
#   #draw everything that needs to be drawn
    screen.fill("white")
    for rect in all_rects:
        rect.draw(screen) #def draw
    pygame.display.flip()
#   #process any events that have happened
    events = pygame.event.get()
    if len(events)>0:
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = event.pos
                all_rects.append(MyRect(pos[0],pos[1]))
#   #update the state of the game
    for rect in all_rects:
        rect.update()
#   #check if done

    clock.tick(60)
#cleanup
pygame.quit()
