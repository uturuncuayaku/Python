# Andres Trujillo
# 11/20/2019
# Game Off 2019
# Open Source PYXEL Game Engine for Python 3.x
# Asteroids 8-bit Retro game
#
#******************************************************#


import math
import random
import pyxel

# constants

WIDTHSCREEN = 100
HEIGHTSCREEN = 100

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rocks:
    def __init__(self):

    	# Random amount of rocks from 3-10
        self.r = random.uniform(3,10)

        self.position = Vector2(random.uniform( self.r, WIDTHSCREEN-self.r ),
           						 random.uniform( self.r, HEIGHTSCREEN-self.r ), )
        self.velocity = Vector2(random.uniform(-1.8, 1.8),
            					random.uniform(-1.8, 1.8),)

        # Randomize color of each rock
        self.color = random.randint(1,15)
        
    def update(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

        # Making sure rocks stay within screen
        if self.velocity.x < 0 and self.position.x < self.r:
            self.velocity.x *= -1

        if self.velocity.x > 0 and self.position.x > WIDTHSCREEN - self.r:
            self.velocity.x *= -1

        if self.velocity.y < 0 and self.position.y < self.r:
            self.velocity.y *= -1

        if self.velocity.y > 0 and self.position.y > HEIGHTSCREEN - self.r:
            self.velocity.y *= -1
        
class Spaceship:
    def __init__(self):
        # Space ship initial loading location in middle of window
        self.space_ship_x = pyxel.mouse_x
        self.space_ship_y = pyxel.mouse_x

        pyxel.image(0).load(0, 0, "Assets/spaceship.png")

        # Vector of spaceship for movement
        #self.spaceship_vx = 50
        #self.spaceship_vy = 50
    def drawSpaceship(self):
    	#self.space_ship_x = 
    	#self.space_ship_y = pyxel.mouse_x
        pyxel.blt(space_ship_x,space_ship_y,0,0,0,10,20,0)

# my main class        
class Asteroid:
    def __init__(self):
        
        # Draw screen using PYXEL Game Engine
        pyxel.init(100, 100, caption="Protect the Universe", scale=5)
        pyxel.mouse(True)

        #Spaceship()
        #Spaceship.drawSpaceship()
        #self.update.Spaceship(pyxel.mouse_x,pyxel.mouse_y)
        #self.drawSpaceship()

        # Calling Rocks() class to populate
        # screen with rocks to be blown up
        self.rocks = [ Rocks() for _ in range(10) ]
        
        # Game Title and Menu
        #self.s = "Asteroids 8-bit"
        #self.start_button = "Start Game: Press 1"
   
        #myss.drawSpaceship()  
        #self.ship.update()
        pyxel.run(self.update, self.draw)



        
        # Game Boolean values
        #self.gameRunning = False
        #self.space_ship_alive = True
        #self.livesRemaining = 10

    # Game Logic        
    def update(self):
        # If player presses Q on keyboard
        # program will exit
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        rocks_count = len(self.rocks)
        
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
        	for i in range(rocks_count):
        		rock = self.rocks[i]

        # Counts backwards from 9 to 0
        for i in range(rocks_count - 1, -1, -1):
        	ri = self.rocks[i]
        	ri.update()
		
		myss = Spaceship()
        self.ship = Spaceship()  
		myss.drawSpaceship() 


    def draw(self):
        
        # Splash Screen welcoming player 
        # Background color filling entire screen with default border sizes
        pyxel.cls(0)

        # Propagate screen with rocks using pyxel circle draw
        # function and passing along random numbers that are calculated
        # in Rocks Class.
        for rock in self.rocks:
            pyxel.circ(rock.position.x, rock.position.y, rock.r, rock.color)
		


        # Attempt to draw spaceship
        # Attempt to also move ship
        #myss = Spaceship()
        #print(type(pyxel.mouse_y), type(pyxel.mouse_x))
        #xofp = pyxel.mouse_x
        #yofp = pyxel.mouse_y
        #myss.drawSpaceship()
        #print("x: "+str(xofp))
        #print("y: "+str(yofp))

        #myss.update()

        #self.ship.rotateShip()
        
        # Attempt to rotate ship
        # at 0,0 or Top Left for now
        #if pyxel.btnp(pyxel.KEY_LEFT):
        #    self.ship.rotateShip()
        
        
        #Place Title and Game Menu at middle of screen
        #pyxel.text(20, 10, self.s, 4)
        #pyxel.text(10, 50, self.start_button, 1)
        #pyxel.text(10, 60, "Quit: Press Q", 1)
        

       
       # When player at initial loading
       # screen presses 1
       # to start game and spaceship
       # will need to be drawn

        #if pyxel.btn(pyxel.KEY_1):
        #    self.gameRunning = True
            # clear screen
            # pyxel.cls(0)
            # draw menu detailing space ships(lives) remaining until game over
            # draw spaceship
            # draw enemies and rocks to blow up
            
        #while self.gameRunning : #& (self.livesRemaining > 0)
        #   pyxel.cls(0)
            # give spaceship movement
            # update spaceship movement
            # update score
            # update the number of ships player has remaining

Asteroid()
