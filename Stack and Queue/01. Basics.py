# STACK  BASICS

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "Cannot pop, stack is empty"
        x = self.items.pop()
        return x

    def top(self):
        if len(self.items) == 0:
            return "Cannot top, stack is empty"
        return self.items[-1]

    def size(self):
        return len(self.items)

# ----------------------------------------------------------------

# QUEUE BASICS 

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            print("dequeue from empty queue")
            return
        x = self.items.pop(0)
        return x

    def front(self):
        if len(self.items) == 0:
            print("Cannot peek, queue is empty")
            return
        return self.items[0]

    def rear(self):
        if len(self.items) == 0:
            print("Cannot read, queue is empty")
            return
        return self.items[-1]

    def size(self):
        return len(self.items)



# Implement Stack using Queue:
# ALGO : push(x)
#         1.Add at Last (Enqueue the element x at the end of the queue).
#         2.Rotate whole List by n-1 (Move the first n-1 elements one by one from the front to the back of the queue).
#        pop()
#           Remove 0th Index (Dequeue/remove the element from the front of the queue).

from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, item):
        self.queue.append(item)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if len(self.queue) == 0:
            return "Stack is empty"
        return self.queue.popleft()

    def peek(self):
        if len(self.queue) == 0:
            return "Stack is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)



# Algorithm (Implement Queue using Two Stacks)
# push(x)
#    1. Transfer all elements from st1 to st2.
#    2. Insert element x into st1.
#    3. Transfer all elements back from st2 to st1.
# pop()
#      Pop and return the top element of st1.peek()Return the top element of st1.

class StackQueue:
    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x):
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(x)
        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self):
        if not self.st1:
            print("Stack is empty")
            return -1  
        top_element = self.st1.pop()
        return top_element

    def peek(self):
        if not self.st1:
            print("Stack is empty")
            return -1
        return self.st1[-1]

    def is_empty(self):
        return not self.st1
