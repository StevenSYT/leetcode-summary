from collections import defaultdict, deque
class Solution:
    def sequenceReconstruction(self, org: List[int],
                               seqs: List[List[int]]) -> bool:
        n = len(org)
        graph = defaultdict(list)
        indegree = [None] * (n + 1)
        for seq in seqs:
            for item in seq:
                if item > n or item < 1:
                    return False
                if indegree[item] == None:
                    indegree[item] = 0
            for i in range(1, len(seq)):
                if seq[i - 1] > n or seq[i] > n:
                    return False
                graph[seq[i - 1]].append(seq[i])
                indegree[seq[i]] += 1
        q = deque([node for node in range(1, n + 1) if indegree[node] == 0])
        res = []
        while q:
            if len(q) > 1:
                return False
            node = q.popleft()
            res.append(node)
            for next_node in graph[node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    q.append(next_node)
        return res == org