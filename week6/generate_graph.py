from typing import List, Tuple

from week6.graph import Graph, Node, Edge


# 图的常见表示方式
# https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs
# Edge lists
# Adjacency matrices
# Adjacency lists

# edge = [to, from]
# 都是有向图
def graph_from_edges(edges: List[Tuple[int, int]], undirected: bool = False) -> Graph:
    """
    edge 的顺序是 from to
    """
    # 无向图是有向图 * 2
    if undirected:
        reverse_edges = [(to, from_) for from_, to in edges]
        edges.extend(reverse_edges)

    graph = Graph()
    for from_, to in edges:
        if from_ not in graph.nodes:
            graph.nodes[from_] = Node(from_)
        if to not in graph.nodes:
            graph.nodes[to] = Node(to)
        from_node, to_node = graph.nodes[from_], graph.nodes[to]

        new_edge = Edge(from_node, to_node)
        graph.edges.add(new_edge)

        from_node.edges.append(new_edge)
        to_node.edges.append(new_edge)

        from_node.nexts.append(to_node)
        from_node.out += 1
        to_node.in_ += 1

    return graph


# 都是有向图
def graph_from_weight_edges(edges: List[Tuple[int, int, int]], undirected: bool = False) -> Graph:
    """
    :param undirected: 是不是有向图
    :type edges: List[Tuple[int, int, int]] 是带权重的边, (from. to, weight)
    """
    # 无向图是有向图 * 2
    if undirected:
        reverse_edges = [(to, from_, weight) for from_, to, weight in edges]
        edges.extend(reverse_edges)

    graph = Graph()
    for from_, to, weight in edges:
        if from_ not in graph.nodes:
            graph.nodes[from_] = Node(from_)
        if to not in graph.nodes:
            graph.nodes[to] = Node(to)
        from_node, to_node = graph.nodes[from_], graph.nodes[to]

        new_edge = Edge(from_node, to_node, weight)
        graph.edges.add(new_edge)

        from_node.edges.append(new_edge)
        to_node.edges.append(new_edge)

        from_node.nexts.append(to_node)
        from_node.out += 1
        to_node.in_ += 1

    return graph
