import turtle
from random import randint

screen = turtle.getscreen()
w = turtle.Turtle(visible=False)

class Circle():
    def __init__(self, fill=False):
        self.fill =fill

    def draw (self, x, y, size, color):
        w.penup()
        w.goto(x, y)
        w.pendown()
        w.color(color)
        w.begin_fill()
        w.circle(size)
        w.end_fill()



class Rect:

    w = 1222
    def __init__(self, size, fill) -> None:
        self.size = size
        print('был сщзданобеукт')
        print(self)
        self.fill = fill

    def draw(self, x, y, color):
        w.goto(x, y)
        w.color(color)
        w.begin_fill()
        for i in range (4):
            w.forward(self.size)
            w.left(90)
        w.end_fill()

# sand = Rect(80, fill=True)

clip = Circle(fill = True)




# sand.draw(0, 0, "red")
# sand.draw(0 + sand.size, 0,"red")
# clip.draw(0, -35, 35, "black")

# clip.draw(0, -10, 10, "white")

# clip.draw(sand.size * 2, -35, 35, "black")

# clip.draw(sand.size * 2, -10, 10, "white")

clip.draw(0, -110, 110, "black")

clip.draw(0, -100, 100, "yellow")




for i in range(10):
    w.goto(0, 0)
    w.left(randint(0, 360))
    w.forward(randint(1, 100))
    clip.draw(w.pos()[0], w.pos()[1], 10, 'red')











screen.mainloop()