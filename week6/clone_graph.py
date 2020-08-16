# Definition for a Node.
from typing import Optional, List, Set, Dict


class Node:
    def __init__(self, val: int = 0, neighbors: List['Node'] = None):
        if neighbors is None:
            neighbors = []
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> Optional['Node']:
        if not Node:
            return None

        cpy = Node(node.val)
        cpys = {node: cpy}

        self.dfs(node, cpys)
        return cpy

    def dfs(self, node: 'Node', cpys: Dict[Node, Node]):
        for n in node.neighbors:
            if n not in cpys:  # 还没有走过
                cpy = Node(n.val)
                cpys[n] = cpy
                cpys[node].neighbors.append(cpy)
                self.dfs(n, cpys)
            else:  # 已经走过的, 刚从那里走过来
                cpys[node].neighbors.append(cpys[n])

