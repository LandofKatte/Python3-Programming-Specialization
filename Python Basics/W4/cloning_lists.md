# Cloning Lists

If we want to modify a list and also keep a copy of the original, we need to be able to make a copy of the list itself, not just the reference. This process is sometimes called cloning, to avoid the ambiguity of the word copy.

The easiest way to clone a list is to use the slice operator.

Taking any slice of a creates a new list. In this case the slice happens to consist of the whole list.
```
a = [81,82,83]

b = a[:]       # make a clone using slice
print(a == b)
print(a is b)

b[0] = 5

print(a)
print(b)

True
False
[81, 82, 83]
[5, 82, 83]
```

Now we are free to make changes to b without worrying about a. Again, we can clearly see in codelens that a and b are entirely different list objects.

```
alist = [4,2,8,6,5]
blist = alist * 2
blist[3] = 999
print(alist)

[4,2,8,6,5]
```
alist was unchanged by the assignment statement. blist was a copy of the references in alist.
