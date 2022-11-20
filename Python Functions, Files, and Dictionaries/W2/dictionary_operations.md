# Dictionary operations

The del statement removes a key-value pair from a dictionary. For example, the following dictionary contains the names of various fruits and the number of each fruit in stock. If someone buys all of the pears, we can remove the entry from the dictionary.
```
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
	
del inventory['pears']
```
Dictionaries are mutable, as the delete operation above indicates. As we’ve seen before with lists, this means that the dictionary can be modified by referencing an association on the left hand side of the assignment statement. In the previous example, instead of deleting the entry for pears, we could have set the inventory to 0.
```
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

inventory['pears'] = 0
```

### Note
Setting the value associated with pears to 0 has a different effect than removing the key-value pair entirely with del. Try printout out the two dictionaries in the examples above.

Similarily, a new shipment of 200 bananas arriving could be handled like this. Notice that there are now 512 bananas— the dictionary has been modified. Note also that the len function also works on dictionaries. It returns the number of key-value pairs.
```
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
inventory['bananas'] = inventory['bananas'] + 200
	
numItems = len(inventory)
```
Notice that there are now 512 bananas—the dictionary has been modified. Note also that the len function also works on dictionaries. It returns the number of key-value pairs.

```
mydict = {"cat":12, "dog":6, "elephant":23}
mydict["mouse"] = mydict["cat"] + mydict["dog"]
print(mydict["mouse"])

18
```

Examples:

Update the value for “Phelps” in the dictionary swimmers to include his medals from the Rio Olympics by adding 5 to the current value (Phelps will now have 28 total medals). Do not rewrite the dictionary.
```
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}

swimmers['Phelps'] = 28
print(swimmers)
```
