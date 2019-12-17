def add(x,y,z=0)
    return x + y + z

print(add(2,3))
print(add(2,3,4))

class Colombia():
    def capital(self):
        print("Bogota is the capital of Colombia")
    def language(self):
        print("Spanish")
    def type(self):
        print("Colombia is in South America")

class USA():
    def capital(self):
        print("Washington, DC")
    def language(self):
        print("English")
    def type(self):
        print("USA is North America")

obj_col = Colombia()
obj_usa = USA()
for country in (obj_col, obj_usa)
    country.capital()
    country.language()
    country.type()

# Poly with Inheritance
"""
In Python, Polymorphism lets us define methods
in the child class that have the same name as the methods in the parent class. In inheritance the child class
inherits the methods from the parents class. However , it is possible to modify a method in a child class that it has inherited from the parent class. This is particularly useful in cases where the method inherited from the
parent class doesnt quite fit the child class. In such cases, we re-implement the method in the child class. This process of re-implementing a method in the child class is known as Method Overriding

"""

class Bird:
    def intro(self):
        print("There are many types of birds")
    def flight(self):
        print("Most of the birds can fly")
class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly")
class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly")

objBird = Bird()
objSpr = sparrow()
objOst = ostrich()

objBird.intro()
objBird.flight()

objSpr.intro()
objSpr.flight()

objOst.intro()
objOst.flight()

"""
Polymorphism with a function and objects
Create a function that can take any object, allowing 
for polymorphism.
Create a function called func()
which will take an object which we will name 
object1

Though I used the name object1 any instantiated object will be able to be called into this function. 

Give the function something that will use my object1
passed to it from somewhere else.


Call three methods of capital language and type

"""
def func(objec1):
    object1.capital()
    object1.language()
    object1.type()
obj_col1 = Colombia()
obj_usa1 = USA()

func(obj_col1)
func(obj_usa1)

