class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = []

    def add_neighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node)

    def remove_neighbor(self, neighbor_node):
        if neighbor_node in self.neighbors:
            self.neighbors.remove(neighbor_node)


class Edge:
    def __init__(self, start_node, end_node, weight=0):
        self.start_node = start_node
        self.end_node = end_node
        self.weight = weight


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node_id):
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id)

    def add_edge(self, start_node_id, end_node_id, weight=0):
        if start_node_id not in self.nodes:
            self.add_node(start_node_id)
        if end_node_id not in self.nodes:
            self.add_node(end_node_id)
        start_node = self.nodes[start_node_id]
        end_node = self.nodes[end_node_id]
        edge = Edge(start_node, end_node, weight)
        self.edges.append(edge)
        start_node.add_neighbor(end_node)
        end_node.add_neighbor(start_node)

    def remove_edge(self, start_node_id, end_node_id):
        for edge in self.edges:
            if edge.start_node.id == start_node_id and edge.end_node.id == end_node_id:
                self.edges.remove(edge)
                edge.start_node.remove_neighbor(edge.end_node)
                edge.end_node.remove_neighbor(edge.start_node)
                break

    def remove_node(self, node_id):
        if node_id in self.nodes:
            del self.nodes[node_id]
            for edge in self.edges:
                if edge.start_node.id == node_id or edge.end_node.id == node_id:
                    self.edges.remove(edge)

    def __str__(self):
        return f"Nodes: {[node.id for node in self.nodes.values()]}\nEdges: {[(edge.start_node.id, edge.end_node.id) for edge in self.edges]}"

graph = Graph()

with open('City Nodes for graph.txt', 'r') as file:
    for line in file:
        start_node, end_node, weight = line.strip().split(', ')
        graph.add_edge(start_node, end_node, int(weight))

print(graph)