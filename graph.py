from default_dict import defaultdict

class Graph:
    def __init__(self, directed=True, weighted=False):
        self.__adjacency_list = {}
        self.__weighted_adj_list = defaultdict()
        self.__vertex_list = []
        self.__directed = directed
        self.__weighted = weighted 

    def add_vertex(self, vertex):
        if vertex not in self.__vertex_list:
            self.__vertex_list.append(vertex)
            self.__adjacency_list[vertex] = []
            self.__weighted_adj_list[vertex] = {}

    def add_edge(self, v1, v2, weight=0):
        if not self.__adjacency_list.get(v1):
            self.add_vertex(v1)
        if not self.__adjacency_list.get(v2):
            self.add_vertex(v2)
        if not self.__weighted:
            self.__adjacency_list[v1].append(v2)
            if not self.__directed:
                self.__adjacency_list[v2].append(v1)
        else:
            self.__adjacency_list[v1].append(v2)
            self.__weighted_adj_list[v1][v2] = weight
            if not self.__directed:
                self.__adjacency_list[v2].append(v1)
                self.__weighted_adj_list[v2][v1] = weight

    @property
    def weighted_adj_list(self):
        weighted_list = {k: v for k, v in self.__weighted_adj_list.items()}
        return weighted_list
        
    @property
    def vertecies_list(self):
        return self.__vertex_list

    @property
    def adjacency_list(self):
        return self.__adjacency_list
 
    def walk_path(self, start, end, path=[]):
        path += [start]
        if start == end:
            return path
        for v in self.__adjacency_list[start]:
            if v not in path:
                new_path = self.walk_path(v, end, path)
                if new_path:
                    return new_path
                return None
    @property
    def repr_list(self):
        for v in self.__adjacency_list:
            for w in self.__adjacency_list[v]:
                print("{0} -> {1}".format(v, w))

    def shortest_path(self, start, end, path=[]):
        path += [start]
        if start == end:
            return path
        shortest = None
        for v in self.__adjacency_list[start]:
            if v not in path:
                new_path = self.shortest_path(v, end, path)
                if new_path:
                    if not shortest or len(new_path) < len(shortest):
                        shortest = new_path
        return shortest
    
    def dfs_timestamp(self, start, discover_time={}, finish_time={}, node_set=None, time=0):
        if node_set is None:
            node_set = set()
        discover_time[start] = time
        time += 1
        node_set.add(start)
        for u in self.adjacency_list[start]:
            if u in node_set:
                continue
            self.dfs_timestamp(u, discover_time, finish_time, node_set, time)
        finish_time[start] = time
        time += 1
        return {"discovered": discover_time,
                "finished": finish_time,
                "time": time}

    def iter_deep_dfs(self, start):
        yielded = set()
        def recurse(start, d, S=None):
            if start not in yielded:
                yield start
                yielded.add(start)
            if d == 0: #max depth is zero, backtrack
                return
            if S is None:
                S = set()
            S.add(start)
            for u in self.adjacency_list[start]:
                if u in S:
                    continue
                for v in recurse(u, d-1, S):
                    yield v
        n = len(self.adjacency_list)
        for d in range(n):
            if len(yielded) == n:
                break
            for u in recurse(start, d):
                yield u

    def dfs(self, start, node_set=set()):
        queue = []
        queue.append(start)
        while queue:
            u = queue.pop()
            if u in node_set:
                continue
            node_set.add(u)
            queue.extend(self.adjacency_list[u])
            yield u

    def get_weight(self, u, v):
        weight = self.__weighted_adj_list[u][v]
        return weight 

    def weighted_matrix(self):
        size = len(self.__vertex_list)
        index_id = {}
        matrix = [[0 for x in range(size)] for y in range(size)]
        index = 0
        for i in sorted(self.__vertex_list):
            index_id[i] = index
            index += 1
        for u in sorted(self.__weighted_adj_list):
            for v in sorted(self.__weighted_adj_list[u]):
                matrix[index_id[u]][index_id[v]] = self.__weighted_adj_list[u][v]
        return matrix

    def matrix(self):
        """  
>>> graph = Graph()
>>> graph.add_vertex("a")
>>> graph.add_vertex("b")
>>> graph.add_vertex("c")  
>>> graph.add_vertex("d")
>>> graph.add_vertex("e")
>>> graph.add_vertex("f")
>>> graph.add_edge("a", "c")
>>> graph.add_edge("a", "f")
>>> graph.add_edge("b", "c")
>>> graph.add_edge("b", "d")
>>> graph.add_edge("b", "f")
>>> graph.add_edge("c", "d")
>>> graph.add_edge("d", "e")
>>> graph.add_edge("d", "f")
>>> graph.add_edge("e", "f")
>>> graph.print_matrix()
...     [0, 0, 1, 0, 0, 1]
...     [0, 0, 1, 1, 0, 1]
...     [0, 0, 0, 1, 0, 0]
...     [0, 0, 0, 0, 1, 1]
...     [0, 0, 0, 0, 0, 1]
...     [0, 0, 0, 0, 0, 0]
        """
        keys = sorted(self.__adjacency_list.keys())
        size = len(keys)
        vertex_indices = dict(zip(keys, range(size)))
        matrix = [[0 for x in range(size)] for y in range(size)]
        for i in range(size):
            for j in range(i, size):
                for e in self.__adjacency_list[keys[i]]:
                    j = vertex_indices[e]
                    matrix[i][j] = 1
        return matrix

def print_matrix(matrix):
    for x in matrix:
        print(x)

def transpose(matrix):
    size = len(matrix)
    res = [[matrix[y][x] for y in range(size)] for x in range(len(matrix[0]))]
    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod() 