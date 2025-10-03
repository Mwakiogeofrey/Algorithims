## Stack
A stack is a colllection of objects that are insered and removed according to the last-in, firs-out(LIFO) principle.
The user may inser objects ino sack at any time, but may only access or remove the most recently inserted object that remains at the so-called top of the stack 
Stack are a fundamental data structures, tey are used in many applications including the following:
Internet Web browser store the addresses of recently visited sites in a stack, Every time a user visits a new stie, the site address is pushed onto the stack addresses. The browser then allows the user to pop back to previously visited sites using the back button
Text editors usually provide an undo mechanism that cancels recent operaions and reverts former states of a document. This undo operation can be accomplished by keeping text changes in a stack. 

# The stack abstract data type
A stack is an abstract data type(ADT) such that an instance S supports the following two methods:
S.push(e): Add element e to the top of stack S
S.pop: Remove and return the top element from the stack S, an error occurs if the stack is empty.
S.top(): Return a reference to the  top element of of stack, without removing it: an error occurs if the stack is empty.
S.is_empty(): Return True if stack S does not contain any elements 
len(S): Return the number of elements in stack S; in Python we implement this with the special __len__. 
we can implemen a sack quie easil b soring i's elemens in a Python list

# Implementing a stack using a python list
We use the adapter design pattern to define an ArrayStack class that uses an underlying Python list for storage
Check out arrayStack.py

# Reversing data using a stack
A stack can be used as a general tool to reverse a data sequence.
This can be accomplished by reading each line and pushing it onto a stack, and then writng the lines in the order they are popped, An implementation of such peocess is given in reverseString.py file.

# Matching Parenthesis and HTMLTags
In this section, we explore two related applications of the stack
Each opening symbol must match its corresponding closing symbol.
 Correct: ( )(( )){([( )])}
• Correct: ((( )(( )){([( )])}))
• Incorrect: )(( )){([( )])}
• Incorrect: ({[ ])}
• Incorrect: (

# Algorithm for matching delimiters
An important task when processing arithmetic expressions is to make sure their delimiting symbol match up correctly.\
Checkout delimeters.py
