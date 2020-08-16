# 必须是无向图

# 将所有的边放入 sorted array 里，以权重从小到大的顺序依次弹出
# 如果两头的边不在同一个集合里，就 union
from typing import Set

from utils.misc import UnionFind
from week6.graph import Graph, Edge


def kruskal(graph: Graph) -> Set[Edge]:
    uf = UnionFind([node for node in graph.nodes.values()])
    res: Set[Edge] = set()

    edges = list(graph.edges)
    edges.sort(key=lambda e: e.weight)
    for e in edges:
        if not uf.is_same_set(e.from_, e.to):
            res.add(e)
            uf.union(e.from_, e.to)
    return res
