Challenge: The formula for computing the final amount if one is earning compound interest is given on Wikipedia as
formula for compound interest

![image](https://user-images.githubusercontent.com/103328611/199859841-92328d1d-92d4-4b69-b708-b3ed64fb3aa8.png)

Write a Python program that assigns the principal amount of 10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8% (0.08). Then have the program prompt the user for the number of years, t, that the money will be compounded for. Calculate and print the final amount after t years.


P = 10000
n = 12
r = 0.08

t = int(input("Compound for how many years? "))

final = P * ( ((1 + (r/n)) ** (n * t)) )

print("The final amount after", t, "years is", final)

________________________________________________________

Write a program that will compute the area of a circle. Prompt the user to enter the radius and save it to avariable called radius. Print a nice message back to the user with the answer.

#A = πr2
pi = 3.14
radius = int(input("What is the radius of the circle? "))
area_of_circle = pi * (radius**2)

print("The area of a circle is ", area_of_circle)

_____________________________________________________________

Challenge: Write a program that will compute the area of a rectangle. Prompt the user to enter the width and height of the rectangle and store the values in variables called width and height. Print a nice message with the answer..

#A = w x h

width = int(input("What is the width of the rectangle? "))
height = int(input("What is the height of the rectangle? "))
area_of_rectangle = height * width

print("The area of the rectangle is ", area_of_rectangle)

_______________________________________________________________

Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and store it in a variable called miles and the number of gallons used stored in a variable gallons. Print a nice message with the answer.

miles = int(input("How many miles driven? "))
gallons = int(input("How many gallons of gas? "))
mpg = miles / gallons

print("The MPG is ", mpg)

__________________________________________________________________

Challenge: Write a program that will convert degrees celsius to degrees fahrenheit.

#formula to convert C to F: (degrees Celcius) x (9/5) + (32)

deg_c = int(input("What is the temperature in Celsius? "))
deg_f = deg_c * (9 / 5) + 32

print(deg_c, " degrees Celsius is", deg_f, " degrees Farenheit.")

__________________________________________________________________________

Ask the user for the temperature in Fahrenheit and store it in a variable call deg_f. Calculate the equivalent temperature in degrees Celsius and store it in deg_c. Output a message to the user giving the temperature in Celsius.

#formula to convert F to C: (degrees F - 32) / 1.8

deg_f = int(input("What is the temperature in Farenheit? "))
deg_c = (deg_f - 32) / 1.8 

print(deg_f, " degrees Farenheit is", deg_c, " degrees Celsius.")

____________________________________________________________________________

There is a function we are providing in for you in this problem called square. It takes one integer and returns the square of that integer value. Write code to assign a variable called xyz the value 5*5 (five squared). Use the square function, rather than just multiplying with *.

xyz = 5
xyz = square(xyz)

print(xyz)
_______________________________________________________________________________
