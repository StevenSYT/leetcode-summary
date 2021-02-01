#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
from collections import deque
from string import ascii_lowercase

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        unvisited_words = set(wordList)
        q = deque([[beginWord]])

        if endWord not in beginWord:
            return []

        res = []
        while q:
            visited = set()
            size = len(q)
            for _ in range(size):
                path = q.popleft()
                word = path[-1]

                if path[-1] == endWord:
                    res.append(path)
                    continue

                for i in range(len(beginWord)):
                    for ch in ascii_lowercase:
                        next_word = word[:i] + ch + word[i + 1:]
                        if next_word in unvisited_words:
                            q.append(path + [next_word])
                            visited.add(next_word)
            unvisited_words -= visited
        return res




# @lc code=end

