class Solution:
    def expand(self, S: str) -> List[str]:
        char_map = collections.defaultdict(list)
        pos = 0
        i = 0
        in_options = False
        while i < len(S):
            ch = S[i]
            i += 1
            if ch == "{":
                in_options = True
            elif ch == "}":
                in_options = False
                pos += 1
            elif ch != ",":
                char_map[pos].append(ch)
                if not in_options:
                    pos += 1
        res = []
        self.dfs(0, char_map, '', res)
        return res

    def dfs(self, pos, char_map, path, res):
        if pos == len(char_map):
            res.append(path)
            return
        for ch in sorted(char_map[pos]):
            self.dfs(pos + 1, char_map, path + ch, res)