import sys
import math
import turtle

class Triangle:
    units = 'cm'

    def __init__(self, length, position=(0, 0), fill='white', stroke='black'):
        self.length = float(length)
        self.position = position
        self.fill = fill
        self.stroke = stroke

    def __str__(self):
        return f"This is a triangle i hope"

    def draw(self, pen):

        if pen.isdown():
            pen.up()
        pen.goto(self.position)
        pen.down()
        pen.begin_fill()
        pen.pencolor(self.stroke)
        pen.fillcolor(self.fill)
        pen.forward(self.length)
        pen.right(120)
        pen.forward(self.length)
        pen.right(120)
        pen.forward(self.length)
        pen.end_fill()
        pen.up()

class Rectangle:
    units = 'cm'

    def __init__(self, width, height, position=(0, 0), fill='white', stroke='black'):
        self.width = float(width)
        self.height = float(height)
        self.position = position
        self.fill = fill
        self.stroke = stroke

    def __str__(self):
        return f"I am a rectangle with {self.width}{self.units} width, and {self.height}{self.units} height."

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height

    def diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def bounding_box(self):
        coords = (self.position[0] - self.width / 2, self.position[0] + self.width / 2,
                  self.position[1] - self.height / 2, self.position[1] + self.height / 2)
        return coords
    def draw(self, pen):
        if pen.isdown():
            pen.up()
        pen.goto(self.position)
        pen.down()
        pen.begin_fill()
        pen.pencolor(self.stroke)
        pen.fillcolor(self.fill)
        pen.forward(self.width)
        pen.right(90)
        pen.forward(self.height)
        pen.right(90)
        pen.forward(self.width)
        pen.right(90)
        pen.forward(self.height)
        pen.end_fill()
        pen.up()
        pen.home()

class Square(Rectangle):
    def __init__(self, width, *args, **kwargs):
        super().__init__(width, width, *args, **kwargs)

    def __str__(self):
        return f"I am a square of width {self.width}{self.units}."



class Circle:
    units = 'cm'  # all circles will have the same units

    def __init__(self, radius, position=(0, 0), fill='white', stroke='black'):
        self.radius = radius  # each circle will have a particular radius
        self.position = position
        self.diameter = 2 * radius
        self.fill = fill
        self.stroke = stroke
        # self.area = math.pi * radius ** 2

    def __str__(self):  # Python special methods
        return f"I am a circle of size {self.radius}{self.units} located at {self.position}."

    def area(self):
        return math.pi * self.radius ** 2

    def perimiter(self):
        return math.pi * 2 * self.radius

    def arc_length(self, theta, degrees=False):
        if degrees == False:
            return theta * self.radius
        else:
            return theta * (1 / 180) * math.pi * self.radius

    def bounding_box(self):
        coords = (self.position[0] - self.radius, self.position[0] + self.radius,
                  self.position[1] - self.radius, self.position[1] + self.radius)
        return coords
    def draw(self, pen):
        if pen.isdown():
            pen.up()
        pen.goto(self.position)
        pen.down()
        pen.begin_fill()
        pen.pencolor(self.stroke)
        pen.fillcolor(self.fill)
        pen.circle(self.radius)
        pen.end_fill()
        pen.up()

class Canvas(turtle.TurtleScreen):
    units = 'cm'

    def __init__(self, width, height, bg_c='grey', canvas=turtle.getcanvas()):

        super().__init__(canvas)
        self.screensize(width, height, bg_c)
        self.pen = turtle.RawPen(canvas)
        self.width = float(width)
        self.height = float(height)
        self.bg_c = bg_c

    def __str__(self):
        return f"We have presumably created a canvas"

    def draw(self, shape):
        shape.draw(self.pen)

    def write(self, text, *args, **kwargs):
        text.write(self.pen, *args, **kwargs)

    def make_cross(self):
        self.pen.up()
        self.pen.goto(0, self.height / 2)
        self.pen.down()
        self.pen.goto(0, -self.height / 2)
        self.pen.up()
        self.pen.goto(-self.width / 2, 0)
        self.pen.down()
        self.pen.goto(self.width / 2, 0)
        self.pen.up()
        self.pen.home()

    def draw_circle(self, radius, position=(0,0), pen_c="red", fill_c="pink"):
        if self.pen.isdown():
            self.pen.up()
        self.pen.goto(position)
        self.pen.down()
        self.pen.begin_fill()
        self.pen.pencolor(pen_c)
        self.pen.fillcolor(fill_c)
        self.pen.circle(radius)
        self.pen.end_fill()
        self.pen.up()

    def draw_rectangle(self, width, height, position=(0, 0), pen_c="red", fill_c="pink"):
        if self.pen.isdown():
            self.pen.up()
        self.pen.goto(position)
        self.pen.down()
        self.pen.begin_fill()
        self.pen.pencolor(pen_c)
        self.pen.fillcolor(fill_c)
        self.pen.forward(width)
        self.pen.right(90)
        self.pen.forward(height)
        self.pen.right(90)
        self.pen.forward(width)
        self.pen.right(90)
        self.pen.forward(height)
        self.pen.end_fill()
        self.pen.up()

class Text:

    def __init__(self, text, position=(0, 0), txt_colour='red'):
        self.position = position
        self.txt_colour = txt_colour
        self.text = text

    def write(self, pen, align='center', font=('Arial', 8, 'normal')):
        if pen.isdown():
            pen.up()
        pen.goto(self.position)
        pen.down()
        pen.pencolor(self.txt_colour)
        pen.write(self.text, font=font, align=align)
        pen.up()


def main():
    # rectangle1 = Rectangle(5, 8)
    # print(rectangle1.perimeter())
    # print(rectangle1.area())
    # print(rectangle1.diagonal())
    # print(rectangle1.bounding_box())
    # print(rectangle1)
    #
    # square1 = Square(5)
    # print(square1.area())
    # print(square1.bounding_box())
    # print(square1.diagonal())
    # print(square1)
    # print(square1.stroke)
    #
    # circle1 = Circle(5)
    # print(circle1)


    #the positions aren't working, have two positions, one in class and one in draw
    # canvas1 = Canvas(1200, 750)
    # print(canvas1.height)
    # print(canvas1)
    # print(canvas1.make_cross())
    # print(canvas1.draw_circle(50))
    # print(canvas1.draw_rectangle(80, 40, position=(100, 100)))
    # print(canvas1.draw(Circle(50)))
    # print(canvas1.draw(Rectangle(100, 300)))
    # print(canvas1.draw(Square(200, position=(-200, 50))))
    # print(canvas1.draw(Triangle(80, position=(100, -50))))
    #
    # print(canvas1.write(Text("Am i a turtle 훈민정음")))

    canvas = Canvas(1000, 700)
    gquad = Rectangle(
        200, 300, fill='#009a44', stroke='white', position=(-200, 0)
    )
    wquad = Rectangle(
        200, 300, fill='white', stroke='#dddddd', position=(0, 0)
    )
    oquad = Rectangle(
        200, 300, fill='#ff8200', stroke='white', position=(200, 0)
    )
    text = Text('IRELAND', position=(100, -400))
    canvas.draw(gquad)
    canvas.draw(wquad)
    canvas.draw(oquad)
    canvas.write(text, align='center', font=('Arial', 60, 'bold'))

    turtle.done()

    return 0


if __name__ == '__main__':
    sys.exit(main())
