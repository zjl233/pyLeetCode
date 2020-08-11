from typing import List, Dict, Set


class Node:
    def __init__(self, val: int) -> None:
        # 节点的标记
        self.val = val
        self.in_ = 0
        self.out = 0
        self.nexts: List['Node'] = []
        self.edges: List[Edge] = []

    def __repr__(self) -> str:
        return f'GraphNode({self.val!r})'  # !r 为了区分 3 和 '3'


class Edge:
    def __init__(self, from_: Node, to: Node, weight: int = 0) -> None:
        self.weight = weight
        self.from_ = from_
        self.to = to

    def __repr__(self) -> str:
        return f'Edge({self.from_.val!r} -> {self.to.val!r} weight: {self.weight!r})'  # !r 为了区分 3 和 '3'

    def __lt__(self, other: 'Edge') -> bool:
        return self.weight < other.weight


class Graph:
    def __init__(self) -> None:
        # nodes 的 key 是节点的标记，可能是数字，如 1,2,3，也可能是字母，如A,B,C，
        # 和 node.val 是相同的
        self.nodes: Dict[int, Node] = dict()
        self.edges: Set[Edge] = set()
