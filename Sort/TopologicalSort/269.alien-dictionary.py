from collections import deque, defaultdict


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]
        char_set = set("".join(words))
        graph = defaultdict(set)
        indegree = defaultdict(int)
        # Build the graph
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                w1 = words[i]
                w2 = words[j]
                pos = 0
                while pos < len(w1) and pos < len(w2):
                    if w1[pos] != w2[pos]:
                        if w2[pos] not in graph[w1[pos]]:
                            graph[w1[pos]].add(w2[pos])
                            indegree[w2[pos]] += 1
                        break
                    pos += 1
                else:
                    if len(w1) > len(w2):
                        return ""
        res = ""

        # Start topological sort
        q = deque([node for node in char_set if indegree[node] == 0])
        while q:
            node = q.popleft()
            res += node
            for next_node in graph[node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    q.append(next_node)
        for node in indegree.keys():
            if indegree[node] != 0:
                return ""
        return res
