from typing import List

from week6.generate_graph import graph_from_edges
from week6.graph import Node
from week6.topological_sort import topological_sort


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = graph_from_edges(prerequisites)
        # 添加孤立的节点
        for i in range(numCourses):
            if i not in graph.nodes:
                graph.nodes[i] = Node(i)
        order = topological_sort(graph)
        return [node.val for node in order]
