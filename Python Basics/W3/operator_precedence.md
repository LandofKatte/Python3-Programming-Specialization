# Precedence of Operators

Arithmetic operators take precedence over logical operators. Python will always evaluate the arithmetic operators first (** is highest, then multiplication/division, then addition/subtraction). Next comes the relational operators. Finally, the logical operators are done last. This means that the expression x*5 >= 10 and y-6 <= 20 will be evaluated so as to first perform the arithmetic and then check the relationships. The and will be done last. Many programmers might place parentheses around the two relational expressions, (x*5 >= 10) and (y-6 <= 20). It is not necessary to do so, but causes no harm and may make it easier for people to read and understand the code.

The following table summarizes the operator precedence from highest to lowest. A complete table for the entire language can be found in the Python Documentation.

| Level | Category | Operators |
|--|--|--|
| 7(high) | exponent | ** |
| 6 | multiplication | *,/,//,% |
| 5 | addition | +,- |
| 4 | relational | ==,!=,<=,>=,>,< |
| 3 | logical | not |
| 2 | logical | and |
| 1(low) | logical | or |

#### Common Mistake!

Students often incorrectly combine the in and or operators. For example, if they want to check that the letter x is inside of either of two variables then they tend to write it the following way: 'x' in y or z

Written this way, the code would not always do what the programmer intended. This is because the in operator is only on the left side of the or statement. It doesn’t get implemented on both sides of the or statement. In order to properly check that x is inside of either variable, the in operator must be used on both sides which looks like this:

'x' in y or 'x' in z
