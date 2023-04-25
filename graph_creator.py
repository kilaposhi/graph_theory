import networkx as nx
import numpy as np
import random


def create_random_graph(num_vertices, num_edges):
    graph = nx.DiGraph()
    vertices = np.arange(num_vertices)
    graph.add_nodes_from(vertices)
    for i in range(num_edges):
        vertex1 = random.randint(0, num_vertices - 1)
        vertex2 = random.randint(0, num_vertices - 1)
        graph.add_edge(vertex1, vertex2)
    return graph
