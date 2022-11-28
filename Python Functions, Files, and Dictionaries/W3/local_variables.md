# Variables and parameters are local

An assignment statement in a function creates a local variable for the variable on the left hand side of the assignment operator. It is called local because this variable only exists inside the function and you cannot use it outside. For example, consider again the square function:
```
def square(x):
    y = x * x
    return y

z = square(10)
print(y)
```
When a function is invoked in Codelens, the local scope is separated from global scope by a blue box. Variables in the local scope will be placed in the blue box while global variables will stay in the global frame. If you press the ‘last >>’ button you will see an error message. When we try to use y on line 6 (outside the function) Python looks for a global variable named y but does not find one. This results in the error: Name Error: 'y' is not defined.

The variable y only exists while the function is being executed — we call this its lifetime. When the execution of the function terminates (returns), the local variables are destroyed. Codelens helps you visualize this because the local variables disappear after the function returns. Go back and step through the statements paying particular attention to the variables that are created when the function is called. Note when they are subsequently destroyed as the function returns.

Formal parameters are also local and act like local variables. For example, the lifetime of x begins when square is called, and its lifetime ends when the function completes its execution.

So it is not possible for a function to set some local variable to a value, complete its execution, and then when it is called again next time, recover the local variable. Each call of the function creates new local variables, and their lifetimes expire when the function returns to the caller.

-------------------
Local variables canNOT be referenced outside of the function they were defined in.

What would be the result of running the following code?
```
x = 3 * 2
y = 1

def subtract(z):
    y = 10
    return y - z

print(subtract(x))

4
```
The output is right because the subtract function takes in x as the global variable for the z parameter and puts it into the function. The subtract function uses the local variable y for its return.


What would be the result of running the following code?
```
def adding(x):
    y = 3
    z = y + x + x
    return z

def producing(x):
    z = x * y
    return z

print(producing(adding(4)))
```
There is an error in the code.

There is an error because we reference y in the producing function, but it was defined in adding. Because y is a local variable, we can't use it in both functions without initializing it in both. If we initialized y as 3 in both though, the answer would be 33.


What would be the result of running the following code?
```
x = 9

def adding():
    x+=1
    print(x)

adding()
```
Error, local variable 'x' is referenced before assignment.

This code gives an error because the local variable 'x' was referenced in the local scope before it was assigned a value.



```
v1 += 1
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
NameError: name 'v1' is not defined
    def foo():
        v1 += 1
    foo()
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 2, in foo
UnboundLocalError: local variable 'v1' referenced before assignment
```
In the code above, notice and understand the different error messages. The local variables are created at the same time the local namespace is created. That is any variable that is assigned to anywhere in the function gets added to the local namespace immediately but it will remain unbound until the assignment statement is executed.
