import turtle
import random
"""
turtle.speed(500)


turtle.teleport(-50,50)
turtle.circle(50)
turtle.teleport(50,50)
turtle.circle(50)

turtle.teleport(-100,-100)

while True:
    turtle.teleport(random.randint(-100,100),random.randint(-100,100))
    turtle.forward(random.randint(-200,200))
    turtle.left(50)

turtle.done()
"""
turtle.speed(50)

class Star():
    def __init__(self,x,y):
        self.xcoord = x
        self.ycoord = y
        self.size = random.randint(9,14)
        self.color = random.choice(["red", "white", "blue"])

    def draw(self):
        turtle.penup()
        turtle.setpos(self.xcoord, self.ycoord)
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()



for i in range(10):
    stars = [
        Star(random.randint(-100,100), random.randint(-100,100))
    ]


for star in stars:
    star.draw()

turtle.done()
