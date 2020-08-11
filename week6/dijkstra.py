from typing import Set, Dict

# 无路径为负的环
from week6.graph import Node


# 返回从 start 节点，到图中所有节点的距离表
# 自己到自己的距离为1
def closest_node(table: Dict[Node, int], visited: Set[Node]) -> Node:
    # node 按照 距离排序
    nodes = sorted(table, key=table.get)
    # 第一个没有 visited 过的 node
    for n in nodes:
        if n not in visited:
            return n


def dijkstra(start: Node) -> Dict[Node, int]:
    table = {start: 0}
    visited: Set[Node] = set()
    closest = closest_node(table, visited)
    while closest:
        distance = table[closest]
        for e in closest.edges:
            to_node = e.to
            # 第一次加入 table，以前的距离为 inf
            if to_node not in table:
                table[to_node] = distance + e.weight
            else:
                table[to_node] = min(
                    table[to_node],
                    distance + e.weight
                )
        visited.add(closest)
        closest = closest_node(table, visited)

    return table
