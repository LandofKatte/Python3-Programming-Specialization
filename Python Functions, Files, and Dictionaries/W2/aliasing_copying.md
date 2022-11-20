# Aliasing and copying

Because dictionaries are mutable, you need to be aware of aliasing (as we saw with lists). Whenever two variables refer to the same dictionary object, changes to one affect the other. For example, opposites is a dictionary that contains pairs of opposites.

```
opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
alias = opposites

print(alias is opposites)

alias['right'] = 'left'
print(opposites['right'])

True
left
```

As you can see from the is operator, alias and opposites refer to the same object.

If you want to modify a dictionary and keep a copy of the original, use the dictionary copy method. Since acopy is a copy of the dictionary, changes to it will not effect the original.

    acopy = opposites.copy()
    acopy['right'] = 'left'    # does not change opposites

```
mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
yourdict = mydict
yourdict["elephant"] = 999
print(mydict["elephant"])

999
```
