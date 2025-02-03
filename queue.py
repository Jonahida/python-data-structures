class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Item enqueued: {item}")
    
    def dequeue(self):
        if not self.is_empty():
            dequeued_item = self.queue.pop(0)
            print(f"Item dequeued: {dequeued_item}")
        else:
            print("Queue is empty.")
    
    def peek(self):
        if not self.is_empty():
            print(f"Front item: {self.queue[0]}")
        else:
            print("Queue is empty.")
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def display(self):
        print("Queue:", self.queue)
