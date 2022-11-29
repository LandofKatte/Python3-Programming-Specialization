# Break and Continue

Python provides ways for us to control the flow of iteration with a two keywords: break and continue.

break allows the program to immediately ‘break out’ of the loop, regardless of the loop’s conditional structure. This means that the program will then skip the rest of the iteration, without rechecking the condition, and just goes on to the next outdented code that exists after the whole while loop.

![image](https://user-images.githubusercontent.com/103328611/204646850-70830d74-a207-4322-928c-dc8b3e6de05d.png)

```
while True:
    print("this phrase will always print")
    break
    print("Does this phrase print?")

print("We are done with the while loop.")

this phrase will always print
We are done with the while loop.
```

We can see here how the print statement right after break is not executed. In fact, without using break, we have no way to stop the while loop because the condition is always set to True!

continue is the other keyword that can control the flow of iteration. Using continue allows the program to immediately “continue” with the next iteration. The program will skip the rest of the iteration, recheck the condition, and maybe does another iteration depending on the condition set for the while loop.

![image](https://user-images.githubusercontent.com/103328611/204647047-afaf0b20-c75f-477e-805c-344c5c775aff.png)

```
x = 0
while x < 10:
    print("we are incrementing x")
    if x % 2 == 0:
        x += 3
        continue
    if x % 3 == 0:
        x += 5
    x += 1
print("Done with our loop! X has the value: " + str(x))

we are incrementing x
we are incrementing x
we are incrementing x
Done with our loop! X has the value: 15
```
Notice in the first iteration how the program doesn’t move to evaluate the divisible by 3 statment or add 1 to x. Instead, it continues to the next iteration.
