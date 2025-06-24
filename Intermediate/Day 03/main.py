# Coding With Kien - 365 Days of Python Programming
# Intermediate - Day 03

# Implement a basic queue

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(f"Queue size: {q.size()}")
print(f"Dequeued item: {q.dequeue()}")
print(f"Dequeued item: {q.dequeue()}")
print(f"Queue size: {q.size()}")

# Output:
# Queue size: 3
# Dequeued item: 1
# Dequeued item: 2
# Queue size: 1 