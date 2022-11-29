# Anonymous functions with lambda expressions

To further drive home the idea that we are passing a function object as a parameter to the sorted object, let’s see an alternative notation for creating a function, a lambda expression. The syntax of a lambda expression is the word “lambda” followed by parameter names, separated by commas but not inside (parentheses), followed by a colon and then an expression. lambda arguments: expression yields a function object. This unnamed object behaves just like the function object constructed below.
```
def function(arguments):
    return expression
```   
Equivalent to:
```
function = lambda args:return_value
```
anonymous function object:
lambda args:return_value

```
def f(x):
    return x - 1

print(f)
print(type(f))
print(f(3))

print(lambda x: x-2)
print(type(lambda x: x-2))
print((lambda x: x-2)(6))

<function f>
<class 'function'>
2
<function <lambda>>
<class 'function'>
4
```

Note the paralells between the two. At line 4, f is bound to a function object. Its printed representation is “<function f>”. At line 8, the lambda expression produces a function object. Because it is unnamed (anonymous), its printed representation doesn’t include a name for it, “<function <lambda>>”. Both are of type ‘function’.

A function, whether named or anonymous, can be called by placing parentheses () after it. In this case, because there is one parameter, there is one value in parentheses. This works the same way for the named function and the anonymous function produced by the lambda expression. The lambda expression had to go in parentheses just for the purposes of grouping all its contents together. Without the extra parentheses around it on line 10, the interpreter would group things differently and make a function of x that returns x - 2(6).

Some students find it more natural to work with lambda expressions than to refer to a function by name. Others find the syntax of lambda expressions confusing. It’s up to you which version you want to use though you will need to be able to read and understand lambda expressions that are written by others. In all the examples below, both ways of doing it will be illustrated.

Say we want to create a function that takes a string and returns the last character in that string. What might this look like with the functions you’ve used before?
  
