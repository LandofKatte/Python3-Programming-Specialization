# The in and not in operators

The in operator tests if one string is a substring of another:
```
print('p' in 'apple')
print('i' in 'apple')
print('ap' in 'apple')
print('pa' in 'apple')

True
False
True
False
```

Note that a string is a substring of itself, and the empty string is a substring of any other string. (Also note that computer scientists like to think about these edge cases quite carefully!)
```
print('a' in 'a')
print('apple' in 'apple')
print('' in 'a')
print('' in 'apple')

True
True
True
True
```

The not in operator returns the logical opposite result of in.
```
print('x' not in 'apple')

True
```

We can also use the in and not in operators on lists!
```
print("a" in ["a", "b", "c", "d"])
print(9 in [3, 2, 9, 10, 9.0])
print('wow' not in ['gee wiz', 'gosh golly', 'wow', 'amazing'])

True
True
False
```

However, remember how you were able to check to see if an “a” was in “apple”? Let’s try that again to see if there’s an “a” somewhere in the following list.
```
print("a" in ["apple", "absolutely", "application", "nope"])

False
```

Clearly, we can tell that a is in the word apple, and absolutely, and application. For some reason though, the Python interpreter returns False. Why is that? When we use the in and not in operators on lists, Python checks to see if the item on the left side of the expression is equivalent to an element in the item on the right side of the expression. In this case, Python is checking whether or not an element of the list is the string “a” - nothing more or less than that.
