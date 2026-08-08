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


# INFIX TO POSTFIX CONVERSION

class Solution:

    def precedence(self, ch):
        if ch == "+" or ch == "-":
            return 1
        if ch == "*" or ch == "/":
            return 2
        if ch == "^":
            return 3
        return 0

    def InfixtoPostfix(self, s):
        stack = []
        result = []

        for char in s:
            if (
                ("a" <= char <= "z")
                or ("A" <= char <= "Z")
                or ("0" <= char <= "9")
            ):
                result.append(char)
            # If character is '(', push it to the stack
            elif char == "(":
                stack.append(char)
            # If character is ')', pop until '(' is encountered
            elif char == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()
            # If character is an operator
            else:
                while stack and self.precedence(
                    stack[-1]
                ) >= self.precedence(char):
                    result.append(stack.pop())
                stack.append(char)

        # Pop remaining operators from the stack
        while stack:
            result.append(stack.pop())

        return "".join(result)


# IINFIX TO PREFIX
# 1. Reverse the infix
# 2. Infix to Postfix
# 3.Reverse the answer

def infixToPrefix(self, s):
    s = s[::-1]

    s = (
        s.replace("(", "temp")
        .replace(")", "(")
        .replace("temp", ")")
    )

    stack = []
    result = []

    for char in s:
        if (
            ("a" <= char <= "z")
            or ("A" <= char <= "Z")
            or ("0" <= char <= "9")
        ):
            result.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                result.append(stack.pop())
            stack.pop()  # Pop '('
        else:
            while stack and self.precedence(
                stack[-1]
            ) > self.precedence(char):
                result.append(stack.pop())
            stack.append(char)

    while stack:
        result.append(stack.pop())

    return "".join(result[::-1])


# POSTFIX TO INFIX 

class Solution:

    def postToInfix(self, s):
        # Stack to store operands
        stack = []

        for char in s:
            # If character is an operand, push it to the stack
            if char.isalnum():
                stack.append(char)
            else:
                # Pop two operands
                operand2 = stack.pop()
                operand1 = stack.pop()

                # Combine operands with the operator
                new_expr = f"({operand1}{char}{operand2})"

                # Push the result back onto the stack
                stack.append(new_expr)

        # The final element in the stack is the infix expression
        return stack[-1]


# PREFIX TO INFIX

class Solution:

    def preToInfix(self, s):
        # Stack to store operands
        stack = []

        for char in s[::-1]:
            # If character is an operand, push it to the stack
            if char.isalnum():
                stack.append(char)
            else:
                # Pop two operands but with reversed order
                operand1 = stack.pop()
                operand2 = stack.pop()

                # Combine operands with the operator
                new_expr = f"({operand1}{char}{operand2})"

                # Push the result back onto the stack
                stack.append(new_expr)

        # The final element in the stack is the infix expression
        return stack[-1]


# POSTFIX TO PREFIX

class Solution:

    def postToPre(self, s):
        # Stack to store operands
        stack = []

        # Process each character in postfix expression
        for char in s:
            # If the character is an operand, push it to the stack
            if char.isalnum():
                stack.append(char)
            else:
                # Pop two operands from the stack
                operand2 = stack.pop()
                operand1 = stack.pop()

                # Combine the operands with the operator in prefix form
                new_expr = f"{char}{operand1}{operand2}"

                # Push the result back onto the stack
                stack.append(new_expr)

        # The final element in the stack is the prefix expression
        return stack[-1]


# PREFIX TO POSTFIX

def preToPost(self, s):
    # Stack to store operands
    stack = []

    # Traverse the prefix expression from right to left using index
    n = len(s)
    for i in range(n - 1, -1, -1):  # Reverse iteration using index
        char = s[i]

        # If the character is an operand, push it to the stack
        if char.isalnum():
            stack.append(char)
        else:
            # Pop two operands from the stack
            operand1 = stack.pop()
            operand2 = stack.pop()

            # Combine the operands with the operator in postfix form
            new_expr = operand1 + operand2 + char

            # Push the result back onto the stack
            stack.append(new_expr)

    # The final element in the stack is the postfix expression
    return stack[-1]

