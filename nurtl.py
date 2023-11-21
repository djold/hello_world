import turtle

screen = turtle.getscreen()
q = turtle.Turtle()

class Rect:

    w = 1222
    def __init__(self, size, fill) -> None:
        self.size = size
        print('был сщзданобеукт')
        print(self)
        self.fill = fill

    def draw(self, x, y, color):
        q.goto(x, y)
        q.color(color)
        q.begin_fill()
        for i in range (4):
            q.forward(self.size)
            q.left(90)
        q.end_fill()
        
rectanglle = Rect(40, fill=True)




print(rectanglle.size)
rectanglle.draw(50,80,"red")
rectanglle.draw(50,40,"yellow")
rectanglle.draw(50,0,"green")















screen.mainloop()