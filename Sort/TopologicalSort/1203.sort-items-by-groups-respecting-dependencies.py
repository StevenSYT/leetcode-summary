#
# @lc app=leetcode id=1203 lang=python3
#
# [1203] Sort Items by Groups Respecting Dependencies
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def sortItems(self, n: int, m: int, group: List[int],
                  beforeItems: List[List[int]]) -> List[int]:
        item_to_group = [None] * n
        group_to_items = defaultdict(list)
        new_group_id = m
        for item, g in enumerate(group):
            if g == -1:
                group_to_items[new_group_id].append(item)
                item_to_group[item] = new_group_id
                new_group_id += 1
            else:
                group_to_items[g].append(item)
                item_to_group[item] = g
        new_group_size = new_group_id
        item_graph = defaultdict(set)
        item_indegree = defaultdict(int)

        group_graph = defaultdict(set)
        group_indegree = defaultdict(int)

        for item in range(n):
            if beforeItems[item]:
                for before_item in beforeItems[item]:
                    cur_group, before_group = item_to_group[
                        item], item_to_group[before_item]
                    if cur_group == before_group:
                        item_graph[before_item].add(item)
                        item_indegree[item] += 1
                    else:
                        if cur_group not in group_graph[before_group]:
                            group_graph[before_group].add(cur_group)
                            group_indegree[cur_group] += 1
        for g in group_to_items.keys():
            try:
                group_to_items[g] = self.sortWithinGroup(
                    group_to_items[g], item_graph, item_indegree)
            except Exception:
                return []

        res = []
        q = deque([
            group for group in range(new_group_size)
            if group_indegree[group] == 0
        ])
        while q:
            group = q.popleft()
            res.extend(group_to_items[group])
            for next_group in group_graph[group]:
                group_indegree[next_group] -= 1
                if group_indegree[next_group] == 0:
                    q.append(next_group)
        for group in group_indegree.keys():
            if group_indegree[group] != 0:
                return []
        return res

    def sortWithinGroup(self, group_items, item_graph, item_indegree):
        q = deque([item for item in group_items if item_indegree[item] == 0])
        res = []
        while q:
            item = q.popleft()
            res.append(item)
            for next_item in item_graph[item]:
                item_indegree[next_item] -= 1
                if item_indegree[next_item] == 0:
                    q.append(next_item)
        for item in group_items:
            if item_indegree[item] != 0:
                raise Exception("indegree not zero")
        return res


# @lc code=end
