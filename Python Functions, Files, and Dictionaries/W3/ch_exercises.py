#Write a function named num_test that takes a number as input. If the number is greater than 10, the function should return “Greater than 10.” If the number is less than 10, the function should return “Less than 10.” If the number is equal to 10, the function should return “Equal to 10.”




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
