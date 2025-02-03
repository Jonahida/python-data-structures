class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            print(f"Inserted root node: {key}")
        else:
            self._insert(self.root, key)
    
    def _insert(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
                print(f"Inserted node: {key}")
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
                print(f"Inserted node: {key}")
            else:
                self._insert(root.right, key)
    
    def search(self, key):
        if self._search(self.root, key):
            print(f"Node with value {key} found")
        else:
            print(f"Node with value {key} not found")
    
    def _search(self, root, key):
        if root is None:
            return False
        if key == root.value:
            return True
        elif key < root.value:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)
    
    def traverse(self):
        print("In-order traversal: ")
        self._in_order(self.root)
        print()
    
    def _in_order(self, root):
        if root:
            self._in_order(root.left)
            print(root.value, end=" ")
            self._in_order(root.right)
