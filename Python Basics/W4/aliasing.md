# Aliasing

Since variables refer to objects, if we assign one variable to another, both variables refer to the same object:
```
a = [81, 82, 83]
b = a
print(a is b)

True
```

In this case, the reference diagram looks like this:

![image](https://user-images.githubusercontent.com/103328611/202057465-e3f1658b-e25d-4c52-8dd8-0cf65b893b81.png)

Because the same list has two different names, a and b, we say that it is aliased. Changes made with one alias affect the other. In the codelens example below, you can see that a and b refer to the same list after executing the assignment statement b = a.
```
a = [81,82,83]
b = [81,82,83]
print(a is b)

b = a
print(a == b)
print(a is b)

b[0] = 5
print(a)

False
True
True
[5, 82, 83]
```

Although this behavior can be useful, it is sometimes unexpected or undesirable. In general, it is safer to avoid aliasing when you are working with mutable objects. Of course, for immutable objects, there’s no problem. That’s why Python is free to alias strings and integers when it sees an opportunity to economize.
