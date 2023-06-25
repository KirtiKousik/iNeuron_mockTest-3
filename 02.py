# Implement a queue using a list in Python. Include the necessary methods such as enqueue, dequeue, and isEmpty.

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0

queue = Queue()
print(queue.isEmpty())  

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.isEmpty())  

print(queue.dequeue())  
print(queue.dequeue())  
print(queue.dequeue())  

print(queue.isEmpty())  