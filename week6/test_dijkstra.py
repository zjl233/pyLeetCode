from unittest import TestCase

from week6.dijkstra import dijkstra
from week6.generate_graph import graph_from_weight_edges


class Test(TestCase):
    def test_dijkstra(self):
        edge_list = [
            ('a', 'b', 1),
            ('a', 'c', 7),
            ('a', 'd', 10),
            ('b', 'c', 2),
            ('c', 'd', 5),
            ('d', 'e', 3),
            ('c', 'e', 20),
            ('b', 'e', 50),
        ]
        graph = graph_from_weight_edges(edge_list)
        start = graph.nodes['a']
        res = dijkstra(start)
        print(res)
