"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id]= set()
        

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("vertex does not Exist")
        

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #create an empty queue and enqueue starting vertex
        #?Queue = []
        q = Queue()
        q.enqueue(starting_vertex)

        # create a set to store the visited verticies
        visited = set()

        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()


            # if vertex has not been visited
            if v not in visited:
                # mark vertex as visited
                # print it for debug
                print(v)

                visited.add(v)
                
                # add all of it's neighbors to the back of the queue
                for next_vertex in self.get_neighbors(v):
                    q.enqueue(next_vertex)
        pass  # TODO

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #create an empty queue and enqueue starting vertex
        #?Queue = []
        s = Stack()
        s.push(starting_vertex)

        # create a set to store the visited verticies
        visited = set()

        # while the queue is not empty
        while s.size() > 0:
            # dequeue the first vertex
            v = s.pop()

            # if vertex has not been visited
            if v not in visited:
                # mark vertex as visited
                visited.add(v)
                # print it for debug
                print(v)

                # add all of it's neighbors to the top of the stack
                for next_vertex in self.get_neighbors(v):
                    s.push(next_vertex)
        pass  # TODO

    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited.add(starting_vertex)
        print(starting_vertex)

        for v in self.get_neighbors(starting_vertex):
            if v in visited:
                return
            else:
                self.dft_recursive(v, visited)
        pass  # TODO

    def bfs(self, starting_vertex, target_vertex_id):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #create an empty queue and enqueue PATH to starting vertex id
        q = Queue()
        q.enqueue([starting_vertex])
        #create a set to store visited verticeies
        visited = set()
        #while queue is not empty:
        while q.size() > 0:
            # dequeue the first PATH
            path = q.dequeue()
            #grab the last vertex from the PATH
            v = path[-1]

            #check if the vertex has not been visited
            if v not in visited:
                #is this vertex the target?
                if v == target_vertex_id:
                    #return the path
                    return path
                #mark as visited
                visited.add(v)

                #then add A PATH to it's neighbors to the back of the queue
                for next_v in self.get_neighbors(v):
                #make a copy of the path
                    path_copy = list(path)
                #append the neighbor to the back of the path
                    path_copy.append(next_v)
                #enqueue out new path
                    q.enqueue(path_copy)

        #return None
        return None

        pass  # TODO

    def dfs(self, starting_vertex, target_vertex_id):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        #create an empty stack and push PATH to starting vertex id
        s= Stack()
        s.push([starting_vertex])
        #create a set to store visited verticeies
        visited = set()
        #while stack is not empty:
        while s.size() > 0:
            # pop the first PATH
            path = s.pop()
            #grab the last vertex from the PATH
            v = path[-1]

            #check if the vertex has not been visited
            if v not in visited:
                #is this vertex the target?
                if v == target_vertex_id:
                    #return the path
                    return path
                #mark as visited
                visited.add(v)

                #then add A PATH to it's neighbors to the back of the queue
                for next_v in self.get_neighbors(v):
                #make a copy of the path
                    path_copy = list(path)
                #append the neighbor to the back of the path
                    path_copy.append(next_v)
                #enqueue out new path
                    s.push(path_copy)

        #return None
        return None
        pass  # TODO

    def dfs_recursive(self, starting_vertex, target_vertex_id, visited= set(), path = []):#destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        temp_path = path.copy()
        temp_path.append(starting_vertex)

        if starting_vertex not in visited:
            # print(starting_vertex)
            visited.add(starting_vertex)

            if starting_vertex == target_vertex_id:
                return temp_path
            else:
                for neighbor in self.get_neighbors(starting_vertex):
                    next_path = self.dfs_recursive(neighbor, target_vertex_id, visited, temp_path)
                    if next_path is not None:
                        return next_path
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
