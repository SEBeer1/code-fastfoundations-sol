import sys
import turtle


def draw_rectangle():
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(10)


def draw_circle():
    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
    pen.goto(15, 28)
    pen.down()
    pen.begin_fill()
    pen.pencolor("red")
    pen.fillcolor("purple")
    pen.circle(60)
    pen.end_fill()
    pen.up()

def draw_triangle():
    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
    pen.goto(50,50)
    pen.down()
    pen.begin_fill()
    pen.pencolor('blue')
    pen.fillcolor('pink')
    pen.forward(30)
    pen.right(120)
    pen.forward(30)
    pen.right(120)
    pen.forward(30)
    pen.end_fill()
    pen.up()

def draw_pentagon():
    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
    pen.goto(120,120)
    pen.down()
    pen.begin_fill()
    pen.pencolor('blue')
    pen.fillcolor('pink')
    for i in range(5):
        pen.forward(50)
        pen.right(72)
    pen.end_fill()
    pen.up()

def write_text():
    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
    pen.goto(-123, -123)
    pen.down()
    pen.pencolor('blue')
    pen.write('Am i a turtle 훈민정음')
    pen.up()




def main():

    draw_rectangle()
    draw_circle()
    draw_triangle()
    draw_pentagon()
    write_text()
    turtle.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
