## Queues
Another fundamental data structure is the queue
It's a collection of objects that are inserted and removed according to the first-in first-out principle.
That is element can be inserted at any time but only the element that has been in the queue the longest can be next removed.
Queues are also used by computing devices such as a network printer, or a Web server responding to requests
The queue abstract data type (ADT) supports the following two fundamental methods for a queue Q:
Q.enqueue(e): Add element e to the back of queue Q
Q.dequeue() Remove and return the first element from queue Q: er
The queue ADT also includes the following supporting methods
Q.first(): Return a reference to the element at the front of queue Q without removing it: an error occurs if the queue is empty.
Q.is_empty(): Return True if queue Q does not contain any elements.
len(Q): Return the number of elements in queue Q: in Python, we implement this with the special method __len__.

Operation         Return Value     first ←Q←last
Q.enqueue(5)          -                 [5]
Q.enqueue(3)          –                 [5, 3]
len(Q)                2                 [5, 3]
Q.dequeue( )          5                 [3]
Q.is empty( )         False             [3]
Q.dequeue( )          3                 [ ]
Q.is empty( )         True              [ ]
Q.dequeue( )          “error”           [ ]
Q.enqueue(7)          –                 [7]
Q.enqueue(9)          –                 [7, 9]
Q.first()             7                 [7, 9]
Q.enqueue(4)          –                 [7, 9, 4]
len(Q)                3                 [7, 9, 4]
Q.dequeue( )          7                 [9, 4]

# A python queue implementation
A complete implementation of a queue ADT using a Python list in circular fashion is presented in queueImplementation.py file.
The queue class maintains the following three instances:
_data: is a reference to a list instance with fixed capacity
_size: Is an integer representing the current number of elements stored in the queue
_font: Is an integer that represents the index within _data of the first element of the queue.

# The deque abstract data type
D.add first(e): Add element e to the front of deque D.
D.add last(e): Add element e to the back of deque D.
D.delete first( ): Remove and return the first element from deque D;
an error occurs if the deque is empty.
D.delete last( ): Remove and return the last element from deque D;
an error occurs if the deque is empty.
D.first(): Return (but do not remove) the first element of deque D;
an error occurs if the deque is empty.
D.last(): Return (but do not remove) the last element of deque D;
an error occurs if the deque is empty.
D.is empty( ): Return True if deque D does not contain any elements.
len(D): Return the number of elements in deque D; in Python, we implement this with the special method len .