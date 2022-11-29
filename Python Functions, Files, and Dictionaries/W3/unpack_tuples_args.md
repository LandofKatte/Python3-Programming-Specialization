# Unpacking Tuples as Arguments to Function Calls

Python even provides a way to pass a single tuple to a function and have it be unpacked for assignment to the named parameters.
```
def add(x, y):
    return x + y

print(add(3, 4))
z = (5, 4)
print(add(z)) # this line causes an error
```
This won’t quite work. It will cause an error, because the function add is expecting two parameters, but you’re only passing one parameter (a tuple). If only there was a way to tell python to unpack that tuple and use the first element to assign to x and the second to y.

Actually, there is a way.
```
def add(x, y):
    return x + y

print(add(3, 4))
z = (5, 4)
print(add(*z)) # this line will cause the values to be unpacked

7
9
```
if you come across some code that someone else has written that uses the * notation inside a parameter list ^
