"""
Project 2 - Connected components and graph resilience
"""
__author__ = 'mdmytiaha'

import poc_queue
# import test


def bfs_visited(ugraph, start_node):
    """
    Takes the undirected graph ugraph and the node start_node and
    returns the set consisting of all nodes that are visited
    by a breadth-first search that starts at start_node
    """
    queue = poc_queue.Queue()
    visited = set([start_node])
    queue.enqueue(start_node)

    while not is_empty(queue):
        vertex = queue.dequeue()
        for neighbor in ugraph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
    return visited

def is_empty(queue):
    """
    check whether queue empty or not
    """
    return len(queue) == 0

def cc_visited(ugraph):
    """

    :param ugraph: undirected graph
    :return: a list of sets, where each set consists of all the nodes (and nothing else) in a connected component
    """
    cc_result = list()
    for vertex in ugraph.keys():
        visited = bfs_visited(ugraph, vertex)
        if visited not in cc_result:
            cc_result.append(visited)
    return cc_result

def largest_cc_size(ugraph):
    """
    :param ugraph: undirected graph
    :return:  the size (an integer) of the largest connected component in ugraph
    """
    largest = [len(some_list) for some_list in cc_visited(ugraph)]
    if is_empty(largest):
        return 0
    return max(largest)

def compute_resilience(ugraph, attack_order):
    """
    :param ugraph: undirected graph
    :param attack_order: list of nodes
    :return:
    """
    resilience = list()
    resilience.append(largest_cc_size(ugraph))
    for attack_vertex in attack_order:
        ugraph.pop(attack_vertex)
        for edges in ugraph.values():
            if attack_vertex in edges:
                edges.remove(attack_vertex)
        resilience.append(largest_cc_size(ugraph))
    return resilience

# print(compute_resilience(test.GRAPH2, [1, 3, 5, 7, 2, 4, 6, 8]))