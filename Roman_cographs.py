from Cograph_modular_decomposition import *


def is_universal_vertex(graph, vertex):
    """
    Checks if a vertex is universal in the given graph.
    
    :param graph: Dictionary representing the graph where keys are vertices and values are lists of neighboring vertices.
    :param vertex: Vertex to check for universality.
    :return: True if the vertex is universal, False otherwise.
    """
    # Check if the vertex has edges to all other vertices except itself
    return set(graph[vertex]) == {v for v in graph if v!= vertex}

def is_almost_universal_vertex(graph, vertex, excluded_vertex):
    """
    Checks if a vertex is almost universal in the given graph, excluding one specific vertex.
    
    :param graph: Dictionary representing the graph where keys are vertices and values are lists of neighboring vertices.
    :param vertex: Vertex to check for being almost universal.
    :param excluded_vertex: Vertex to exclude when checking for universality.
    :return: True if the vertex is almost universal, False otherwise.
    """
    # Check if the vertex has edges to all other vertices except the excluded vertex and itself
    return set(graph[vertex]).difference({excluded_vertex}) == {v for v in graph if v!= vertex and v!= excluded_vertex}

def roman_cograph(Gl, Gr):
    """
    Calculates the Roman domination number (γR) of a graph represented by two dictionaries.
    
    :param Gl: Dictionary representing the original graph where keys are vertices and values are lists of neighboring vertices.
    :param Gr: Dictionary representing the complement graph where keys are vertices and values are lists of neighboring vertices.
    :return: The Roman domination number of the graph.
    """
    # Check for universal vertex in both graphs (original and its complement)
    if any(is_universal_vertex(Gl, vertex) for vertex in Gl) or any(is_universal_vertex(Gr, vertex) for vertex in Gr):
        return 2
    
    # Check for almost universal vertex in both graphs (original and its complement)
    elif any(is_almost_universal_vertex(Gl, vertex, excluded_vertex) for vertex in Gl for excluded_vertex in Gl[vertex]) or \
         any(is_almost_universal_vertex(Gr, vertex, excluded_vertex) for vertex in Gr for excluded_vertex in Gr[vertex]):
        return 3
    
    # Default case if neither condition is met
    return 4