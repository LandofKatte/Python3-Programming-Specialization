# Functions can call other functions (Composition)

It is important to understand that each of the functions we write can be used and called from other functions we write. This is one of the most important ways that computer programmers take a large problem and break it down into a group of smaller problems. This process of breaking a problem into smaller subproblems is called functional decomposition.

Here’s a simple example of functional decomposition using two functions. The first function called square simply computes the square of a given number. The second function called sum_of_squares makes use of square to compute the sum of three numbers that have been squared.
```
def square(x):
	    y = x * x
	    return y
	
def sum_of_squares(x,y,z):
	    a = square(x)
	    b = square(y)
	    c = square(z)
	
	    return a+b+c
	
a = -5
b = 2
c = 10
result = sum_of_squares(a,b,c)
print(result)
```

Even though this is a pretty simple idea, in practice this example illustrates many very important Python concepts, including local and global variables along with parameter passing. Note that the body of square is not executed until it is called from inside the sum_of_squares function for the first time on line 6.

Also notice that when square is called (at Step 8, for example), there are two groups of local variables, one for square and one for sum_of_squares. Each group of local variables is called a stack frame. The variables x, and y are local variables in both functions. These are completely different variables, even though they have the same name. Each function invocation creates a new frame, and variables are looked up in that frame. Notice that at step 9, y has the value 25 is one frame and 2 in the other.

What happens when you to refer to variable y on line 3? Python looks up the value of y in the stack frame for the square function. If it didn’t find it there, it would go look in the global frame.

Let’s use composition to build up a little more useful function. Recall from the dictionaries chapter that we had a two-step process for finding the letter that appears most frequently in a text string:

    Accumulate a dictionary with letters as keys and counts as values. See example.

    Find the best key from that dictionary. See example.

We can make functions for each of those and then compose them into a single function that finds the most common letter.

```
def most_common_letter(s):
    frequencies = count_freqs(s)
    return best_key(frequencies)

def count_freqs(st):
    d = {}
    for c in st:
        if c not in d:
             d[c] = 0
        d[c] = d[c] + 1
    return d

def best_key(dictionary):
    ks = dictionary.keys()
    best_key_so_far = list(ks)[0]  # Have to turn ks into a real list before using [] to select an item
    for k in ks:
        if dictionary[k] > dictionary[best_key_so_far]:
            best_key_so_far = k
    return best_key_so_far

print(most_common_letter("abbbbbbbbbbbccccddddd"))

b
```

Write two functions, one called addit and one called mult. addit takes one number as an input and adds 5. mult takes one number as an input, and multiplies that input by whatever is returned by addit, and then returns the result.
```
def addit(num):
    sum = num + 5
    return sum

def mult(num):
    result = num * addit(num)
    return result
```
