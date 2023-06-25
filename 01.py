# Implement a stack using a list in Python. Include the necessary methods such as push, pop, and isEmpty.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Cannot pop from an empty stack.")
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

stack = Stack()
print(stack.isEmpty())

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.isEmpty())

print(stack.pop())  
print(stack.pop())  
print(stack.pop())

print(stack.isEmpty())  
