# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
from collections import deque, namedtuple

# 1. mark all nodes unvisited
# 2. set initial node distance to zero, other nodes to infinite
# 3. select unvisited node with smallest distance
# 4. find unvisited neighbors (to selected node), compare distances, and save smallest one
# 5. mark current node visited
# 6. stop if destination is visited, otherwise repeat step 3-6

inf = float('inf')
edge = namedtuple('Edge', 'start, end, cost')

# make_edge
def make_edge(start, end, cost=1): return edge(start, end, cost)

class Graph:
    def __init__(self, edges):
        check_edges = [i for i in edges if len(i) not in [2, 3]]
        if check_edges:
            raise ValueError('Error: check_edges, {}'.format(check_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    # vertices
    @property
    def vertices(self):
        return set(
            # turn ([1,2], [3,4]) into [1, 2, 3, 4]
            sum(([edge.start, edge.end] for edge in self.edges), [])
        )

    # get_node_pairs
    def get_node_pairs(self, node_1, node_2, both_ends=True):
        if both_ends:
            node_pairs = [[node_1, node_2], [node_2, node_1]]
        else:
            node_pairs = [[node_1, node_2]]

        return node_pairs

    # remove_edge
    def remove_edge(self, node_1, node_2, both_ends=True):
        node_pairs = self.get_node_pairs(node_1, node_2, both_ends)
        edges = self.edges[:]

        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    # add_edge
    def add_edge(self, node_1, node_2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(node_1, node_2, both_ends)
        
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Error: add_edge, {} {}'.format(node_1, node_2))

        self.edges.append(edge(start=node_1, end=node_2, cost=cost))
        if both_ends:
            self.edges.append(edge(start=node_2, end=node_1, cost=cost))

    # neighbors
    @property
    def neighbors(self):
        neighbors = { vertex: set() for vertex in self.vertices }

        for edge in self.edges:
            neighbors[edge.start].add((edge.end, edge.cost))

        return neighbors

    # dijkstra
    def dijkstra(self, source, destination):
        assert source in self.vertices, 'assert: source do not exist'

        # 1. mark all nodes unvisited
        # 2. set initial node distance to zero, other nodes to infinite
        distances = { vertex: inf for vertex in self.vertices }
        previous_vertices = { vertex: None for vertex in self.vertices }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            # 3. select unvisited node with smallest distance
            current_vertex = min(vertices, key = lambda vertex: distances[vertex])

            # 6. stop if destination is visited, otherwise repeat step 3-6
            if distances[current_vertex] == inf:
                break

            # 4. find unvisited neighbors (to selected node), compare distances, and save smallest one
            for neighbor, cost in self.neighbors[current_vertex]:
                alternative_route = distances[current_vertex] + cost

                if (alternative_route < distances[neighbor]):
                    distances[neighbor] = alternative_route
                    previous_vertices[neighbor] = current_vertex

            # 5. mark current node visited
            vertices.remove(current_vertex)

        path, current_vertex = deque(), destination

        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]

        if path:
            path.appendleft(current_vertex)

        return path

# create example graph
graph = Graph([
    ('a', 'b', 7),
    ('a', 'c', 9),
    ('a', 'f', 14),
    ('b', 'c', 10),
    ('b', 'd', 15),
    ('c', 'd', 11),
    ('c', 'f', 2),
    ('d', 'e', 6),
    ('e', 'f', 9)
])

print(graph.dijkstra('a', 'f'))
# deque(['a', 'c', 'f'])
