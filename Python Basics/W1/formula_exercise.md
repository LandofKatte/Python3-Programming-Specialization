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
