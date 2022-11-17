# The Accumulator Pattern with Strings

We can also accumulate strings rather than accumulating numbers, as you’ve seen before. The following program isn’t particularly useful for data processing, but we will see more useful things later that accumulate strings.
```
s = input("Enter some text: [meow]") 
ac = ""
for c in s:
    ac = ac + c + "-" + c + "-"

print(ac)

m-m-e-e-o-o-w-w-
```

Look carefully at line 4 in the above program (ac = ac + c + "-" + c + "-"). In words, it says that the new value of ac will be the old value of ac concatenated with the current character, a dash, then the current character and a dash again. We are building the result string character by character.

Take a close look also at the initialization of ac. We start with an empty string and then begin adding new characters to the end. Also note that I have given it a different name this time, ac instead of accum. There’s nothing magical about these names. You could use any valid variable and it would work the same (try substituting x for ac everywhere in the above code).

```
s = "ball"
r = ""
for item in s:
   r = item.upper() + r
print(r)

LLAB
```

For each character in the string already saved in the variable str1, add each character to a list called chars.
# HINT: what's the accumulator? That should go here.
```
str1 = "I love python"
chars = []

for char in str1:
    chars.append(char)
print(chars)

['I', ' ', 'l', 'o', 'v', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n']
```

Assign an empty string to the variable output. Using the range function, write code to make it so that the variable output has 35 a s inside it (like "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"). Hint: use the accumulation pattern!
```
output = ""

for i in range(35):
    output = output + "a"
print(output)
```
