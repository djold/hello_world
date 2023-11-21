import turtle

screen = turtle.getscreen()
t = turtle.Turtle()
 
class DrawShape:
    def draw(self, color='red'):
        if self.fill:
            t.color(color)
            t.begin_fill()
        for _ in range(self.sides):
            t.forward(self.size)
            t.left(self.angle)
        if self.fill:
            t.end_fill()
class Rect(DrawShape):
    def __init__(self, size, fill=False):
        self.size = size
        self.sides = 4
        self.angle = 90
        self.fill = fill

rect = Rect(100, fill=True)
rect.draw('red')






# t.color('red')
# t.begin_fill()
# t.circle(90)
# t.end_fill()

# for i in range(50):
#     t.forward(50)
#     t.left(170)
    # t.forward(50)
    # t.right(170)
# t.up()
# t.forward(100)
# t.goto(100,122)



screen.mainloop()




