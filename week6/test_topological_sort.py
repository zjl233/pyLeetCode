from typing import List
from unittest import TestCase

from utils.treenode import TreeNode
from week6.generate_graph import graph_from_edges, graph_from_weight_edges
from week6.topological_sort import topological_sort


class Test(TestCase):
    def test_topological_sort(self):
        edges1 = [
            ('B', 'A', 0),
            ('B', 'C', 0),
            ('A', 'C', 0),
            ('B', 'E', 0),

            ('C', 'E', 0),
        ]
        graph = graph_from_weight_edges(edges1)
        res = topological_sort(graph)
        print(res)


        edges2 = [
            ('D', 'A', 0),
            ('A', 'B', 0),
            ('B', 'C', 0),
            ('C', 'A', 0),
        ]
        graph = graph_from_weight_edges(edges2)
        res = topological_sort(graph)
        print(res)

