#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#


# @lc code=startF
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()
        for word in words:
            self.add_word(word)

        M, N = len(board), len(board[0])
        visited = [[0] * N for _ in range(M)]
        res = set()

        for i in range(M):
            for j in range(N):
                self.dfs(board, i, j, "", self.root, visited, res)

        return list(res)

    def add_word(self, word):
        cur_node = self.root
        for ch in word:
            if ch not in cur_node.children:
                cur_node.children[ch] = TrieNode()
            cur_node = cur_node.children[ch]
        cur_node.is_end = True

    # 遍历的过程跟trie同时遍历，作比较。
    def dfs(self, board, i, j, path, node, visited, res):
        M, N = len(board), len(board[0])
        ch = board[i][j]
        if ch not in node.children:
            return

        visited[i][j] = 1

        node = node.children[ch]
        if node.is_end:
            res.add(path + ch)

        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = i + d[0], j + d[1]

            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0:
                self.dfs(board, nx, ny, path + ch, node, visited, res)

        visited[i][j] = 0


# @lc code=end
