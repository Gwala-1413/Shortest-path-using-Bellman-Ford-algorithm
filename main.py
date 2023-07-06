class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def print_solution(self, dist, path):
        print("Vertex\tDistance from Source\tShortest Path")
        for i in range(self.V):
            shortest_path = " -> ".join(map(str, path[i]))
            print(f"{i}\t{dist[i]}\t\t\t{shortest_path}")

    def bellman_ford(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0
        path = [[] for _ in range(self.V)]
        path[src].append(src)

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    path[v] = path[u] + [v]

        for u, v, w in self.graph:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                raise ValueError("Graph contains negative weight cycle")

        return dist, path


def get_int_input(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def create_graph():
    vertices = get_int_input("\nEnter the number of vertices in the graph: ")
    edges = get_int_input("\nEnter the number of edges in the graph: ")

    graph = Graph(vertices)

    print("\nEnter edge details (source destination weight):")
    for i in range(edges):
        while True:
            try:
                inputs = input(f"Enter edge {i+1}: ").split()
                if len(inputs) != 3:
                    raise ValueError
                source, destination, weight = map(int, inputs)
                graph.add_edge(source, destination, weight)
                break
            except ValueError:
                print("Invalid input. Please enter three integers separated by spaces.")

    return graph


def find_shortest_path():
    graph = create_graph()
    source = get_int_input("\nEnter the source vertex: ")
    destination = get_int_input("\nEnter the destination vertex: ")

    try:
        shortest_distances, shortest_paths = graph.bellman_ford(source)
        shortest_distance = shortest_distances[destination]
        shortest_path = shortest_paths[destination]
        print(f"\nThe shortest distance from vertex {source} to vertex {destination} is: {shortest_distance}")
        print("\nThe shortest path traveled is: ", " -> ".join(map(str, shortest_path)))
        #print_solution()
    except ValueError as e:
        print("Error:", str(e))


def print_menu():
    print("\nMenu:")
    print("1. Find Shortest Path")
    print("2. Exit")


def main():
    print("\nShortest Path using Bellman-Ford Algorithm\n")
    while True:
        print_menu()
        choice = get_int_input("\nEnter your choice (1-2): ")

        if choice == 1:
            find_shortest_path()
        elif choice == 2:
            print("\nExiting the program...")
            break
        else:
            print("\nInvalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
