import sys
import os
import numpy as np
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from Stack_queue import queue
class vertex:
    def __init__(self, data):
        self.data = data


class Graph:

    def __init__(self , directed: bool, weighted:bool):
        self.adj_matrix = []
        self.vertecies = {}
        self.size = 0
        self.directed = directed
        self.weighted = weighted
    
    def change_size(self):
        if len(self.adj_matrix) ==0:
            self.adj_matrix = [[0]*self.size for _ in range(self.size)]
        else:
            for row in self.adj_matrix:
                row.append(0)
            self.adj_matrix.append([0]*self.size)

    def serch_data(self, v1 , v2 = None):
        # initialize the indexes with -1
        v1_idx = -1
        v2_idx = -1
        if v1 in self.vertecies:
            v1_idx = self.vertecies[v1][0]
        if v2 in self.vertecies:
            v2_idx = self.vertecies[v2][0]
        return v1_idx ,v2_idx
    
    def add_verex(self , data):
        idx ,_ = self.serch_data(data)
        if idx == -1:
            node = vertex(data)
            self.vertecies[data] = [self.size , node]
            self.size +=1
            self.change_size()
        else:
            pass

    
    def add_edge(self, v1_data , v2_data , weight = None):
        v1_idx , v2_idx =self.serch_data(v1_data , v2_data)
        if v1_idx == -1 or v2_idx == -1:
            print("some vertex not exist")
        else:
            if self.weighted:
                if weight:
                    self.adj_matrix[v1_idx][v2_idx] = weight
                    if not self.directed:
                        self.adj_matrix[v2_idx][v1_idx] = weight
                else:
                    print("please provide weight")
            else:
                self.adj_matrix[v1_idx][v2_idx] = 1
                if not self.directed:
                        self.adj_matrix[v2_idx][v1_idx] = 1

    def print_connection(self):
        vertecies = list(self.vertecies.keys())
        if self.weighted:
            for i in range(len(vertecies)):
                print(f"vertex {vertecies[i]} is connected to ", end='-->')
                for j in range(len(vertecies)):
                    if self.adj_matrix[i][j] > 0:
                        print(f"{vertecies[j]} with weight {self.adj_matrix[i][j]}", end=', ')
                print()
        else:
            for i in range(len(vertecies)):
                print(f"vertex {vertecies[i]} is connected to ", end='-->')
                for j in range(len(vertecies)):
                    if self.adj_matrix[i][j] > 0:
                        print(f"{vertecies[j]} ", end=', ')
                print()

    def DFS(self, index ,visited =[]):
        vertecies = list(self.vertecies.keys())
        print(vertecies [index])
        visited.append(vertecies[index])
        for i,neighbour in enumerate(self.adj_matrix[index]):
            if neighbour > 0 and vertecies[i] not in visited:
                self.DFS(i , visited)
    
    def BFS(self ,index):
        bfs_queue = queue.Queue()
        vertecies = list(self.vertecies.keys())
        visited = [vertecies[index]]
        bfs_queue.enqueue(vertecies[index])
        while not bfs_queue.is_empty():
            vertex = bfs_queue.dequeue()
            print(vertex)
            for i ,neighbour in enumerate(self.adj_matrix[self.vertecies[vertex][0]]):
                if neighbour>0 and vertecies[i] not in visited:
                    bfs_queue.enqueue(vertecies[i])
                    visited.append(vertecies[i])

    def cycle_detection_DFS(self, index, parent = None, visited=[] , cycles = []):
        vertecies = list(self.vertecies.keys())
        visited.append(vertecies[index])
        cycles.append(vertecies[index])
        for i , neighbour in enumerate(self.adj_matrix[index]):
            if neighbour>0:
                if vertecies[i]!= parent:
                    if vertecies[i] in visited:
                        if vertecies[i] in cycles:
                            cycle = ''.join(cycles[cycles.index(vertecies[i]):])
                            print(f"ther's a cycle: {cycle}")
                    else:
                        self.cycle_detection_DFS(i ,vertecies[index] ,visited, cycles)
                        cycles = cycles[:cycles.index(vertecies[index])+1]
        return
    
    # implement cycle detection with union find
    def find(self , v_idx , subsets):
        # the parent root has index equal to its value
        if subsets[v_idx] == v_idx:
            return v_idx
        return self.find(subsets[v_idx],subsets)
    
    
    def cycle_detection_UF(self):
        # define the roots of each vertex in the graph
        parents = [i for i in range(self.size)]
        
        # loop over the edges of the graph
        for i in range(self.size):
            for j in range(i , self.size):
                if self.adj_matrix[i][j]>0:
                    # get the roots of both verticies
                    v1_root= self.find(i,parents)
                    v2_root= self.find(j,parents)
                    # if the two roots are the same then cycle detected
                    if v1_root == v2_root:
                        print("cycle detected")
                        return
                    else:
                        # merge the two subset by change the root of the second subset to be the same as the first one
                        parents[v2_root] = v1_root

        

graph = Graph(False, False)
graph.add_verex('A')
graph.add_verex('B')
graph.add_verex('C')
graph.add_verex('D')
graph.add_verex('E')
graph.add_verex('F')
graph.add_edge('E','A')
graph.add_edge('D','A')
graph.add_edge('A','C')
graph.add_edge('C','B')
graph.add_edge('B','F')
graph.add_verex('G')
graph.add_edge('C','G')
graph.add_edge('C','E')
graph.add_edge('C','F')
graph.add_edge('D','E')
graph.cycle_detection_DFS(3)
graph.cycle_detection_UF()
#print(graph.adj_matrix)
