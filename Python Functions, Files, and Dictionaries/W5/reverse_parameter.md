# Optional reverse parameter

The sorted function takes some optional parameters (see the Optional Parameters page). The first optional parameter is a key function, which will be described in the next section. The second optional parameter is a Boolean value which determines whether to sort the items in reverse order. By default, it is False, but if you set it to True, the list will be sorted in reverse order.
```
L2 = ["Cherry", "Apple", "Blueberry"]
print(sorted(L2, reverse=True))

['Cherry', 'Blueberry', 'Apple']
```

### Note
For most functions, it is possible to provide optional parameters without keywords, but the sorted function prevents this, so you have to provide keywords for the reverse and key parameters. In this situation, it is more convenient to use the keyword mechanism anyway.

```
lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]
lst_sorted = sorted(lst, reverse=False)


[-2, 1, 2, 3, 5, 5, 6, 7, 9]
```


Sort the list, lst from largest to smallest. Save this new list to the variable lst_sorted.
```
lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]
lst_sorted = sorted(lst, reverse=True)
print(lst_sorted)

[9, 7, 6, 5, 5, 3, 2, 1, -2]
```
