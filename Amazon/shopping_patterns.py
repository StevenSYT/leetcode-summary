from collections import defaultdict


class Graph:
    def __init__(self, num_nodes, num_edges):
        self.nodes = list(range(1, num_nodes))
        self.num_edges = num_edges
        self.edges = defaultdict(set)
        self.degrees = defaultdict(int)

    def add_edge(self, n1, n2):
        self.edges[n1].add(n2)
        self.edges[n2].add(n1)
        self.degrees[n1] += 1
        self.degrees[n2] += 1

    def get_degree(self, n):
        return self.degrees[n]

    def edge_exist(self, n1, n2):
        return n2 in self.edges[n1]


class Solution:
    def get_min_score(self, products_nodes, products_edges, products_from,
                      products_to):
        g = Graph(products_nodes, products_edges)

        for i in range(len(products_from)):
            g.add_edge(products_from[i], products_to[i])

        min_score = float('inf')
        visited_trios = set()
        for start_node, end_nodes in g.edges.items():
            for end_node in end_nodes:
                # For each edge, find a third node check if trio
                for node in g.nodes:
                    if node == end_node or node == start_node or tuple(
                            sorted([start_node, end_node, node
                                    ])) in visited_trios:
                        continue
                    if g.edge_exist(start_node, node) and g.edge_exist(
                            end_node, node):
                        # Got a trio
                        min_score = min(
                            g.get_degree(start_node) + g.get_degree(end_node) +
                            g.get_degree(node) - 6, min_score)
                        visited_trios.add(
                            tuple(sorted([start_node, end_node, node])))
        return min_score if min_score != float('inf') else -1


s = Solution()
products_nodes = [6]
products_edges = [6]
products_from = [[1, 2, 2, 3, 4, 5]]
products_to = [[2, 4, 5, 5, 5, 6]]
outputs = [3]

pass_count = 0
for i in range(len(products_nodes)):
    res = s.get_min_score(products_nodes[i], products_edges[i],
                          products_from[i], products_to[i])
    if (res == outputs[i]):
        print("Test case {} passed.".format(i))
        pass_count += 1
    else:
        print("Test case {} failed.".format(i))

if pass_count == len(products_nodes):
    print("Accepted, {}/{} passed".format(pass_count, len(products_nodes)))
else:
    print("Wrong answer, {}/{} passed".format(pass_count, len(products_nodes)))
