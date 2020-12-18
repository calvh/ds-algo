class Queue:
    """
    Implementation of a queue using a simulated circular array.
    Not optimized for production use.

    """

    def __init__(self, initial_capacity=3):
        self.queue = [None] * initial_capacity
        self.front = 0  # index to first item
        self.rear = 0  # index to next available spot
        self.count = 0
        self.capacity = initial_capacity

    def enqueue(self, o):
        if self.is_full():
            self.expand_capacity(self.capacity * 2)
        self.queue[self.rear] = o
        self.rear = (self.rear + 1) % (self.capacity)
        self.count += 1

    def dequeue(self):
        result = self.queue[self.front]
        self.queue[self.front] = None
        self.count -= 1
        self.front = (self.front + 1) % self.capacity
        return result

    def expand_capacity(self, new_capacity):
        new_queue = [None] * new_capacity

        for i in range(self.count):
            new_queue[i] = self.queue[self.front + i]

        self.capacity = new_capacity
        self.front = 0
        self.rear = self.count
        self.queue = new_queue

    def first(self):
        return self.queue[self.front]

    def size(self):
        return self.count

    def is_full(self):
        return self.capacity == self.count

    def is_empty(self):
        return self.count == 0

    def __str__(self):
        return str(self.queue)


"""
# test code
q = Queue()

q.enqueue(1)
q.enqueue(1)
q.enqueue(1)
q.enqueue(1)
q.dequeue()
q.dequeue()
print(q.size())
print(q.is_empty())
print(q)
"""