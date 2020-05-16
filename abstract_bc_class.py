# abstract base class
from abc import ABC, abstractmethod

#abstract base class -->we can not make the object of abstract of base class
class Shape(ABC):
    @abstractmethod  # we have to implement this method in all classes
    def print_area(self):
        return 0


class Rectangle(Shape):
    type = 'Rectangle'
    sides = 4

    def __init__(self, l, b):
        self.lenght = l
        self.breadth = b

    def print_area(self):
        return self.lenght * self.breadth


a = Rectangle(10, 20)
print(a.print_area())
