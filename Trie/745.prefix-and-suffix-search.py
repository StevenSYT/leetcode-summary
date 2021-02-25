#
# @lc app=leetcode id=745 lang=python3
#
# [745] Prefix and Suffix Search
#

# @lc code=start
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


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
# @lc code=end
