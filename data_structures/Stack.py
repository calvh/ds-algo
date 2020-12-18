class Stack:
    """
    Implementation of a stack using a simulated array.
    Not optimized for production use.

    """

    def __init__(self, initial_capacity=3):
        self.stack = [None] * initial_capacity
        self.top = -1  # index to top of stack
        self.capacity = initial_capacity

    def push(self, o):
        if self.is_full():
            self.expand_capacity(self.capacity * 2)
        self.top += 1
        self.stack[self.top] = o

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty.")
        result = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return result

    def expand_capacity(self, new_capacity):
        new_stack = [None] * new_capacity

        for i in range(self.top + 1):
            new_stack[i] = self.stack[i]

        self.capacity = new_capacity
        self.stack = new_stack

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty.")
        return self.stack[self.top]

    def size(self):
        return self.top + 1

    def is_full(self):
        return self.top + 1 == self.capacity

    def is_empty(self):
        return self.top == -1

    def __str__(self):
        return str(self.stack)


"""
# test code
s = Stack()
s.push(1)
s.push(1)
s.push(1)
s.pop(1)
s.pop(1)

print(s.size())
print(s.is_empty())
print(s)
"""