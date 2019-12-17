"""
    ************************
    Andres Trujillo
    December 6, 2019
    Python3.6
    Ubuntu Linux Server 4.15
    docs.python.org/3/library/functions.html#super
    realpython.com/python-super
    ************************
"""
"""
DEFINITION:
    super() alone returns a temporary object of the superclass 
    that then allows you to call that superclass's methods.

COMMON USE CASE:
        Building classes that extend the functionality of
        previously built classes.

        Calling the previously built methods with super()
        saves you from needing to rewrite those methods
        in your sublcass and allows you to swap out the 
        superclasses with minimal code changes.
"""

#super() in Single Inheritance

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width =width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*self.length+2*self.width
class Square:
    def __init__(self,length):
        self.length = length
    def area(self):
        return self.length*self.length
    def perimeter(self):
        return 4*self.length
#driver code
square= Square(4)
square.area()

rectangle=Rectangle(2,4)
rectangle.area()
"""
    In this example, you have two shapes that related to each other:
    A square is a special kind of rectangle. The code, however doesnt
    reflect that relationship and thus has code that is essentially repeated.

    INHERTIANCE!!!!!!!!!!!
    By using inheritance, you can reduce the amount of code you write while 
    simultaneously reflecting the real-world relationship between rectangles
    and squares.


    FOR EXAMPLE:

"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
    def pertimeter(self):
        return 2*self.length+2*self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(Self, length):
        super().__init__(length,length)
"""
    Super() in single inheritance

    It allows you to call methods of the superclass in your subclass. The
    primary use case of this is to extend the functionality of the
    inherited method.

    Creating a class Cube that inherits from Square and extends the
    functionality of .area() (inherited from the Rectangle class though
    Square) to calculate the surface are and volume of a Cube instance.



    Implemented two methods for the Cube clas: surface area and volume
    These calculations rely on calculating the area of a single face
    Rather than reimplementing the area calculate, I used super()
    to extend the area calculation.

    My Cube class definition does not have an __init__() method
    because Cube inherits from Square and __init__() method
    doesnt do anything differently for CUbe than it already does
    for Square, I skip defining it and the __init__() method
    of the superclass(square) will be called automatically.

    super() returns a delegate object to a parent class,
    so you call the method you want directly on it: super().area()

    This saves me from having to reqrite the area calculations , but
    it also allows us to change the internal .area() logic in a single location.
    Very handy when you have a number of subclasses inheriting from one
    superclass.


"""
class Square(Rectangle):
    def __init__(self,length):
        super().init__(length,length)
class Cube(Square):
    def surface_are(self)_:
        face_area = super().area()
        return face_area*6
    def volume(self):
        face_area = super().area()
        return face_area*self.length
# Driver code
cube = Cube(3)
cube.surface_area()
cub.volume()
































