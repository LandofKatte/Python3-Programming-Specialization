# Mutability
If a type is able to change, then it is said to be mutable. If the type is not able to change then it is said to be immutable.

## Strings are IMMUTABLE

What makes strings different from some other Python collection types is that you are not allowed to modify the individual characters in the collection. It is tempting to use the [] operator on the left side of an assignment, with the intention of changing a character in a string.

Strings are immutable, which means you cannot change an existing string. The best you can do is create a new string that is a variation on the original.
```
greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print(greeting)          # same as it was

Jello, world!
Hello, world!
```
The solution here is to concatenate a new first letter onto a slice of greeting. This operation has no effect on the original string.

While it’s possible to make up new variable names each time we make changes to existing values, it could become difficult to keep track of them all.
```
phrase = "many moons"
phrase_expanded = phrase + " and many stars"
phrase_larger = phrase_expanded + " litter"
phrase_complete = "M" + phrase_larger[1:] + " the night sky."
excited_phrase_complete = phrase_complete[:-1] + "!"
```
The more that you change the string, the more difficult it is to come up with a new variable to use. It’s perfectly acceptable to re-assign the value to the same variable name in this case.


## LISTS are MUTABLE

We can change an item in a list by accessing it directly as part of the assignment statement. Using the indexing operator (square brackets) on the left side of an assignment, we can update one of the list items.
```
fruit = ["banana", "apple", "cherry"]
print(fruit)

fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)

['banana', 'apple', 'cherry']
['pear', 'apple', 'orange']
```
An assignment to an element of a list is called item assignment. Item assignment does not work for strings. Recall that strings are immutable.
```
alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y']
print(alist)

['a', 'x', 'y', 'd', 'e', 'f']
```
We can also remove elements from a list by assigning the empty list to them.
```
alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = []
print(alist)

['a', 'd', 'e', 'f']
```
We can even insert elements into a list by squeezing them into an empty slice at the desired location.
```
alist = ['a', 'd', 'f']
alist[1:1] = ['b', 'c']
print(alist)
alist[4:4] = ['e']
print(alist)

['a', 'b', 'c', 'd', 'f']
['a', 'b', 'c', 'd', 'e', 'f']
```

## Tuples are Immutable

As with strings, if we try to use item assignment to modify one of the elements of a tuple, we get an error. In fact, that’s the key difference between lists and tuples: tuples are like immutable lists. None of the operations on lists that mutate them are available for tuples. Once a tuple is created, it can’t be changed.
