class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")


def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])

    # Do a BFS storing the path
    # print(graph.vertices)
    q = Queue()
    q.enqueue([starting_node])
    max_path_length = 1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if (len(path) >= max_path_length and v < earliest_ancestor) or (len(path) > max_path_length):
            earliest_ancestor = v
            max_path_length = len(path)
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)

    return earliest_ancestor


# from collections import defaultdict

# class Stack():
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack.append(value)
#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None
#     def size(self):
#         return len(self.stack)

# def dfs(ancestors, starting_node):
#     #use dfs
#     s = Stack()
#     s.push([starting_node])

#     visited = set()

#     while s.size > 0:
#         path = s.pop()

#         v = path[-1]

#         if v not in visited:
#             visited.append(vertex)
                        
#         for decendants in starting_node[vertex]:
#             path_copy = path.copy()
#             path_copy.append(decendants)
#             stack.push(path_copy)

#     return visited [-1]

#     pass

# def earliest_ancestor(fam_tree, person):
#     fam = defaultdict(list)

#     for parent, child in fam_tree:
#         fam[child].append(parent)
    
#     if person not in fam:
#         return -1

#     earliest = earliest_ancestor(person, fam)

#     return earliset
