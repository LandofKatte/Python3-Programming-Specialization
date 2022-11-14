# Chained conditionals

Python provides an alternative way to write nested selection such as the one shown in the previous section. This is sometimes referred to as a chained conditional.
```
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y must be equal")
```
The flow of control can be drawn in a different orientation but the resulting pattern is identical to the one shown above.

![image](https://user-images.githubusercontent.com/103328611/201705208-358df7b6-9de3-4b59-b7ec-db0e261c0752.png)

elif is an abbreviation of else if. Again, exactly one branch will be executed. There is no limit of the number of elif statements but only a single (and optional) final else statement is allowed and it must be the last branch in the statement.

![image](https://user-images.githubusercontent.com/103328611/201705292-51390465-f909-446f-9bb7-92567a7bfbd5.png)

Each condition is checked in order. If the first is false, the next is checked, and so on. If one of them is true, the corresponding branch executes, and the statement ends. Even if more than one condition is true, only the first true branch executes.

Here is the same program using elif.
```
x = 10
y = 10

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y must be equal")
    
x and y must be equal
```

The following image highlights different kinds of valid conditionals that can be used. Though there are other versions of conditionals that Python can understand (imagine an if statement with twenty elif statements), those other versions must follow the same order as seen below.

![image](https://user-images.githubusercontent.com/103328611/201705523-691ca51a-e11a-418a-aaf4-0d623e06f844.png)
