# List Element Deletion

Using slices to delete list elements can be awkward and therefore error-prone. Python provides an alternative that is more readable. The del statement removes an element from a list by using its position.

```
a = ['one', 'two', 'three']
del a[1]
print(a)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[1:5]
print(alist)

['one', 'three']
['a', 'f']
```

As you might expect, del handles negative indices and causes a runtime error if the index is out of range. In addition, you can use a slice as an index for del. As usual, slices select all the elements up to, but not including, the second index.
