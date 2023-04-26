import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms import bipartite
import numpy as np
import random


def create_random_vertices(num_vertices):
    """
    Create two vertices within the existing graph's nodes
    The vertices are not equal
    :param num_vertices: int
    :return: vertex1, vertex2
    """
    equals = True
    while equals:
        vertex1 = random.randint(0, num_vertices - 1)
        vertex2 = random.randint(0, num_vertices - 1)
        if vertex1 != vertex2:
            equals = False
    return vertex1, vertex2


def create_base_graph(num_vertices, num_edges):
    max_edges = ((num_vertices-1)*num_vertices)/2 # Max edges of a Directed Acyclic Graph (DAG)
    if num_edges > max_edges:
        raise Exception("Trying to create a graph with too many edges")
    graph = nx.DiGraph()
    vertices = np.arange(num_vertices)
    graph.add_nodes_from(vertices)
    return graph


def create_random_DiGraph(num_vertices, num_edges):
    graph = create_base_graph(num_vertices, num_edges)
    for i in range(num_edges):
        vertex1, vertex2 = create_random_vertices(num_vertices)
        graph.add_edge(vertex1, vertex2)
    return graph


def create_acyclic_DiGraph(num_vertices, num_edges):
    graph = create_base_graph(num_vertices, num_edges)
    for i in range(num_edges):
        not_acyclic = True
        while not_acyclic:
            vertex1, vertex2 = create_random_vertices(num_vertices)
            if vertex2 not in nx.ancestors(graph, vertex1):
                not_acyclic = False
        graph.add_edge(vertex1, vertex2)
    return graph


def draw_graph(graph : nx.DiGraph, title=None):
    options = {
        'node_color': 'red',
        'node_size': 200,
        'with_labels': True,
        'width': 3,
    }
    plt.title(title)
    return nx.draw_networkx(graph, pos=nx.spring_layout(graph, seed=100), **options)


def draw_grey_graph(graph:nx.DiGraph, title=None):
    options = {
        'node_color': 'grey',
        'node_size': 200,
        'with_labels': True,
        'alpha': 0.5,
        'width': 3,
        'edge_color': 'grey',
        'arrowsize': 20
    }
    plt.title(title)
    return nx.draw_networkx(graph, pos=nx.spring_layout(graph, seed=100), **options)

def draw_bipartite_graph(bipartite_graph : bipartite, title = None):
    options = {
        'node_color': 'red',
        'node_size': 200,
        'with_labels': True,
        'width': 3
    }
    plt.title(title)
    bottom_nodes, top_nodes = bipartite.sets(bipartite_graph)
    return nx.draw_networkx(bipartite_graph, pos=nx.bipartite_layout(bipartite_graph,top_nodes), **options)



def draw_matching_graph(bipartite_graph:bipartite, matching_list :dict, title:str= None):
    options = {
        'node_color': 'red',
        'node_size': 200,
        'with_labels': True,
        'width': 3,

    }
    plt.title(title)
    bottom_nodes, top_nodes = bipartite.sets(bipartite_graph)
    nx.draw_networkx(bipartite_graph, pos=nx.bipartite_layout(bipartite_graph,top_nodes), **options)
    return nx.draw_networkx(bipartite_graph, pos=nx.bipartite_layout(bipartite_graph,top_nodes), **options)


graph = create_acyclic_DiGraph(4, 6)
draw_graph(graph, title="test")
plt.show()
