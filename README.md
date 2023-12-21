# 🚀 Bellman-Ford Shortest Path

This Python script uses the Bellman-Ford algorithm to find the shortest path in a weighted directed graph. It features an interactive menu and colorful output.

![image](https://github.com/Gwala-1413/Shortest-path-using-Bellman-Ford-algorithm/assets/115860146/1b0c4e7d-1fba-46fe-8203-91bb5f5d2175) 
![image](https://github.com/Gwala-1413/Shortest-path-using-Bellman-Ford-algorithm/assets/115860146/98b34321-0baa-4b58-8fe2-bf205bb58f76)


## 🌟 Features
- **Interactive Menu:** Choose options to find the shortest path or exit.
- **Graph Visualization:** Display shortest paths with vertices and distances.
- **Exception Handling:** Informative error messages for invalid inputs and negative weight cycles.
- **Colorful Output:** Attractive console output with colorful text.

## 🛠️ Usage
1. Run with `python filename.py`.
2. Choose option 1 to find the shortest path.
3. Input the following details:
    - Number of vertices in the graph.
    - Number of edges in the graph.
    - For each edge, enter source, destination, and weight (separated by spaces).
4. Enter the source and destination vertices.
5. View the shortest path and distance or handle errors.

## 📊 Graph Class
- Represents a weighted directed graph.
- `add_edge(u, v, w)`: Adds an edge with source `u`, destination `v`, and weight `w`.
- `bellman_ford(src)`: Finds shortest paths from the source vertex.

## 🎮 Main Functions
- `find_shortest_path()`: Creates a graph, finds paths, and prints results.
- `print_menu()`: Displays a colorful menu.
- `main()`: Main driver for user interaction.

## 📝 Menu Options
- Option 1: Find the shortest path.
- Option 2: Exit the program.

Feel free to contribute and improve this code! 🤝
