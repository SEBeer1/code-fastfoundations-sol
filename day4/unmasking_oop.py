import math
import os
import sys


class Circle:
    units = 'cm'  # all circles will have the same units

    def __init__(self, radius, position=(0, 0), fill='white', stroke='black'):
        self.radius = radius  # each circle will have a particular radius
        self.position = position
        self.diameter = 2 * radius
        self.fill = fill
        self.stroke = stroke
        #self.area = math.pi * radius ** 2

    def __str__(self):  # Python special methods
        return f"I am a circle of size {self.radius}{self.units} located at {self.position}."


    def area(self):
        return math.pi * self.radius ** 2

    def perimiter(self):
        return math.pi * 2 * self.radius

    def arc_length(self, theta, degrees=False):
        if degrees==False:
            return theta * self.radius
        else:
            return theta * (1/180) * math.pi * self.radius

    def bounding_box(self):
        coords = (self.position[0] - self.radius, self.position[0] + self.radius,
                  self.position[1] - self.radius, self.position[1] + self.radius)
        return coords


def main():
    small_circle = Circle(10)
    big_circle = Circle(50)
    small_circle.position = (20,32)

    print(small_circle)
    print(big_circle)

    # now we change units for all instances on the class
    Circle.units = 'pm'

    print(small_circle)
    print(big_circle)

    # but
    big_circle.units = 'hm'  # only change for the big_circle instance

    print(small_circle)
    print(big_circle)

    print(big_circle.area)
    print(big_circle.diameter)

    #print(bounding_box(small_circle))
    #print(arc_length(small_circle, math.pi))
    #print(arc_length(small_circle, 180, degrees=True))

    #canvas = canvas(1200, 780)
    #canvas.mystery_method()
    #turtle.done()

    print(big_circle.area())
    print(big_circle.perimiter())
    print(big_circle.arc_length(math.pi))
    print(big_circle.bounding_box())

    return os.EX_OK


if __name__ == '__main__':
    sys.exit(main())
