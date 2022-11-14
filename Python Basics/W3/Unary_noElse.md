# Omitting the else Clause: Unary Selection

Another form of the if statement is one in which the else clause is omitted entirely. This creates what is sometimes called unary selection. In this case, when the condition evaluates to True, the statements are executed. Otherwise the flow of execution continues to the statement after the body of the if.

Flowchart of an if with no else

![image](https://user-images.githubusercontent.com/103328611/201703623-4a844282-c8a2-4fa0-9d48-b172591157dc.png)

```
x = 10
if x < 0:
    print("The negative number ",  x, " is not valid here.")
print("This is always printed")

This is always printed
```
