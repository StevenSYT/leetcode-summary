#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
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
                return any([
                    self.match(word[1:], node.children[key])
                    for key in node.children
                ])

            else:
                return False
        else:
            return self.match(word[1:], node.children[word[0]])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
