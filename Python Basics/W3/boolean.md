# Boolean Values and Boolean Expressions

The Python type for storing true and false values is called bool, named after the British mathematician, George Boole. George Boole created Boolean Algebra, which is the basis of all modern computer arithmetic.

There are only two boolean values. They are True and False. Capitalization is important, since true and false are not boolean values (remember Python is case sensitive).
```
print(True)
print(type(True))
print(type(False))

True
<class 'bool'>
<class 'bool'>
```
Note

Boolean values are not strings!

It is extremely important to realize that True and False are not strings. They are not surrounded by quotes. They are the only two values in the data type bool. Take a close look at the types shown below.
```
print(type(True))
print(type("True"))

<class 'bool'>
<class 'str'>
```

A boolean expression is an expression that evaluates to a boolean value. The equality operator, ==, compares two values and produces a boolean value related to whether the two values are equal to one another.
```
print(5 == 5)
print(5 == 6)

True
False
```

In the first statement, the two operands are equal, so the expression evaluates to True. In the second statement, 5 is not equal to 6, so we get False.

The == operator is one of six common comparison operators; the others are:
```
x != y               # x is not equal to y
x > y                # x is greater than y
x < y                # x is less than y
x >= y               # x is greater than or equal to y
x <= y               # x is less than or equal to y
```
Although these operations are probably familiar to you, the Python symbols are different from the mathematical symbols. A common error is to use a single equal sign (=) instead of a double equal sign (==). Remember that = is an assignment operator and == is a comparison operator. Also, there is no such thing as =< or =>.

Note too that an equality test is symmetric, but assignment is not. For example, if a == 7 then 7 == a. But in Python, the statement a = 7 is legal and 7 = a is not.
