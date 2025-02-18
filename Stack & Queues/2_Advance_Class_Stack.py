class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)  # Add element to the top
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # Remove and return top element
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]  # Return top element without removing
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0  # Check if stack is empty
    
    def size(self):
        return len(self.stack)  # Return the number of elements


s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.pop())   
print(s.peek())  
print(s.is_empty())  
# from collections import deque
# stack = deque()
# stack.append(6)
# stack.append(20)
# stack.append(30)
# stack.append(40)
# stack.pop()
# print(stack)
