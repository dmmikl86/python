"""
Project 1 - Degree distributions for graphs
"""
EX_GRAPH0 = {
    0: set([1, 2]),
    1: set([]),
    2: set([])
}

EX_GRAPH1 = {
    0: set([4, 5, 1]),
    1: set([6, 2]),
    2: set([3]),
    3: set([0]),
    4: set([1]),
    5: set([2]),
    6: set([])
}

EX_GRAPH2 = {
    0: set([4, 5, 1]),
    1: set([6, 2]),
    2: set([7, 3]),
    3: set([7]),
    4: set([1]),
    5: set([2]),
    6: set([]),
    7: set([3]),
    8: set([1, 2]),
    9: set([0, 4, 5, 6, 7, 3])
}

def make_complete_graph(num_nodes):
    """
    :param num_nodes: the number of nodes
    :return: a dictionary corresponding to a complete directed graph with the specified number of nodes
    """
    res = {}

    if num_nodes == 1:
        return {0: set([])}
    else:
        for node in range(num_nodes):
            set_of_edges = set()
            for index in range(num_nodes):
                if index != node:
                    set_of_edges.add(index)
            res[node] = set_of_edges
        return res

def compute_in_degrees(digraph):
    """
    :param digraph: a directed graph (represented as a dictionary)
    :return: a dictionary with the same set of keys (nodes)
    """
    res = {}
    for node in digraph.keys():
        res[node] = 0

    for node in digraph.keys():
        for value in digraph[node]:
            res[value] = (res[value] + 1)
    return res

def in_degree_distribution(digraph):
    """
    :param digraph: directed graph (represented as a dictionary)
    :return: computes the unnormalized distribution of the in-degrees of the graph
    """
    in_degrees = compute_in_degrees(digraph)
    set_in_degrees = list(set(in_degrees.values()))
    res = {}
    for index in set_in_degrees:
        res[index] = len(filter(lambda x: x == index, in_degrees.values()))

    return res
