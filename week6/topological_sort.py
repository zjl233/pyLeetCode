from collections import deque
from typing import List, Dict, Deque

from week6.graph import Node, Graph


# 输入的都是有向，无环图
def topological_sort(graph: Graph) -> List[Node]:
    if not graph:
        raise ValueError('graph must be not None')

    # 每个节点的剩余入度，不要修改原始节点
    rest_in: Dict[Node, int] = {}
    # 拓扑排序的开始，只有入度为零才能进入队列
    starts: Deque[Node] = deque()
    # 拓扑排序的结果
    order: List[Node] = []

    # 初始化 rest_in 和 starts
    for _, n in graph.nodes.items():
        rest_in[n] = n.in_
        if n.in_ == 0:
            starts.append(n)

    # 遍历 starts 里的节点

    while starts:
        start = starts.popleft()
        # 从图里拆除 n，将 n 相邻节点的入度 -1
        order.append(start)
        for n in start.nexts:
            rest_in[n] -= 1
            # 产生新的开始节点
            if rest_in[n] == 0:
                starts.append(n)

    # 结束时，所有节点的入度应该都等于0
    no_loop = all(in_ == 0 for in_ in rest_in.values())

    return order if no_loop else []


# 用拓扑排序判断是否有环
def topological_sort_detect_cycle(graph: Graph) -> bool:
    if not graph:
        raise ValueError('graph must be not None')

    # 每个节点的剩余入度，不要修改原始节点
    rest_in: Dict[Node, int] = {}
    # 拓扑排序的开始，只有入度为零才能进入队列
    starts: Deque[Node] = deque()
    # 拓扑排序的结果
    order: List[Node] = []

    # 初始化 rest_in 和 starts
    for _, n in graph.nodes.items():
        rest_in[n] = n.in_
        if n.in_ == 0:
            starts.append(n)

    # 遍历 starts 里的节点

    while starts:
        start = starts.popleft()
        # 从图里拆除 n，将 n 相邻节点的入度 -1
        order.append(start)
        for n in start.nexts:
            rest_in[n] -= 1
            # 产生新的开始节点
            if rest_in[n] == 0:
                starts.append(n)

    # 结束时，所有节点的入度应该都等于0
    has_loop = not all(in_ == 0 for in_ in rest_in.values())

    return has_loop
