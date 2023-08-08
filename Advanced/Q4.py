"""Define a class named Shape and its subclass Square. The Square
class has an init function which takes length as argument. Both
classes have an area function which can print the area of the
shape where Shape’s area is 0 by default.
"""


class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, len):
        Shape.__init__(self)
        self.length = len

    def area(self):
        return self.length*self.length

aSqre= Square(5)
print(aSqre.area())