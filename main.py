from stack import Stack
from queue import Queue
from linked_list import LinkedList
from hash_table import HashTable
from tree import BinaryTree
from trie import Trie
from graph import Graph


def main():
    while True:
        print("\nSelect a Data Structure:")
        print("1. Stack")
        print("2. Queue")
        print("3. Linked List")
        print("4. Hash Table")
        print("5. Binary Tree")
        print("6. Trie")
        print("7. Graph")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            stack_operations()
        elif choice == '2':
            queue_operations()
        elif choice == '3':
            linked_list_operations()
        elif choice == '4':
            hash_table_operations()
        elif choice == '5':
            binary_tree_operations()
        elif choice == '6':
            trie_operations()
        elif choice == '7':
            graph_operations()
        elif choice == '8':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


def stack_operations():
    stack = Stack()
    print("""
    Stack:
    A Stack is a linear data structure that follows the Last In, First Out (LIFO) principle. 
    It means that the last element added to the stack will be the first one to be removed.
    Common operations include Push (to add an element), Pop (to remove the top element), 
    and Peek (to view the top element without removing it).
    
    Features:
    - Simple and efficient.
    - Useful in scenarios such as expression evaluation, backtracking algorithms, and function call management.
    
    Examples of Use:
    - Function Call Stack: The system keeps track of function calls in a stack. The last function called is the first to return.
    - Expression Evaluation: Stacks are used to evaluate expressions in Reverse Polish Notation (RPN), where operators follow operands, making it easier to compute.
    - Undo/Redo Operations: Used in text editors where each action can be pushed onto a stack, and undoing will pop the action off.
    """)
    
    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Go Back")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            item = input("Enter item to push: ")
            stack.push(item)
            stack.display()
        elif choice == '2':
            stack.pop()
            stack.display()
        elif choice == '3':
            stack.peek()
        elif choice == '4':
            stack.display()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


def queue_operations():
    queue = Queue()
    print("""
    Queue:
    A Queue is a linear data structure that follows the First In, First Out (FIFO) principle. 
    This means that the first element added to the queue will be the first one to be removed.
    It supports operations such as Enqueue (to add an element), Dequeue (to remove an element), 
    and Peek (to view the front element without removing it).
    
    Features:
    - Ideal for scenarios where order matters, like scheduling tasks or handling data in a sequential manner.
    - Commonly used in breadth-first search (BFS) algorithms.
    
    Examples of Use:
    - Print Spooler: Printers use queues to manage print jobs. The first document to be sent to the printer is the first to be printed.
    - Task Scheduling: Operating systems use queues to manage tasks for CPU scheduling in a first-come-first-serve manner.
    - Breadth-First Search (BFS): Queues are essential in the BFS algorithm to explore nodes level by level.
    """)
    
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Go Back")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            item = input("Enter item to enqueue: ")
            queue.enqueue(item)
            queue.display()
        elif choice == '2':
            queue.dequeue()
            queue.display()
        elif choice == '3':
            queue.peek()
        elif choice == '4':
            queue.display()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


def linked_list_operations():
    linked_list = LinkedList()
    print("""
    Linked List:
    A Linked List is a linear data structure where elements (called nodes) are stored in a sequence.
    Each node contains data and a reference (or link) to the next node in the sequence. 
    Operations include Insertion (to add a new node), Deletion (to remove a node), and Traversal (to visit each node).
    
    Features:
    - Efficient insertion and deletion of nodes, especially in the middle of the list.
    - Useful in dynamic memory allocation and implementing data structures like stacks and queues.
    
    Examples of Use:
    - Dynamic Memory Allocation: Linked lists are used when the amount of memory needed is unknown at compile time, such as in memory management systems.
    - Implementation of Stacks and Queues: Linked lists can be used to implement both stack and queue data structures efficiently.
    - Navigation Systems: In some scenarios, like doubly linked lists in browser history, a user can move forward and backward between different web pages.
    """)
    
    while True:
        print("\nLinked List Operations:")
        print("1. Insert")
        print("2. Delete")
        print("3. Traverse")
        print("4. Go Back")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            data = input("Enter data to insert: ")
            linked_list.insert(data)
            linked_list.traverse()
        elif choice == '2':
            data = input("Enter data to delete: ")
            linked_list.delete(data)
            linked_list.traverse()
        elif choice == '3':
            linked_list.traverse()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


def hash_table_operations():
    print("""
    Hash Table:
    A Hash Table is a data structure that stores key-value pairs. It provides very efficient methods for insertion, deletion, and searching of data. 
    The key is hashed using a hash function to determine the index where the value will be stored. A common technique for handling collisions is chaining, where each index of the table contains a list of key-value pairs. This makes retrieval, insertion, and deletion operations extremely fast.
    
    Features:
    - Efficient average-case time complexity for insertion, deletion, and search (O(1)).
    - Handles collisions using techniques like chaining or open addressing.
    - Optimized for situations where you need fast lookups by key.
    
    Examples of Use:
    - Database Indexing: Hash tables are used in databases to quickly retrieve records by a unique key (e.g., employee ID, student number).
    - Caching: Hash tables are used in caching systems, where frequently accessed data is stored and retrieved quickly using a hash key.
    - Hash Maps in Programming Languages: In many programming languages like Python, Java, and C++, hash tables are used internally in dictionaries (Python) or hash maps (Java).
    - Password Storage: Hash functions are often used to securely store passwords, with the hash of the password being stored in the database. When a user logs in, their password is hashed and compared with the stored hash.
    """)
    
    size = int(input("Enter size of hash table: "))
    hash_table = HashTable(size)
    
    while True:
        print("\nHash Table Operations:")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display")
        print("5. Go Back")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            key = input("Enter key to insert: ")
            value = input("Enter value to insert: ")
            hash_table.insert(key, value)
            hash_table.display()
        elif choice == '2':
            key = input("Enter key to search: ")
            hash_table.search(key)
        elif choice == '3':
            key = input("Enter key to delete: ")
            hash_table.delete(key)
            hash_table.display()
        elif choice == '4':
            hash_table.display()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


def binary_tree_operations():
    tree = BinaryTree()
    print("""
    Binary Tree:
    A Binary Tree is a hierarchical data structure consisting of nodes, where each node has at most two children, 
    typically referred to as the left and right children. Common operations include Insertion (to add a node), 
    Search (to find a node), and Traversal (to visit each node).
    
    Features:
    - Can be used to implement searching algorithms like binary search.
    - Forms the basis for more advanced tree structures like AVL trees, red-black trees, and heaps.
    
    Examples of Use:
    - Binary Search Trees (BST): Used in applications where fast lookups, insertions, and deletions are needed. It's commonly used in databases.
    - Expression Parsing: Used in evaluating arithmetic expressions in compilers and interpreters.
    - Priority Queues (Heaps): Binary trees are used to implement heap data structures for efficient priority queue operations.
    """)
    
    while True:
        print("\nBinary Tree Operations:")
        print("1. Insert")
        print("2. Search")
        print("3. Traverse")
        print("4. Go Back")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            value = int(input("Enter value to insert: "))
            tree.insert(value)
            tree.traverse()
        elif choice == '2':
            value = int(input("Enter value to search: "))
            tree.search(value)
        elif choice == '3':
            tree.traverse()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


def trie_operations():
    trie = Trie()
    print("""
    Trie:
    A Trie (also known as a Prefix Tree) is a tree-like data structure used to store a dynamic set of strings.
    Each node represents a character of a string, and the path from the root to the node represents a prefix of some string.
    Operations include Insert (to add a string), Search (to find a string), Delete (to remove a string), and Display.
    
    Features:
    - Efficient for storing strings, especially for prefix-based searches.
    - Commonly used for autocomplete systems and dictionaries.
    
    Examples of Use:
    - Autocomplete Systems: Used in search engines and mobile keyboards to suggest words based on user input.
    - Spell Checking: Tries are used for efficient dictionary lookups in spell checkers.
    - IP Routing: Tries can be used in routing tables where IP addresses are stored in a prefix-based manner.
    """)
    
    while True:
        print("\nTrie Operations:")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display")
        print("5. Go Back")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            word = input("Enter word to insert: ")
            trie.insert(word)
            trie.display()
        elif choice == '2':
            word = input("Enter word to search: ")
            trie.search(word)
        elif choice == '3':
            word = input("Enter word to delete: ")
            trie.delete(word)
            trie.display()
        elif choice == '4':
            trie.display()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


def graph_operations():
    graph = Graph()
    print("""
    Graph:
    A Graph is a collection of nodes (vertices) and edges, where the edges connect pairs of nodes.
    It can be used to represent various real-world relationships like social networks, transportation systems, etc.
    Common operations include Add Vertex (to add a node), Add Edge (to create a connection between two nodes), and Display.
    
    Features:
    - Can represent complex relationships in the form of networks or maps.
    - Can be used to implement algorithms like Depth-First Search (DFS), Breadth-First Search (BFS), and Dijkstra’s algorithm.
    
    Examples of Use:
    - Social Networks: Graphs are used to represent users as nodes and relationships as edges (e.g., Facebook, Twitter).
    - Routing Algorithms: Used in applications like Google Maps to find the shortest path between locations.
    - Recommendation Systems: Graphs are used in collaborative filtering systems, where edges represent similarities between items.
    """)
    
    while True:
        print("\nGraph Operations:")
        print("1. Add Vertex")
        print("2. Add Edge")
        print("3. Display")
        print("4. Go Back")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            vertex = input("Enter vertex to add: ")
            graph.add_vertex(vertex)
            graph.display()
        elif choice == '2':
            vertex1 = input("Enter first vertex: ")
            vertex2 = input("Enter second vertex: ")
            graph.add_edge(vertex1, vertex2)
            graph.display()
        elif choice == '3':
            graph.display()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

