class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Item inserted: {data}")
    
    def delete(self, data):
        temp = self.head
        if temp and temp.data == data:
            self.head = temp.next
            print(f"Item deleted: {data}")
            return
        
        prev = None
        while temp and temp.data != data:
            prev = temp
            temp = temp.next
        
        if temp is None:
            print(f"Item {data} not found.")
            return
        
        prev.next = temp.next
        print(f"Item deleted: {data}")
    
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
