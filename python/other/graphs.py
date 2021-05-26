class Graph(dict):
    def __init__(self, vertices=[], edges=[]):
        '''
            vertices    : list of vertices
            edges       : list of edges
        '''

        for vertex in vertices: self.add_vertex(vertex)
        for edge in edges: self.add_edge(edge)

    def add_vertex(self, vertex):
        '''Add vertex to graph.'''

        self[vertex] = {}

    def add_edge(self, edge):
        '''
            Add edge in both directions between vertex_1 and vertex_2, 
            replaces existing edge if any.
        '''

        vertex_1, vertex_2 = edge

        self[vertex_1][vertex_2] = edge
        self[vertex_2][vertex_1] = edge

    def get_edge(self, vertex_1, vertex_2):
        '''Return edge between vertex_1 and vertex_2, otherwise None.'''

        try:
            return self[vertex_1][vertex_2]
        except:
            return None

    def remove_edge(self, edge):
        '''Remove edge from graph.'''

        vertex_1, vertex_2 = edge

        del (self[vertex_1][vertex_2])
        del (self[vertex_2][vertex_1])

    def vertices(self):
        '''Return list of vertices in graph.'''
        
        lst = []
        for vertex in self.keys():
            lst.append(vertex)

        return lst

    def edges(self):
        '''Return list of edges in graph.'''

        lst = []
        for vertex in self.keys():
            for vertex, edge in self[vertex].items():
                if edge not in lst: lst.append(edge)

        return lst

    def out_vertices(self, vertex_1):
        '''Return list of connected vertices.'''

        lst = []
        for vertex in self[vertex_1]:
            lst.append(vertex)

        return lst

    def out_edges(self, vertex_1):
        '''Return list of connected edges.'''

        lst = []
        for vertex, edge in self[vertex_1].items():
            lst.append(edge)

        return lst

    def add_all_edges(self):
        '''Add edges between all vertices in graph (complete graph).'''

        for vertex_1 in self.keys():
            for vertex_2 in self.keys():
                if (vertex_1 != vertex_2):
                    self.add_edge(Edge(vertex_1, vertex_2))

# Vertex
class Vertex(object):
    def __init__(self, label=""):
        self.label = label

    def __repr__(self):
        return ("Vertex (%s)" % repr(self.label))

    __str__ = __repr__

# Edge
class Edge(tuple):
    def __new__(cls, edge_1, edge_2):
        return tuple.__new__(cls, (edge_1, edge_2))

    def __repr__(self):
        return ("Edge (%s, %s)" % (repr(self[0]), repr(self[1])))

    __str__ = __repr__

# vertices
A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')

# edges
A_B = Edge(A, B)
A_C = Edge(A, C)
C_D = Edge(C, D)

# graph
graph = Graph([A, B, C], [])
graph.add_all_edges()

print(graph)

# { 
#     Vertex ('A'): { 
#         Vertex ('B'): Edge (Vertex ('B'), Vertex ('A')), 
#         Vertex ('C'): Edge (Vertex ('C'), Vertex ('A'))
#     }, 
#     Vertex ('B'): {
#         Vertex ('A'): Edge (Vertex ('B'), Vertex ('A')), 
#         Vertex ('C'): Edge (Vertex ('C'), Vertex ('B'))
#     }, 
#     Vertex ('C'): {
#         Vertex ('A'): Edge (Vertex ('C'), Vertex ('A')), 
#         Vertex ('B'): Edge (Vertex ('C'), Vertex ('B'))
#     }
# }