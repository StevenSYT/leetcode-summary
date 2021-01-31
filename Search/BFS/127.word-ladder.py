#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import deque
from string import ascii_lowercase

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        unvisited_words = set(wordList)
        q = deque([(beginWord, 1)])

        if endWord not in unvisited_words:
            return 0

        while q:
            word, step = q.popleft()
            if word == endWord:
                return step

            for i in range(len(word)):
                for ch in ascii_lowercase:
                    next_word = word[:i] + ch + word[i+1:]

                    if next_word in unvisited_words:
                        q.append((next_word, step + 1))
                        unvisited_words.remove(next_word)
        return 0
        

        

# @lc code=end

