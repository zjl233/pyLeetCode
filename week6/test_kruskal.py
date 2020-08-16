from unittest import TestCase

from week6.generate_graph import graph_from_weight_edges
from week6.kruskal import kruskal


class Test(TestCase):
    def test_kruskal(self):
        edge_list = [
            ('a', 'b', 7,),
            ('a', 'c', 10),
            ('b', 'c', 3,),
            ('b', 'd', 9,),
            ('a', 'd', 9,),
            ('c', 'd', 6,),
            ('c', 'e', 1,),
            ('d', 'e', 3,),

            # ('b', 'a', 7,),
            # ('c', 'a', 10),
            # ('c', 'b', 3,),
            # ('d', 'b', 9,),
            # ('d', 'a', 9,),
            # ('d', 'c', 6,),
            # ('e', 'c', 1,),
            # ('e', 'd', 3,),

        ]
        graph = graph_from_weight_edges(edge_list, True)
        res = kruskal(graph)
        print(res)
