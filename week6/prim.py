import heapq
import random
from typing import Set

from week6.graph import Graph, Edge, Node


def prim(graph: Graph) -> Set[Edge]:
    if not graph:
        return set()

    # 随意挑选的开始节点
    start: Node = random.choice(list(graph.nodes.values()))
    # 从大到小排好的面，应为要增加和删除，所以使用 heap
    edges = start.edges
    heapq.heapify(edges)
    # 已经走过的节点
    visited = {start}
    # 结果
    res = set()

    while edges:
        edge = heapq.heappop(edges)
        to_node = edge.to
        if to_node not in visited:
            visited.add(to_node)
            res.add(edge)
            for e in to_node.edges:
                heapq.heappush(edges, e)
    return res

