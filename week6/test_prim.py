from typing import List
from unittest import TestCase

from week6.generate_graph import graph_from_weight_edges
from week6.prim import prim


class Test(TestCase):
    def test_prim(self):
        edges = [
            ('A', 'D', 1),
            ('A', 'B', 7),
            ('A', 'E', 2),
            ('D', 'B', 8),
            ('B', 'E', 3),
            ('D', 'C', 1),
            ('C', 'E', 10),
        ]
        graph = graph_from_weight_edges(edges, True)
        res = prim(graph)
        print(res)