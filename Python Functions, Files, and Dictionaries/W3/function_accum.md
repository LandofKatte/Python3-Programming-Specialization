#  A function that accumulates

We have used the len function a lot already. If it weren’t part of python, our lives as programmers would have been a lot harder.

Well, actually, not that much harder. Now that we know how to define functions, we could define len ourselves if it did not exist. Previously, we have used the accumlator pattern to count the number of lines in a file. Let’s use that same idea and just wrap it in a function definition. We’ll call it mylen to distinguish it from the real len which already exists. We actually could call it len, but that wouldn’t be a very good idea, because it would replace the original len function, and our implementation may not be a very good one.

```
def mylen(seq):
    c = 0 # initialize count variable to 0
    for _ in seq:
        c = c + 1   # increment the counter for each item in seq
    return c

print(mylen("hello"))
print(mylen([1, 2, 7]))

5
3
```
_________________________________________________________________________________

Write a function named total that takes a list of integers as input, and returns the total value of all those integers added together.
```
def total(lst):
    tot=0
    for i in lst:
        tot = tot + i
    return (tot)
```

Write a function called count that takes a list of numbers as input and returns a count of the number of elements in the list.
```
def count(lst):
    values = 0
    for i in lst:
        values = values + 1
    return values
```
