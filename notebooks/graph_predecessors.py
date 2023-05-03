import networkx as nx


def vertices_number_of_predecessors(graph: nx.DiGraph) -> dict[int, int]:
    """
    Return dict associating vertices and their number of predecessors from a graph
    :Example: {0: 2, vertex: num_predecessor,...}  vertex '0' has 2 predecessors
    """
    num_vertices = graph.number_of_nodes()
    return {vertex: len(list(graph.predecessors(vertex))) for vertex in range(num_vertices)}


def vertices_without_predecessors(graph: nx.DiGraph) -> list[int]:
    """
    return a list of graph's vertices that does not have predecessors
    :Example: [0,2] vertices '0' and '2' don't have predecessors in the graph
    """
    num_vertices = graph.number_of_nodes()
    num_predecessors = vertices_number_of_predecessors(graph)
    return [vertex for vertex in range(num_vertices) if num_predecessors[vertex] == 0]  # stack
