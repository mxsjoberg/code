# https://en.wikipedia.org/wiki/Prim%27s_algorithm
import sys

class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)] 

    # function to print tree stored in parent
    def print_mst(self, parent): 
        print("Edge \tWeight")
        for i in range(1, self.V): 
            print(parent[i], "-", i, "\t", self.graph[i][ parent[i]])

    # function to find vertex with minimum distance value from set of 
    # vertices not included in shortest path tree 
    def min_key(self, key, mst_set): 
        # define min value 
        min = sys.maxsize 

        for v in range(self.V): 
            if key[v] < min and mst_set[v] == False: 
                min = key[v] 
                min_index = v 

        return min_index 

    # function to construct and print mst for graph represented using 
    # adjacency matrix 
    def prim_mst(self): 
        # key values used to select minimum weight edge
        key = [sys.maxsize] * self.V 
        
        # array to store constructed mst 
        parent = [None] * self.V
        
        # set key to 0 so it is first vertex 
        key[0] = 0
        mst_set = [False] * self.V 
        
        # first node is root
        parent[0] = -1

        # select minimum distance vertex from set of vertices not 
        # processed
        for cout in range(self.V):     
            # u is equal to source in first iteration 
            u = self.min_key(key, mst_set) 

            # add minimum distance vertex to shortest path tree 
            mst_set[u] = True

            # update distance value of adjacent vertices of selected vertex 
            # if current distance is greater than new distance and vertex not 
            # in shotest path tree 
            for v in range(self.V): 
                # update key if graph[u][v] is smaller than key[v] 
                if self.graph[u][v] > 0 and mst_set[v] == False and key[v] > self.graph[u][v]: 
                    key[v] = self.graph[u][v] 
                    parent[v] = u 

        self.print_mst(parent) 

# create graph
g = Graph(8) 
# g.graph = [[0, 2, 0, 6, 0], 
#            [2, 0, 3, 8, 5], 
#            [0, 3, 0, 0, 7], 
#            [6, 8, 0, 0, 9], 
#            [0, 5, 7, 9, 0]] 

#           A  B  C  D  E  F  G  H
g.graph = [[0, 1, 0, 0, 4, 8, 0, 0], # A
           [0, 0, 2, 0, 0, 6, 6, 0], # B
           [0, 0, 0, 1, 0, 0, 2, 0], # C
           [0, 0, 0, 0, 0, 0, 1, 4], # D
           [0, 0, 0, 0, 0, 5, 0, 0], # E
           [0, 0, 0, 0, 0, 0, 0, 0], # F
           [0, 0, 0, 0, 0, 1, 0, 1], # G
           [0, 0, 0, 0, 0, 0, 0, 0]] # H

g.prim_mst()

# Edge    Weight
# 0 - 1    2
# 1 - 2    3
# 0 - 3    6
# 1 - 4    5