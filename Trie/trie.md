# Trie

- [Implement Trie (Prefix Tree)](<#implement-trie-(prefix-tree)>)
- [Design Add and Search Words Data Structure](#design-add-and-search-words-data-structure)
- [Prefix and Suffix Search](#prefix-and-suffix-search)

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

## Prefix and Suffix Search

[745. Prefix and Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/)

**Solution 1: Trie**

Use Two Trie structure to store the prefix and suffix, each node should also maintain the indices of the word when traversing the current node.

```python
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.indices = set()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word, i):
        cur_node = self.root

        for ch in word:
            cur_node = cur_node.children[ch]
            cur_node.indices.add(i)

    def search(self, word):
        cur_node = self.root

        for ch in word:
            if ch not in cur_node.children:
                return set()

            cur_node = cur_node.children[ch]

        return cur_node.indices

class WordFilter:

    def __init__(self, words: List[str]):
        self.pre_trie = Trie()
        self.suf_trie = Trie()

        word_set = set()
        for i in range(len(words) - 1, -1, -1):
            word = words[i]
            if word not in word_set:
                word_set.add(word)
                self.pre_trie.add_word(word, i)
                self.suf_trie.add_word(word[::-1], i)


    def f(self, prefix: str, suffix: str) -> int:
        pre_indices = self.pre_trie.search(prefix)
        suf_indices = self.suf_trie.search(suffix[::-1])
        res = pre_indices & suf_indices

        if not res:
            return -1

        return max(list(res))
```

**Solution 2: Dictionary**

We can just use 2 dicts to store the prefix, suffix information

```python
from collections import defaultdict


class WordFilter:
    def __init__(self, words: List[str]):
        self.pre_dict = defaultdict(set)
        self.suf_dict = defaultdict(set)

        seen = set()
        for i in range(len(words) - 1, -1, -1):
            word = words[i]
            if word not in seen:
                seen.add(word)
                for j in range(len(word)):
                    self.pre_dict[word[:j + 1]].add(i)
                    self.suf_dict[word[j:]].add(i)

    def f(self, prefix: str, suffix: str) -> int:
        pre_indices = self.pre_dict[prefix]
        suf_indices = self.suf_dict[suffix]

        res = pre_indices & suf_indices
        return max(list(res)) if res else -1
```
