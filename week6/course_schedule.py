from typing import List

from week6.generate_graph import graph_from_edges
from week6.graph import Node
from week6.topological_sort import topological_sort_detect_cycle


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = graph_from_edges(prerequisites)
        has_cycle = topological_sort_detect_cycle(graph)
        return not has_cycle


