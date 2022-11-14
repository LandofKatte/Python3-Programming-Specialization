# Conditional Execution: Binary Selection

In order to write useful programs, we almost always need the ability to check conditions and change the behavior of the program accordingly. Selection statements, sometimes also referred to as conditional statements, give us this ability. The simplest form of selection is the if statement. This is sometimes referred to as binary selection since there are two possible paths of execution.

```
x = 15

if x % 2 == 0:
    print(x, "is even")
else:
    print(x, "is odd")
    
15 is odd
```

The syntax for an if statement looks like this:

if BOOLEAN EXPRESSION:
    STATEMENTS_1        # executed if condition evaluates to True
else:
    STATEMENTS_2        # executed if condition evaluates to False

The boolean expression after the if statement is called the condition. If it is true, then the indented statements get executed. If not, then the statements indented under the else clause get executed.

Flowchart of a if statement with an else

![image](https://user-images.githubusercontent.com/103328611/201699762-ecba767e-9318-45a4-a609-c204b0e6a647.png)

As with the function definition from the last chapter and other compound statements like for, the if statement consists of a header line and a body. The header line begins with the keyword if followed by a boolean expression and ends with a colon (:).

The indented statements that follow are called a block. The first unindented statement marks the end of the block.

Each of the statements inside the first block of statements is executed in order if the boolean expression evaluates to True. The entire first block of statements is skipped if the boolean expression evaluates to False, and instead all the statements under the else clause are executed.

There is no limit on the number of statements that can appear under the two clauses of an if statement, but there has to be at least one statement in each block.
