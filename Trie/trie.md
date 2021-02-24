# Trie

- [Implement Trie (Prefix Tree)](<#implement-trie-(prefix-tree)>)
- [Design Add and Search Words Data Structure](#design-add-and-search-words-data-structure)

## Implement Trie (Prefix Tree)

[208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()



    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_node = self.root
        for ch in word:
            if ch not in cur_node.children:
                cur_node.children[ch] = TrieNode()

            cur_node = cur_node.children[ch]
        cur_node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_node = self.root
        for ch in word:
            if ch not in cur_node.children:
                return False

            cur_node = cur_node.children[ch]

        return cur_node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self.root
        for ch in prefix:
            if ch not in cur_node.children:
                return False

            cur_node = cur_node.children[ch]

        return True
```

## Design Add and Search Words Data Structure

[211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

```python
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for ch in word:
            cur_node = cur_node.children[ch]

        cur_node.is_end = True

    def search(self, word: str) -> bool:
        return self.match(word, self.root)

    def match(self, word, node):
        if not word:
            return node.is_end

        ch = word[0]
        if ch not in node.children:
            if ch == '.':
                return any([self.match(word[1:], node.children[key]) for key in node.children])

            else:
                return False
        else:
            return self.match(word[1:], node.children[word[0]])
```
