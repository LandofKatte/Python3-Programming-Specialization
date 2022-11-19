# Introduction: Dictionaries

This sort of direct look up of a value in Python is done with an object called a Dictionary. Dictionaries are a different kind of collection. They are Python’s built-in mapping type. A map is an unordered, associative collection. The association, or mapping, is from a key, which can be of any immutable type (e.g., the chapter name and number in the analogy above), to a value (the starting page number), which can be any Python data object.

One way to create a dictionary is to start with the empty dictionary and add key-value pairs. The empty dictionary is denoted {}.
The key-value pairs of the dictionary are separated by commas. Each pair contains a key and a value separated by a colon.

A dictionary is an unordered collection of key-value pairs.

```
eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'
print(eng2sp)

{'one': 'uno', 'two': 'dos', 'three': 'tres'}
```
```
eng2sp = {'three': 'tres', 'one': 'uno', 'two': 'dos'}
print(eng2sp)

{'three': 'tres', 'one': 'uno', 'two': 'dos'}
```
It doesn’t matter what order we write the pairs. The values in a dictionary are accessed with keys, not with indices, so there is no need to care about ordering.
Here is how we use a key to look up the corresponding value.
```
eng2sp = {'three': 'tres', 'one': 'uno', 'two': 'dos'}

value = eng2sp['two']
print(value)
print(eng2sp['one'])

dos
uno
```

## Exercises:

Create a dictionary that keeps track of the USA’s Olympic medal count. Each key of the dictionary should be the type of medal (gold, silver, or bronze) and each key’s value should be the number of that type of medal the USA’s won. Currently, the USA has 33 gold medals, 17 silver, and 12 bronze. Create a dictionary saved in the variable medals that reflects this information.
```
medals = {}

medals['gold'] = 33
medals['silver'] = 17
medals['bronze'] = 12

print(medals)

{'gold': 33, 'silver': 17, 'bronze': 12}
```

You are keeping track of olympic medals for Italy in the 2016 Rio Summer Olympics! At the moment, Italy has 7 gold medals, 8 silver metals, and 6 bronze medals. Create a dictionary called olympics where the keys are the types of medals, and the values are the number of that type of medals that Italy has won so far.
```
olympics = {}

olympics['gold'] = 7
olympics['silver'] = 8
olympics['bronze'] = 6

print(olympics)

{'gold': 7, 'silver': 8, 'bronze': 6}
```

Every four years, the summer Olympics are held in a different country. Add a key-value pair to the dictionary places that reflects that the 2016 Olympics were held in Brazil. Do not rewrite the entire dictionary to do this!
```
places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012}

places['Brazil'] = 2016
```
