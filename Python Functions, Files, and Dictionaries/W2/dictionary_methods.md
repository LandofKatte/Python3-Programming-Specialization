# Dictionary methods

Dictionaries have a number of useful built-in methods. The following table provides a summary and more details can be found in the Python Documentation.

| Method | Parameters | Description |
|--|--|--|
| keys | none | Returns a view of the keys in the dictionary |
| values | none | Returns a view of the values in the dictionary |
| items | none | Returns a view of the key-value pairs in the dictionary |
| get | key | Returns the value associated with key; None otherwise |
| get | key,alt | Returns the value associated with key; alt otherwise |

As we saw earlier with strings and lists, dictionary methods use dot notation, which specifies the name of the method to the right of the dot and the name of the object on which to apply the method immediately to the left of the dot. For example, if x is a variable whose value is a dictionary, x.keys is the method object, and x.keys() invokes the method, returning a view of the value.

# Iterating over Dictionaries

There are three ways to iterate over the contents of a dictionary. Let’s take a moment to examine them.

The first technique involves iterating over the keys of the dictionary using the keys method. The keys method returns a collection of the keys in the dictionary.

```
inventory = {'apples': 430, 'bananas': 312, 'pears': 217, 'oranges': 525}

for akey in inventory.keys():     # the order in which we get the keys is not defined
    print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())       # Make a list of all of the keys
print(ks)
print(ks[0])                      # Display the first key

Got key apples which maps to value 430
Got key bananas which maps to value 312
Got key pears which maps to value 217
Got key oranges which maps to value 525
['apples', 'bananas', 'pears', 'oranges']
apples
```

Note the first line of the for loop:

    for akey in inventory.keys():

Each time through the loop, the loop variable akey is assigned a different key in the dictionary. In the loop body, the value associated with the key is accessed by indexing the dictionary with akey using the expression inventory[akey]. Note that the order in which the keys are assigned in the loop is not predictable. If you want to visit the keys in alphabetic order, you must use the sorted function to produce a sorted collection of keys, like this:

    for akey in sorted(inventory.keys()):

It’s so common to iterate over the keys in a dictionary that you can omit the keys method call in the for loop — iterating over a dictionary implicitly iterates over its keys.
```
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for k in inventory:
    print("Got key", k)
    
Got key apples
Got key bananas
Got key oranges
Got key pears
```

The values method returns a collection of the values in the dictionary. Here’s an example that displays a list of the values:
```
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.values()))

for v in inventory.values():
    print("Got", v)
    
[430, 312, 525, 217]
Got 430
Got 312
Got 525
Got 217
```

The items method returns a collection of tuples containing each key and its associated value. Take a look at this example that iterates over the dictionary using the items method:
```
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.items()))

for k, v in inventory.items():
    print("Got", k, "that maps to", v)
    
[('apples', 430), ('bananas', 312), ('oranges', 525), ('pears', 217)]
Got apples that maps to 430
Got bananas that maps to 312
Got oranges that maps to 525
Got pears that maps to 217
```

Take a close look at the first line of the for loop:

for k, v in inventory.items():

Each time through the loop, k receives a key from the dictionary, and v receives its associated value. That avoids the need to index the dictionary inside the loop body to access the value associated with the key.

### Note
You may have noticed in the examples above that, to print the result of the keys(), values(), and items() methods, we used lines like this:

    print(list(inventory.keys())

instead of this:

print(inventory.keys())

Technically, keys(), values(), and items() don’t return actual lists. Like the range function described previously, they return objects that produce the items one at a time, rather than producing and storing all of them in advance as a list. If you need to perform an operation on the result of one of these methods such as extracting the first item, you must convert the result to a list using the list conversion function. For example, if you want to get the first key, this won’t work: inventory.keys()[0]. You need to make the collection of keys into a real list before using [0] to index into it: list(inventory.keys())[0].

# Safely Retrieving Values

Looking up a value in a dictionary is a potentially dangerous operation. When using the [] operator to access a key, if the key is not present, a runtime error occurs. There are two ways to deal with this problem.

The first approach is to use the in and not in operators, which can test if a key is in the dictionary:
```
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory)
print('cherries' in inventory)

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("We have no bananas")
    
True
False
312
```

The second approach is to use the get method. get retrieves the value associated with a key, similar to the [] operator. The important difference is that get will not cause a runtime error if the key is not present. It will instead return the value None. There exists a variation of get that allows a second parameter that serves as an alternative return value in the case where the key is not present. This can be seen in the final example below. In this case, since “cherries” is not a key, get returns 0 (instead of None).
```
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries",0))

430
None
0
```
```
mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
answer = mydict.get("cat")//mydict.get("dog")
print(answer)

2
```
```
mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
print("dog" in mydict)

True
#Dog is a key in the dictionary.
```
```
mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
print(23 in mydict)

False
#The in operator returns True if a key is in the dictionary, False otherwise.
```
```
total = 0
mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
for akey in mydict:
   if len(akey) > 3:
      total = total + mydict[akey]
print(total)

43
#The for statement iterates over the keys. It adds the values of the keys that have length greater than 3.
```

We have a dictionary of the specific events that Italy has won medals in and the number of medals they have won for each event. Assign to the variable events a list of the keys from the dictionary medal_events. Do not hard code this.
```
medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}

events = list(medal_events.keys())
```
