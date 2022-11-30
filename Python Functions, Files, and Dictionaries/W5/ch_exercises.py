You’re going to write a function that takes a string as a parameter and returns a list of the five most frequent characters in the string. Eventually, you will be able to do this sort of problem without a lot of coaching. But we’re going to step you through it as a series of exercises.

First, the function will count the frequencies of all the characters, as we’ve done before, using a dictionary and the accumulator pattern. Then, it will sort the (key, value) pairs. Finally, it will take a slice of the sorted list to get just the top five. That slice will be returned.

Step 1. Suppose you had this list, [8, 7, 6, 6, 4, 4, 3, 1, 0], already sorted, how would you make a list of just the best 5? (Hint: take a slice).


L = [8, 7, 6, 6, 4, 4, 3, 1, 0]

L[:5]


Now suppose the list wasn’t sorted yet. How would get those same five elements from this list?


L = [0, 1, 6, 7, 3, 6, 8, 4, 4]

L2 = sorted(L, reverse=True)
L2[:5]


Now take a list L and make a dictionary of counts for how often these numbers appear in the list.


L = [0, 1, 6, 7, 3, 6, 8, 4, 4, 6, 1, 6, 6, 5, 4, 4, 3, 35, 4, 11]

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
        
        
Now sort the keys (numbers) based on their frequencies. Review Sorting a Dictionary if you’re not sure how to do this. Keep just the top five keys.


L = [0, 1, 6, 7, 3, 6, 8, 4, 4, 6, 1, 6, 6, 5, 4, 4, 3, 35, 4, 11]

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1

s = sorted(d, key=lambda x: d[x], reverse=True)

print(s[:5])

[4, 6, 3, 1, 11]


Finally, generalize what you’ve done. Write a function that takes a string instead of a list as a parameter and returns a list of the five most frequent characters in the string.

def five_most_frequent(s):
    d = {}
    for x in s:
        if x in d:
            d[x] = d[x] + 1
        else:
            d[x] = 1

    s = sorted(d, key=lambda x: d[x], reverse=True)

    return s[:5]
