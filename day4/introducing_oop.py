import sys


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


class Canvas:
    units = 'cm'

    def __init__(self, width, height, bg_colour='grey'):
        self.width = float(width)
        self.height = float(height)
        self.bg_colour = bg_colour

class Text:

    def __init__(self, position=(0,0), size=8, txt_colour='red'):
        self.position = position
        self.size = size
        self.txt_colour = txt_colour

def main():
    rectangle1 = Rectangle(5, 8)
    print(rectangle1.perimeter())
    print(rectangle1.area())
    print(rectangle1.diagonal())
    print(rectangle1.bounding_box())
    print(rectangle1)

    circle1 = Circle(5)
    print(circle1)

    return 0


if __name__ == '__main__':
    sys.exit(main())
