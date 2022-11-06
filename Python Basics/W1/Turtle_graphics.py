#The first line tells Python to load a module named turtle. That module brings us two new types that we can use: the Turtle type, and the Screen type. The dot notation turtle.Turtle means “The Turtle type that is defined within the turtle module”. (Remember that Python is case sensitive, so the module name, turtle, with a lowercase t, is different from the type Turtle because of the uppercase T.)

#We then create and open what the turtle module calls a screen (we would prefer to call it a window, or in the case of this web version of Python simply a canvas), which we assign to variable wn. Every window contains a canvas, which is the area inside the window on which we can draw.

#Which direction does the Turtle face when it is created? *EAST*
#Why do we type turtle.Turtle() to get a new Turtle object? *The first "turtle" (before the period) tells Python that we are referring to the turtle module, which is where the object "Turtle" is found.*


#Example given

import turtle             # allows us to use the turtles library
wn = turtle.Screen()      # creates a graphics window
alex = turtle.Turtle()    # create a turtle named alex
alex.forward(150)         # tell alex to move forward by 150 units
alex.left(90)             # turn by 90 degrees
alex.forward(75)          # complete the second side of a rectangle

#unfinished rectangle

#Example given

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")        # set the window background color

tess = turtle.Turtle()
tess.color("blue")              # make tess blue
tess.pensize(3)                 # set the width of her pen

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()                # wait for a user click on the canvas

#The last line plays a very important role. The wn variable refers to the window shown above. When we invoke its exitonclick method, the program pauses execution and waits for the user to click the mouse somewhere in the window. When this click event occurs, the response is to close the turtle window and exit (stop execution of) the Python program.

Color Names Available:

https://www.w3schools.com/colors/colors_names.asp
  
#Example given (2 turtles)

import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")


tess = turtle.Turtle()           # create tess and set his pen width
tess.pensize(5)

alex = turtle.Turtle()           # create alex
alex.color("hotpink")            # set his color

tess.forward(80)                 # Let tess draw an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                   # complete the triangle

tess.right(180)                  # turn tess around
tess.forward(80)                 # move her away from the origin so we can see alex

alex.forward(50)                 # make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()
__________________

import turtle
wn = turtle.Screen()
june = turtle.Turtle()

for _ in range(4):
    june.color("green", "yellow")
    june.forward(50)
    june.right(90)

    #line colored-for loop square
________________________________________________________________________
#Spiral example using For Loop

import turtle
wn = turtle.Screen()

elan = turtle.Turtle()

distance = 50
for _ in range(10):
    elan.forward(distance)
    elan.right(90)
    distance = distance + 10

    
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")          #actually turtle shaped

dist = 5
tess.up()                     # this is new (moves pen up off canvas so doesnt leave line)
for _ in range(30):    # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(dist)          # move tess along
    tess.right(24)              # and turn her
    dist = dist + 2
wn.exitonclick()
________________________________________________________________________

import turtle             # allows us to use the turtles library
wn = turtle.Screen()      # creates a graphics window
alex = turtle.Turtle()    # create a turtle named alex
alex.left(50)
alex.forward(133)         # tell alex to move forward by 133 units
alex.circle(50,200)             # turn
alex.right(140)
alex.circle(50,200)
alex.forward(133)

#creates a heart :)

____________________________________________________________________________

#For loop

import turtle
wn = turtle.Screen()
alex = turtle.Turtle() 

for _ in range(7):
    alex.left(50)
    alex.forward(133)         
    alex.circle(50,200)            
    alex.right(140)
    alex.circle(50,200)
    alex.forward(133)

#looks like overlapping clover hearts
_____________________________________________________________________________________

""""

Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):

    An equilateral triangle

    A square

    A hexagon (six sides)

    An octagon (eight sides)

""""

# draw an equilateral triangle
import turtle

wn = turtle.Screen()
norton = turtle.Turtle()

for i in range(3):
    norton.forward(100)

    # the angle of each vertice of a regular polygon
    # is 360 divided by the number of sides
    norton.left(360/3)

wn.exitonclick()

# draw a square
import turtle

wn = turtle.Screen()
squirtle = turtle.Turtle()

for i in range(4):
    squirtle.forward(100)
    squirtle.left(360/4)

wn.exitonclick()

# draw a hexagon
import turtle

wn = turtle.Screen()
turthex = turtle.Turtle()

for i in range(6):
    turthex.forward(100)
    turthex.left(360/6)

wn.exitonclick()

# draw an octogon
import turtle

wn = turtle.Screen()
octo = turtle.Turtle()

for i in range(8):
    octo.forward(75)
    octo.left(360/8)

wn.exitonclick()

__________________________________________
#star of david
import turtle

star = turtle.Turtle()

for i in range(5):
    star.forward(110)
    star.left(216)
______________________________________________ 
#multi-stars
import turtle
  
# number of sides
n = 10
  
# creating instance of turtle
pen = turtle.Turtle()
  
# loop to draw a side
for i in range(n):
    # drawing side of 
    # length i*10
    pen.forward(i * 10)
  
    # changing direction of pen 
    # by 144 degree in clockwise
    pen.right(144)
  
# closing the instance
turtle.done()
_____________________________________________
#cool busy spiral-star
import turtle

turing = turtle.Turtle()

turing.hideturtle()
turing.speed(20)

for i in range(150):
    turing.forward(i)
    turing.right(98)
    
___________________________________________________
#circle

import turtle
    
tur = turtle.Turtle()
  
tur.circle(-50)
turtle.done()
_____________________________________________
