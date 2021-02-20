class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        self.dfs("", 0, word, 0, res)
        return res

    def dfs(self, path, pos, word, count, res):
        if pos == len(word):
            if count > 0:
                path += str(count)
            res.append(path)
            return

        self.dfs(path, pos + 1, word, count + 1, res)

        self.dfs(path + (str(count) if count > 0 else "") + word[pos], pos + 1,
                 word, 0, res)
