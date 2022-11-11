#Write one for loop to print out each character of the string my_str on a separate line.

my_str = "MICHIGAN"

for char in my_str:
    print(char)
    
M
I
C
H
I
G
A
N
__________________________________________________

#Write one for loop to print out each element of the list several_things. Then, write another for loop to print out the TYPE of each element of the list several_things. To complete this problem you should have written two different for loops, each of which iterates over the list several_things, but each of those 2 for loops should have a different result.

several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

for thing in several_things:
    print(thing)
    
for typ in several_things:
    print(type(typ))
    
hello
2
4
6.0
7.5
234352354
the end

99
<class 'str'>
<class 'int'>
<class 'int'>
<class 'float'>
<class 'float'>
<class 'int'>
<class 'str'>
<class 'str'>
<class 'int'>
__________________________________________

#Write code that uses iteration to print out the length of each element of the list stored in str_list.

str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

for i in range(len(str_list)):
    print(len(str_list[i]))
    
_______________________________________________

#Write a program that uses the turtle module and a for loop to draw something. It doesn’t have to be complicated, but draw something different than we have done in the past. (Hint: if you are drawing something complicated, it could get tedious to watch it draw over and over. Try setting .speed(10) for the turtle to draw fast, or .speed(0) for it to draw super fast with no animation.)


import turtle

wn = turtle.Screen()
wn.bgcolor("light blue")
alex = turtle.Turtle()
alex.color("blue")
alex.shape("turtle")
alex.speed(10)

for i in range(20):
    alex.forward(100)
    alex.stamp()
    alex.backward(100)
    alex.right(360/20)

turtle.circle(100)
turtle.circle(-100)
_________________________

#Write code to count the number of characters in original_str using the accumulation pattern and assign the answer to a variable num_chars. Do NOT use the len function to solve the problem (if you use it while you are working on this problem, comment it out afterward!)

original_str = "The quick brown rhino jumped over the extremely lazy fox."

num_chars = 0

for i in original_str:
    num_chars = num_chars + 1
print(num_chars)
__________________________________

#addition_str is a string with a list of numbers separated by the + sign. Write code that uses the accumulation pattern to take the sum of all of the numbers and assigns it to sum_val (an integer). (You should use the .split("+") function to split by "+" and int() to cast to an integer).
addition_str = "2+5+10+20"

nums = addition_str.split("+")
#print(nums)
sum_val = 0
for w in nums:
    sum_val = sum_val + int(w)
print(sum_val)

#37
__________________________________
#week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign. Write code that uses the accumulation pattern to compute the average (sum divided by number of items) and assigns it to avg_temp. Do not hard code your answer (i.e., make your code compute both the sum or the number of items in week_temps_f) (You should use the .split(",") function to split by "," and float() to cast to a float).

week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

week_temps_f = week_temps_f.split(",")
accum = 0

for n in week_temps_f:
    accum = accum + float(n)

avg_temp = accum/len(week_temps_f)
print(avg_temp)

#faster way to compute than above??
_____________________________________________
#Write code to create a list of numbers from 0 to 67 and assign that list to the variable nums. Do not hard code the list.

nums = list(range(0, 68))
print(nums)
