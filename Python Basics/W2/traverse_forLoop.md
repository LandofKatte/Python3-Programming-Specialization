# Traversal and the for Loop: By Index

With a for loop, the loop variable is bound, on each iteration, to the next item in a sequence. Sometimes, it is natural to think about iterating through the positions, or indexes of a sequence, rather than through the items themselves.

For example, consider the list ['apple', 'pear', 'apricot', 'cherry', 'peach']. ‘apple’ is at position 0, ‘pear’ at position 1, and ‘peach’ at position 4.

Thus, we can iterate through the indexes by generating a sequence of them, using the range function.
```
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(5):
    print(n, fruits[n])
    
0 apple
1 pear
2 apricot
3 cherry
4 peach
```
In order to make the iteration more general, we can use the len function to provide the bound for range. This is a very common pattern for traversing any sequence by position. Make sure you understand why the range function behaves correctly when using len of the string as its parameter value.
```
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n, fruits[n])
    
0 apple
1 pear
2 apricot
3 cherry
4 peach
```
In some other programming languages, that’s the only way to iterate through a sequence, by iterating through the positions and extracting the items at each of the positions. Python code is often easier to read because we don’t have to do iteration that way. Compare the iteration above with the more “pythonic” approach below.
```
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for fruit in fruits:
    print(fruit)
    
apple
pear
apricot
cherry
peach
```
If we really want to print the indexes (positions) along with the fruit names, then iterating through the indexes as in the previous versions is available to us. Python also provides an enumerate function which provides a more “pythonic” way of enumerating the items in a list, but we will delay the explanation of how to use enumerate until we cover the notions of tuple packing and unpacking.
