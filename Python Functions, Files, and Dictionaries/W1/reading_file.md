# Reading a File

As an example, suppose we have a text file called olympics.txt that contains the data representing about olympians across different years. The contents of the file are shown at the bottom of the page.

To open this file, we would call the open function. The variable, fileref, now holds a reference to the file object returned by open. When we are finished with the file, we can close it by using the close method. After the file is closed any further attempts to use fileref will result in an error.
```
fileref = open("olympics.txt", "r")
## other code here that refers to variable fileref
fileref.close()
```

### Note

A common mistake is to get confused about whether you are providing a variable name or a string literal as an input to the open function. In the code above, “olympics.txt” is a string literal that should correspond to the name of a file on your computer. If you put something without quotes, like open(x, "r"), it will be treated as a variable name. In this example, x should be a variable that’s already been bound to a string value like “olympics.txt”.
