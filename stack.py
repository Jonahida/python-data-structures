class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
        print(f"Item pushed: {item}")
    
    def pop(self):
        if not self.is_empty():
            popped_item = self.stack.pop()
            print(f"Item popped: {popped_item}")
        else:
            print("Stack is empty.")
    
    def peek(self):
        if not self.is_empty():
            print(f"Top item: {self.stack[-1]}")
        else:
            print("Stack is empty.")
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def display(self):
        print("Stack:", self.stack)
