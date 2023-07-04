"""
Graphs
"""

class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        print()
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])
        print()

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys() and v2 in self.adj_list[v1] and v1 in self.adj_list[v2]:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False

    # def remove_vertex(self, vertex):
    #     if vertex in self.adj_list.keys():
    #         for v in self.adj_list[vertex]:
    #             self.remove_edge(vertex, v)
    #         del self.adj_list[vertex]
    #         return True
    #     return False


def _main():
    my_graph = Graph()

    my_graph.add_vertex("A")
    my_graph.add_vertex("B")
    my_graph.add_vertex("C")
    my_graph.print_graph()

    my_graph.add_edge("A", "B")
    my_graph.add_edge("A", "C")
    my_graph.add_edge("B", "C")
    my_graph.print_graph()

    my_graph.remove_edge("A", "B")
    my_graph.print_graph()

    # my_graph.remove_vertex("B")
    # my_graph.print_graph()

def _exercises():
    pass

if __name__ == "__main__":
    _main()
    _exercises()