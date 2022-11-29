# Tuple Packing

Wherever python expects a single value, if multiple expressions are provided, separated by commas, they are automatically packed into a tuple. For example, we can omit the parentheses when assigning a tuple of values to a single variable.
```
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
# or equivalently
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
print(julia[4])

2009
```
Which of the following statements will output Atlanta, Georgia
print(julia[-1])

[-1] picks out the last item in the sequence.


Create a tuple called practice that has four elements: ‘y’, ‘h’, ‘z’, and ‘x’.
practice = ("y", "h", "z", "x")

Create a tuple named tup1 that has three elements: ‘a’, ‘b’, and ‘c’.
tup1 = ("a", "b", "c")

Provided is a list of tuples. Create another list called t_check that contains the third element of every tuple.
```
lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]
t_check = []

for x in lst_tups:
    t_check.append(x[2])
print(t_check)

['Zaptos', 'Charizard', 'Diglett', 'Tauros', 'Lanturn', 'Wailord']
```

Below, we have provided a list of tuples. Write a for loop that saves the second element of each tuple into a list called seconds.
```
tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]
seconds = []

for x in tups:
    seconds.append(x[1])
print(seconds)

['b', 7, 'green', 9.99, 'chipmunk']
```
