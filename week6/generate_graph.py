from typing import List, Tuple

from week6.graph import Graph, Node, Edge


# 图的常见表示方式
# https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs
# Edge lists
# Adjacency matrices
# Adjacency lists

# edge = [to, from]
def graph_from_edges(edges: List[List[int]]) -> Graph:
    """
    edge 的顺序是 to from
    """
    graph = Graph()
    for to, from_ in edges:
        if from_ not in graph.nodes:
            graph.nodes[from_] = Node(from_)
        if to not in graph.nodes:
            graph.nodes[to] = Node(to)
        from_node, to_node = graph.nodes[from_], graph.nodes[to]

        new_edge = Edge(from_node, to_node)
        from_node.edges.append(new_edge)
        to_node.edges.append(new_edge)

        from_node.nexts.append(to_node)
        from_node.out += 1
        to_node.in_ += 1

    return graph


def graph_from_weight_edges(edges: List[Tuple[int, int, int]]) -> Graph:
    """

    :type edges: List[Tuple[int, int, int]] 是带权重的边, (weight, from, to)
    """
    graph = Graph()
    for from_, to, weight in edges:
        if from_ not in graph.nodes:
            graph.nodes[from_] = Node(from_)
        if to not in graph.nodes:
            graph.nodes[to] = Node(to)
        from_node, to_node = graph.nodes[from_], graph.nodes[to]

        new_edge = Edge(from_node, to_node, weight)
        from_node.edges.append(new_edge)
        to_node.edges.append(new_edge)

        from_node.nexts.append(to_node)
        from_node.out += 1
        to_node.in_ += 1

    return graph
