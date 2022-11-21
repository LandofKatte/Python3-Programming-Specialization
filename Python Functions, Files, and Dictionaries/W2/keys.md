# Accumulating the Best Key

Now what if we want to find the key associated with the maximum value? It would be nice to just find the maximum value as above, and then look up the key associated with it, but dictionaries don’t work that way. You can look up the value associated with a key, but not the key associated with a value. (The reason for that is there may be more than one key that has the same value).

The trick is to have the accumulator keep track of the best key so far instead of the best value so far. For simplicity, let’s assume that there are at least two keys in the dictionary. Then, similar to our first version of computing the max of a list, we can initialize the best-key-so-far to be the first key, and loop through the keys, replacing the best-so-far whenever we find a better one.

In the exercise below, we have provided skeleton code. See if you can fill it in. An answer is provided, but you’ll learn more if you try to write it yourself first.

Write a program that finds the key in a dictionary that has the maximum value. If two keys have the same maximum value, it’s OK to print out either one. Fill in the skeleton code
```
d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

ks = d.keys()
# initialize variable best_key_so_far to be the first key in d
best_key_so_far = list(ks)[0]  # Have to turn ks into a real list before using [] to select an item
for k in ks:
    # check if the value associated with the current key is
    # bigger than the value associated with the best_key_so_far
    # if so, save the current key as the best so far
    if d[k] > d[best_key_so_far]:
        best_key_so_far = k
        
print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))

key e has the highest value, 312
```

Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to min_value.
```
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d = {}

for i in placement:
    if i not in d:
        d[i] = 0
    d[i] = d[i] + 1
print(d)

kys = list(d.keys())
#print(kys)

min_value = kys[0]

for key in kys:
    if d[key] < d[min_value]:
        min_value = key
print(min_value)

{'B': 2, 'e': 17, 'a': 12, 'c': 8, 'h': 4, 's': 10, ' ': 27, 'r': 7, 'o': 10, 'l': 8, 'p': 6, 't': 8, 'v': 3, 'i': 13, 'n': 7, 'g': 2, 'w': 3, 'M': 3, 'k': 2, 'd': 2, '.': 2, 'x': 1}
x
```

Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value.
```
product = "iphone and android phones"

lett_d = {}
for i in product:
    if i not in lett_d:
        lett_d[i] = 0
    lett_d[i] = lett_d[i]+1
print(lett_d)

kys = list(lett_d.keys())

max_value = kys[0]

for key in kys:
    if lett_d[key] > lett_d[max_value]:
        max_value = key
print(max_value)

{'i': 2, 'p': 2, 'h': 2, 'o': 3, 'n': 4, 'e': 2, ' ': 3, 'a': 2, 'd': 3, 'r': 1, 's': 1}
n
```
