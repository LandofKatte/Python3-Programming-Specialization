# The Accumulator Pattern with Lists

We can accumulate values into a list rather than accumulating a single numeric value. Consider, for example, the following program which transforms a list into a new list by squaring each of the values.
```
nums = [3, 5, 8]
accum = []
for w in nums:
    x = w**2
    accum.append(x)
print(accum)

[9, 25, 64]
```

Here, we initialize the accumulator variable to be an empty list, on line 2.

We iterate through the sequence (line 3). On each iteration we transform the item by squaring it (line 4).

The update step appends the new item to the list which is stored in the accumulator variable (line 5). The update happens using the .append(), which mutates the list rather than using a reassignment. Instead, we could have written accum = accum + [x], or accum += [x]. In either case, we’d need to concatenate a list containing x, not just x itself.

At the end, we have accumulated a new list of the same length as the original, but with each item transformed into a new item. This is called a mapping operation, and we will revisit it in a later chapter.

Note how this differs from mutating the original list, as you saw in a previous section.
```
alist = [4,2,8,6,5]
blist = [ ]
for item in alist:
   blist.append(item+5)
print(blist)

[9,7,13,11,10]
```
```
lst= [3,0,9,4,1,7]
new_list=[]
for i in range(len(lst)):
   new_list.append(lst[i]+5)
print(new_list)

[8,5,14,9,6,12]
```

For each word in the list verbs, add an -ing ending. Save this new list in a new list, ing.
```
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing = []

for word in range(len(verbs)):
    ing.append(verbs[word]+"ing")
print(ing)

['kayaking', 'crying', 'walking', 'eating', 'drinking', 'flying']
```

Given the list of numbers, numbs, create a new list of those same numbers increased by 5. Save this new list to the variable newlist.
```
numbs = [5, 10, 15, 20, 25]
newlist = []

for i in range(len(numbs)):
   newlist.append(numbs[i]+5)

print(newlist)

[10, 15, 20, 25, 30]
```

Given the list of numbers, numbs, modifiy the list numbs so that each of the original numbers are increased by 5. Note this is not an accumulator pattern problem, but its a good review.
```
numbs = [5, 10, 15, 20, 25]

for i in range(len(numbs)):
    numbs[i]=numbs[i]+5
print(numbs)
```

For each number in lst_nums, multiply that number by 2 and append it to a new list called larger_nums.
```
lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]

larger_nums = []

for i in range(len(lst_nums)):
   larger_nums.append(lst_nums[i]*2)

print(larger_nums)

[8, 58, 10.6, 20, 4, 3634, 3934, 18, 62.64]
```
