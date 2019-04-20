from _collections import defaultdict
class Graph:
    # Constructor
    def __init__(self):
        # default dic to store graph
        self.graph = defaultdict(list)

    # adding edge to graph
    def addEdge(self, source, destination):
        self.graph[source].append(destination)

    # BFS
    def BFS(self, s):
        visited = [False] * (len(self.graph))

        queue = []
        queue.append(s)
        visited[s] = True;

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            print(visited)

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.BFS(2)