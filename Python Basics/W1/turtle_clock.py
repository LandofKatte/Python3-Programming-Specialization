#blue-turtle green-fill clock face
#just plan turtles (no lines)
import turtle
wn = turtle.Screen()
wn.bgcolor("light green")
alex = turtle.Turtle()
alex.color("blue")
alex.shape("turtle")
alex.speed(5)
alex.penup()
alex.stamp()

for i in range(12):
    alex.forward(150)
    alex.stamp()
    alex.backward(150)
    alex.right(360/12)             #clockwise
__________________
#turtle clock with hour lines

#NEEDS TO BE REWORKED- GROSS CODE

import turtle
wn = turtle.Screen()
wn.bgcolor("light green")
alex = turtle.Turtle()
alex.color("blue")
alex.shape("turtle")
alex.speed(5)
alex.penup()
alex.stamp()

lin = turtle.Turtle()
lin.color("blue")#make class turtle same attribute...
lin.speed(7) #same class attribute
lin.pensize(2)
lin.penup()

#theres a better less redundant way to write this...
for i in range(12):
    alex.forward(150)
    alex.stamp()
    alex.backward(150)
    alex.right(360/12)             #clockwise

for i in range(12):
    lin.forward(120)       #<140
    lin.pendown()
    lin.forward(10)        #130 forward
    lin.penup()
    lin.backward(130)
    lin.right(360/12)             #clockwise
