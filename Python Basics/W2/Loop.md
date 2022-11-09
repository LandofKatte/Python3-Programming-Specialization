# Loop

A basic building block of all programs is to be able to repeat some code over and over again. We refer to this repetitive idea as iteration. In this section, we will explore some mechanisms for basic iteration.

In Python, the for statement allows us to write programs that implement iteration. As a simple example, let’s say we have some friends, and we’d like to send them each an email inviting them to our party. We don’t quite know how to send email yet, so for the moment we’ll just print a message for each friend.
```
for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    print("Hi", name, "Please come to my party on Saturday!")
    
Hi Joe Please come to my party on Saturday!
Hi Amy Please come to my party on Saturday!
Hi Brad Please come to my party on Saturday!
Hi Angelina Please come to my party on Saturday!
Hi Zuki Please come to my party on Saturday!
Hi Thandi Please come to my party on Saturday!
Hi Paris Please come to my party on Saturday!
```

Take a look at the output produced when you press the run button. There is one line printed for each friend. Here’s how it works:

   name in this for statement is called the loop variable or, alternatively, the iterator variable.

   The list of names in the square brackets is the sequence over which we will iterate.

   Line 2 is the loop body. The loop body is always indented. The indentation determines exactly what statements are “in the loop”. The loop body is performed one time for each name in the list.

   On each iteration or pass of the loop, first a check is done to see if there are still more items to be processed. If there are none left (this is called the terminating condition of the loop), the loop has finished. Program execution continues at the next statement after the loop body.

   If there are items still to be processed, the loop variable is updated to refer to the next item in the list. This means, in this case, that the loop body is executed here 7 times, and each time name will refer to a different friend.
   
   At the end of each execution of the body of the loop, Python returns to the for statement, to see if there are more items to be handled.

The overall syntax is for <loop_var_name> in <sequence>:

    Between the words for and in, there must be a variable name for the loop variable. You can’t put a whole expression there.

    A colon is required at the end of the line

    After the word in and before the colon is an expression that must evaluate to a sequence (e.g, a string or a list or a tuple). It could be a literal, or a variable name, or a more complex expression.
_______________________________________________
  
## Flow of Execution of the for Loop

As a program executes, the interpreter always keeps track of which statement is about to be executed. We call this the control flow, or the flow of execution of the program. When humans execute programs, they often use their finger to point to each statement in turn. So you could think of control flow as “Python’s moving finger”.

Control flow until now has been strictly top to bottom, one statement at a time. We call this type of control sequential. Sequential flow of control is always assumed to be the default behavior for a computer program. The for statement changes this.

Flow of control is often easy to visualize and understand if we draw a flowchart. This flowchart shows the exact steps and logic of how the for statement executes.
  
![image](https://user-images.githubusercontent.com/103328611/200932651-0d095768-9ede-473c-8971-f71671019ac5.png)

## While Loop  

While loops may not seem to be necessary when you’re iterating over a few items, it is extremely helpful when iterating over lots of items. Imagine if you needed to change what happened in the code block. On the left, when you use iteration, this is easy. On the right, when you have hard coded the process, this is more difficult.

![image](https://user-images.githubusercontent.com/103328611/200933065-da4f70cf-479b-464f-ae63-c534ef50ce4c.png)
