#ch12

#Write a function named num_test that takes a number as input. If the number is greater than 10, the function should return “Greater than 10.” If the number is less than 10, the function should return “Less than 10.” If the number is equal to 10, the function should return “Equal to 10.”

#CODE HERE


#Write a function that will return the number of digits in an integer.

def numDigits(n):
    # your code here
    n_str = str(n)
    return len(n_str)


print(numDigits(50))
print(numDigits(20000))
print(numDigits(1))

2
5
1

#Write a function that reverses its string argument.

def reverse(astring):
    # CODE HERE

#Write a function that mirrors its string argument, generating a string containing the original string and the string backwards.

def reverse(mystr):
    reversed = ''
    for char in mystr:
        reversed = char + reversed
    return reversed

def mirror(mystr):
    return mystr + reverse(mystr)

assert mirror('good') == 'gooddoog'
assert mirror('Python') == 'PythonnohtyP'
assert mirror('') == ''
assert mirror('a') == 'aa'

#Write a function that removes all occurrences of a given letter from a string.

def remove_letter(theLetter, theString):
#CODE HERE



#Although Python provides us with many list methods, it is good practice and very instructive to think about how they are implemented. Implement a Python function that works like the following:

   # count

   # in

   # reverse

   # index

   # insert

def insert(obj, index, lst):
    newlst = []
    for i in range(len(lst)):
        if i == index:
            newlst.append(obj)
        newlst.append(lst[i])
    return newlst

lst = [0, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
print(count(1, lst))
print(is_in(4, lst))
print(reverse(lst))
print(index(2, lst))
print(insert('cat', 4, lst))

2
True
[9, 8, 7, 6, 5, 4, 3, 2, 2, 1, 1, 0]
3
[0, 1, 1, 2, 'cat', 2, 3, 4, 5, 6, 7, 8, 9]


#Write a function replace(s, old, new) that replaces all occurences of old with new in a string s:
    test(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')

s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
test(replace(s, 'om', 'am'),
       'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!')

test(replace(s, 'o', 'a'),
       'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!')

#Hint: use the split and join methods.

def replace(s, old, new):
    #CODE HERE
    
____________________________________________________________________________
#ch13

#Fill in the left side of line 7 so that the following code runs without error

def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a

#EDIT THIS LINE = circleInfo(10)
print("area is " + str(area))
print("circumference is " + str(circ))


#Use a for loop to print out the last name, year of birth, and city for each of the people. (There are multiple ways you could do this. Try out some code and see what happens!)

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
claude = ("Claude", "Shannon", 1916, "A Mathematical Theory of Communication", 1948, "Mathematician", "Petoskey, Michigan")
alan = ("Alan", "Turing", 1912, "Computing machinery and intelligence", 1950, "Mathematician", "London, England")

people = [julia, claude, alan]
#EDIT CODE
