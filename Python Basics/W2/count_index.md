# Count and Index

As you create more complex programs, you will find that some tasks are commonly done. Python has some built-in functions and methods to help you with these tasks. This page will cover two helpful methods for both strings and lists: count and index.

You’ve learned about methods before when drawing with the turtle module. There, you used .forward(50) and .color("purple") to complete actions. We refer to forward and color as methods of the turtle class. Objects like strings and lists also have methods that we can use.

## Count

The first method we’ll talk about is called count. It requires that you provide one argument, which is what you would like to count. The method then returns the number of times that the argument occured in the string/list the method was used on. There are some differences between count for strings and count for lists. When you use count on a string, the argument can only be a string. You can’t count how many times the integer 2 appears in a string, though you can count how many times the string “2” appears in a string. For lists, the argument is not restricted to just strings.
```
a = "I have had an apple on my desk before!"
print(a.count("e"))
print(a.count("ha"))

5
2
```
```
z = ['atoms', 4, 'neutron', 6, 'proton', 4, 'electron', 4, 'electron', 'atoms']
print(z.count("4"))
print(z.count(4))
print(z.count("a"))
print(z.count("electron"))

0
3
0
2
```
When you run the activecode window above, you’ll see how count with a list works. Notice how “4” has a count of zero but 4 has a count of three? This is because the list z only contains the integer 4. There are never any strings that are 4. Additionally, when we check the count of “a”, we see that the program returns zero. Though some of the words in the list contain the letter “a”, the program is looking for items in the list that are just the letter “a”.

## Index

The other method that can be helpful for both strings and lists is the index method. The index method requires one argument, and, like the count method, it takes only strings when index is used on strings, and any type when it is used on lists. For both strings and lists, index returns the leftmost index where the argument is found. If it is unable to find the argument in the string or list, then an error will occur.
```
music = "Pull out your music and dancing can begin"
bio = ["Metatarsal", "Metatarsal", "Fibula", [], "Tibia", "Tibia", 43, "Femur", "Occipital", "Metatarsal"]

print(music.index("m"))
print(music.index("your"))

print(bio.index("Metatarsal"))
print(bio.index([]))
print(bio.index(43))

14
9
0
3
6
```

All of the above examples work, but were you surprised by any of the return values? Remember that index will return the left most index of the argument. Even though “Metatarsal” occurs many times in bio, the method will only return the location of one of them.
