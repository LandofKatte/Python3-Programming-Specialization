# Strings and for loops

Since a string is simply a sequence of characters, the for loop iterates over each character automatically.

```
for achar in "Go Spot Go":
    print(achar)
    
G
o
 
S
p
o
t
 
G
o
```
The loop variable achar is automatically reassigned each character in the string “Go Spot Go”. We will refer to this type of sequence iteration as iteration by item. Note that the for loop processes the characters in a string or items in a sequence one at a time from left to right.

# Lists and for loops

It is also possible to perform list traversal using iteration by item. A list is a sequence of items, so the for loop iterates over each item in the list automatically.
```
fruits = ["apple", "orange", "banana", "cherry"]

for afruit in fruits:     # by item
    print(afruit)
    
apple
orange
banana
cherry
```

# Using the range Function to Generate a Sequence to Iterate Over

We are now in a position to understand the inner workings we glossed over previously when we first introduced repeated execution with a for loop. Here was the example:
```
print("This will execute first")

for _ in range(3):
    print("This line will execute three times")
    print("This line will also execute three times")

print("Now we are outside of the for loop!")

This will execute first
This line will execute three times
This line will also execute three times
This line will execute three times
This line will also execute three times
This line will execute three times
This line will also execute three times
Now we are outside of the for loop!
```

The range function takes an integer n as input and returns a sequence of numbers, starting at 0 and going up to but not including n. Thus, instead of range(3), we could have written [0, 1, 2].

The loop variable _ is bound to 0 the first time lines 4 and 5 execute. The next time, _ is bound to 1. Third time, it is bound to 2. _ is a strange name for a variable but if you look carefully at the rules about variable names, it is a legal name. By convention, we use the _ as our loop variable when we don’t intend to ever refer to the loop variable. That is, we are just trying to repeat the code block some number of times (once for each item in a sequence), but we are not going to do anything with the particular items. _ will be bound to a different item each time, but we won’t ever refer to those particular items in the code.

By contrast, notice that in the previous activecode window, the loop variable is afruit. In that for loop, we do refer to each item, with print(afruit).

## Iteration Simplifies our Turtle Program

Remember the turtle drawings we made earlier? Let’s look again at how we can use for loops there!

To draw a square we’d like to do the same thing four times — move the turtle forward some distance and turn 90 degrees. We previously used 8 lines of Python code to have alex draw the four sides of a square. This next program does exactly the same thing but, with the help of the for statement, uses just three lines (not including the setup code). Remember that the for statement will repeat the forward and left four times, one time for each value in the list.
```
import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()

for i in [0, 1, 2, 3]:      # repeat four times
    alex.forward(50)
    alex.left(90)

wn.exitonclick()
```
The values [0,1,2,3] were provided to make the loop body execute 4 times. We could have used any four values.
```
import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()

for aColor in ["yellow", "red", "purple", "blue"]:    # repeat four times
    alex.color(aColor)
    alex.forward(50)
    alex.left(90)

wn.exitonclick()
```
In this case, the value of aColor is used to change the color attribute of alex. Each iteration causes aColor to change to the next value in the list.

The for-loop is our first example of a compound statement. Syntactically a compound statement is a statement. The level of indentation of a (whole) compound statement is the indentation of its heading. In the example above there are five statements with the same indentation, executed sequentially: the import, 2 assignments, the whole for-loop, and wn.exitonclick(). The for-loop compound statement is executed completely before going on to the next sequential statement, wn.exitonclick()
