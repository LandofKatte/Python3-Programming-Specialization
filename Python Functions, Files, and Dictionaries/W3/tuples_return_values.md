# Tuples as Return Values

Functions can return tuples as return values. This is very useful — we often want to know some batsman’s highest and lowest score, or we want to find the mean and the standard deviation, or we want to know the year, the month, and the day, or if we’re doing some ecological modeling we may want to know the number of rabbits and the number of wolves on an island at a given time. In each case, a function (which can only return a single value), can create a single tuple holding multiple elements.

For example, we could write a function that returns both the area and the circumference of a circle of radius r.
```
def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return (c, a)

print(circleInfo(10))

(62.8318, 314.159)
```
Again, we can take advantage of packing to make the code look a little more readable on line 4
```
def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a

print(circleInfo(10))

(62.8318, 314.159)
```

It’s common to unpack the returned values into multiple variables.
```
def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a

print(circleInfo(10))

circumference, area = circleInfo(10)
print(circumference)
print(area)

circumference_two, area_two = circleInfo(45)
print(circumference_two)
print(area_two)

(62.8318, 314.159)
62.8318
314.159
282.7431
6361.719749999999
```


If you want a function to return two values, contained in variables x and y, which of the following methods will work?

    Include the statement "return [x, y]"
    Include the statement "return (x, y)"
    Include the statement "return x, y"

    return [x,y] is not the preferred method because it returns x and y in a mutable list rather than a tuple which is more efficient. But it is workable.
    return (x, y) returns a tuple.
    return x, y causes the two values to be packed into a tuple.


Define a function called information that takes as input, the variables name, birth_year, fav_color, and hometown. It should return a tuple of these variables in this order.
```
def information(name,birth_year,fav_color,hometown):
    return (name,birth_year,fav_color,hometown)
```

Define a function called info with the following required parameters: name, age, birth_year, year_in_college, and hometown. The function should return a tuple that contains all the inputted information.
```
def info(name,age,birth_year,year_in_college,hometown):
    return (name,age,birth_year,year_in_college,hometown)
```
