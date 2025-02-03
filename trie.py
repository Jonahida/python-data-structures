class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        print(f"Inserted word: {word}")
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                print(f"Word {word} not found.")
                return False
            node = node.children[char]
        if node.is_end_of_word:
            print(f"Word {word} found.")
            return True
        else:
            print(f"Word {word} not found.")
            return False
    
    def delete(self, word):
        if self._delete(self.root, word):
            print(f"Deleted word: {word}")
        else:
            print(f"Word {word} not found.")
    
    def _delete(self, node, word):
        if not word:
            if node.is_end_of_word:
                node.is_end_of_word = False
                return len(node.children) == 0
            return False
        
        char = word[0]
        if char not in node.children:
            return False
        
        can_delete_current_node = self._delete(node.children[char], word[1:])
        
        if can_delete_current_node:
            del node.children[char]
            return len(node.children) == 0
        
        return False
    
    def display(self):
        print("Trie structure:")
        self._print_trie(self.root, "")
    
    def _print_trie(self, node, prefix):
        if node.is_end_of_word:
            print(f"Word: {prefix}")
        for char, child in node.children.items():
            self._print_trie(child, prefix + char)
