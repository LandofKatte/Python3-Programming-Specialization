# Nested Iteration

When you have nested data structures, especially lists and/or dictionaries, you will frequently need nested for loops to traverse them.
```
nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    for y in x:
        print("     level2: " + y)

level1: 
     level2: a
     level2: b
     level2: c
level1: 
     level2: d
     level2: e
level1: 
     level2: f
     level2: g
     level2: h
```
Line 3 executes once for each top-level list, three times in all. With each sub-list, line 5 executes once for each item in the sub-list.


Now try rearranging these code fragments to make a function that counts all the leaf items in a nested list like nested1 above, the items at the lowest level of nesting (8 of them in nested1).
```
def count_leaves(n):
  count = 0
  for L in n:
    for x in L:
      count = count + 1
  return count
```

Below, we have provided a list of lists that contain information about people. Write code to create a new list that contains every person’s last name, and save that list as last_names.
```
info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]

last_names = []

for entertainer in info:
    last_names.append(entertainer[1])

print(last_names)

['Turner', 'Damon', 'Wiig', 'Phelps', 'Obama']
```

Below, we have provided a list of lists named L. Use nested iteration to save every string containing “b” into a new list named b_strings.
```
L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]

b_strings = []

for lst in L:
    for word in lst:
        if 'b' in word:
            b_strings.append(word)

print(b_strings)

['bananas', 'blueberries', 'cucumbers', 'green beans', 'root beer', 'cranberry juice']
```
