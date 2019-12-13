import turtle
import math
import random


turtle.bgcolor('black')
screen = turtle.Screen()
screen.screensize(2000,2000)

Johny = turtle.Turtle()
Johny.speed(0)
Johny.color('green')

Steve = turtle.Turtle()
Steve.speed(0)
Steve.color('white')

Barry = turtle.Turtle()
Barry.speed(0)
Barry.color('grey')

Terry = turtle.Turtle()
Terry.speed(0)
Terry.color('red')

Will = turtle.Turtle()
Will.speed(0)
Will.color('white')

Nich = turtle.Turtle()
Nich.speed(0)
Nich.color('red')


minus = random.randint(0,100)

while True:
 def drawCircles(t,size):
     for i in range(10):
         t.circle(size*1.02)
         size=size- minus+62
 def drawSpecial(t,size,repeat):
   for i in range (repeat):
     drawCircles(t,size)
     t.right(360/repeat)
 drawSpecial(Johny,101,11)
 def drawCircles(t,size):
     for i in range(5):
         t.circle(size)
         size=size - minus -3
 def drawSpecial(t,size,repeat):
     for i in range (repeat):
         drawCircles(t,size*2.23)
         t.right(360/repeat)
         drawSpecial(Steve,102,12)

 def drawCircles(t,size):
     for i in range(3):
         t.circle(size)
         size=size- minus
 def drawSpecial(t,size,repeat):
     for i in range (repeat):
         drawCircles(t,size)
         t.right(360/repeat)
 drawSpecial(Barry,103,13)

 def drawCircles(t,size):
     for i in range(4):
         t.circle(size)
         size=size- minus + 2
 def drawSpecial(t,size,repeat):
     for i in range (repeat):
         drawCircles(t,size*1.2)
         t.right(360/repeat)
 drawSpecial(Terry,103,13)

 
 def drawCircles(t,size):
     for i in range(4):
         t.circle(size)
         size=size-minus*3
 def drawSpecial(t,size,repeat):
     for i in range (repeat):
         drawCircles(t,size)
         t.right(360/repeat)
 drawSpecial(Will,104,14)


 def drawCircles(t,size):
     for i in range(4):
         t.circle(size%9)
         size=size-minus-45
 
 def drawSpecial(t,size,repeat):
     for i in range (repeat):
         drawCircles(t,size)
         t.right(360/repeat)
         drawSpecial(Nich,105,10)