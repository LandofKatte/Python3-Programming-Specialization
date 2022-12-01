# Introduction: Nested Data and Nested Iteration

## Lists with Complex Items

The lists we have seen so far have had numbers or strings as items. We’ve snuck in a few more complex items, but without ever explicitly discussing what it meant to have more complex items.

In fact, the items in a list can be any type of python object. For example, we can have a list of lists.
```
nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
print(nested1[0])
print(len(nested1))
nested1.append(['i'])
print("-------")
for L in nested1:
    print(L)
    
['a', 'b', 'c']
3
-------
['a', 'b', 'c']
['d', 'e']
['f', 'g', 'h']
['i']
```

Line 2 prints out the first item from the list that nested1 is bound to. That item is itself a list, so it prints out with square brackets. It has length 3, which prints out on line 3. Line 4 adds a new item to nested1. It is a list with one element, ‘i’ (it a list with one element, it’s not just the string ‘i’).

When you get to step 4 of the execution, take a look at the object that variable nested1 points to. It is a list of three items, numbered 0, 1, and 2. The item in slot 1 is small enough that it is shown right there as a list containing items “d” and “e”. The item in slot 0 didn’t quite fit, so it is shown in the figure as a pointer to another separate list; same thing for the item in slot 2, the list ['f', 'g', 'h'].

There’s no special meaning to whether the list is shown embedded or with a pointer to it: that’s just CodeLens making the best use of space that it can. In fact, if you go on to step 5, you’ll see that, with the addition of a fourth item, the list [‘i’], CodeLens has chosen to show all four lists embedded in the top-level list.

With a nested list, you can make complex expressions to get or set a value in a sub-list.

```
nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
y = nested1[1]
print(y)
print(y[0])

print([10, 20, 30][1])
print(nested1[1][0])

['d', 'e']
d
20
d
```

Lines 1-4 above probably look pretty natural to you. Line 5 illustrates the left to right processing of expressions. nested1[1] evaluates to the second inner list, so nested1[1][1] evaluates to its second element, 'e'. Line 6 is just a reminder that you index into a literal list, one that is written out, the same way as you can index into a list referred to by a variable. [10, 20, 30] creates a list. [1] indexes into that list, pulling out the second item, 20.

Just as with a function call where the return value can be thought of as replacing the text of the function call in an expression, you can evaluate an expression like that in line 7 from left to right. Because the value of nested1[1] is the list ['d', 'e'], nested1[1][0] is the same as ['d', 'e'][0]. So line 7 is equivalent to lines 2 and 4; it is a simpler way of pulling out the first item from the second list.

At first, expressions like that on line 7 may look foreign. They will soon feel more natural, and you will end up using them a lot. Once you are comfortable with them, the only time you will write code like lines 2-4 is when you aren’t quite sure what your data’s structure is, and so you need to incrementally write and debug your code. Often, you will start by writing code like lines 2-4, then, once you’re sure it’s working, replace it with something like line 7.

You can change values in such lists in the usual ways. You can even use complex expressions to change values.
```
nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h'], ['i']]
2	nested1[1] = [1, 2, 3]
3	nested1[1][0] = 100
```

The complex items in a list do not have to be lists. They can be tuples or dictionaries. The items in a list do not all have to be the same type, but you will drive yourself crazy if you have lists of objects of varying types. Save yourself some headaches and don’t do that. Here’s a list of dictionaries and some operations on them.
```
nested2 = [{'a': 1, 'b': 3}, {'a': 5, 'c': 90, 5: 50}, {'b': 3, 'c': "yes"}]
```

Global frame
nested2	
 
	
Objects
	
list
0	1	2
dict
"a"	1
"b"	3
	
dict
"a"	5
"c"	90
5	50
	
dict
"b"	3
"c"	"yes"

--------

Try practicing some operations to get or set values in a list of dictionaries.
```





```

You can even have a list of functions (!).
```
def square(x):
    return x*x

L = [square, abs, lambda x: x+1]

print("****names****")
for f in L:
    print(f)

print("****call each of them****")
for f in L:
    print(f(-2))

print("****just the first one in the list****")
print(L[0])
print(L[0](3))

****names****
<function square>
<built-in function abs>
<function <lambda>>
****call each of them****
4
2
-1
****just the first one in the list****
<function square>
9
```

