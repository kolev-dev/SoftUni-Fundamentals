class Shape:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

class Parallelogram(Shape):
    def area(self):
        return self.a * self.h

class Trapezoid(Shape):
    def area(self):
        return (self.a + self.b) * self.h

argument_a = 5
argument_b = 3
argument_h = 1

shapes_list = [Trapezoid(argument_a,argument_b,argument_h), Parallelogram(argument_a,argument_b,argument_h)]


for shape in shapes_list:
    print(shape.area())


