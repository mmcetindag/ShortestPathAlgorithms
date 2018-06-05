import queue
from collections import namedtuple

edge = namedtuple('edge', ['vertex', 'weight'])

class GraphUndirectedWeighted(object):
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adjacency_list = [[] for _ in range(vertex_count)]

    def add_edge(self, source, dest, weight):
        assert source < self.vertex_count
        assert dest < self.vertex_count
        self.adjacency_list[source].append(edge(dest, weight))
        self.adjacency_list[dest].append(edge(source, weight))

    def get_edge(self, vertex):
        for e in self.adjacency_list[vertex]:
            yield e

    def get_vertex(self):
        for v in range(self.vertex_count):
            yield v


def dijkstra(graph, source, dest):
    q = queue.PriorityQueue()
    parents = []
    distances = []
    start_weight = float("inf")

    for i in graph.get_vertex():
        weight = start_weight
        if source == i:
            weight = 0
        distances.append(weight)
        parents.append(None)

    q.put(([0, source]))

    while not q.empty():
        v_tuple = q.get()
        v = v_tuple[1]

        for e in graph.get_edge(v):
            candidate_distance = distances[v] + e.weight
            if distances[e.vertex] > candidate_distance:
                distances[e.vertex] = candidate_distance
                parents[e.vertex] = v
                # primitive but effective negative cycle detection
                if candidate_distance < -1000:
                    raise Exception("Negative cycle detected")
                q.put(([distances[e.vertex], e.vertex]))

    shortest_path = []
    end = dest
    while end is not None:
        shortest_path.append(end)
        end = parents[end]

    shortest_path.reverse()

    return shortest_path, distances[dest]


g = GraphUndirectedWeighted(9)
g.add_edge(0, 1, 4)
g.add_edge(1, 7, 6)
g.add_edge(1, 2, 1)
g.add_edge(2, 3, 3)
g.add_edge(3, 7, 1)
g.add_edge(3, 4, 2)
g.add_edge(3, 5, 1)
g.add_edge(4, 5, 1)
g.add_edge(5, 6, 1)
g.add_edge(6, 7, 2)
g.add_edge(6, 8, 2)
g.add_edge(7, 8, 2)

shortest_path, distance = dijkstra(g, 0, 4)
print("shortest_path = " + str(shortest_path) + ", distance = " + str(distance))