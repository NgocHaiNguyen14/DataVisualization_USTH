import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

def bfs_with_step_labels(G, s):
    """
    Perform a breadth-first search (BFS) on the graph G starting from node s,
    and visualize the edges with step numbers.
    
    Parameters:
        G (networkx.Graph): The input graph.
        s (any): The starting node.
    """
    visited = set()
    queue = deque([s])
    bfs_tree_edges = []  # To store BFS tree edges
    step = 1  # Step counter

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in G.neighbors(current_node):
                if neighbor not in visited:
                    bfs_tree_edges.append(((current_node, neighbor), step))
                    queue.append(neighbor)
                    step += 1

    # Create a new graph with the BFS tree edges
    bfs_tree = nx.DiGraph()
    bfs_tree.add_edges_from([edge for edge, _ in bfs_tree_edges])

    # Generate positions for consistent visualization
    pos = nx.spring_layout(bfs_tree)

    # Draw the nodes and edges of the BFS tree
    plt.figure(figsize=(8, 6))
    nx.draw_networkx(bfs_tree, pos, with_labels=True, node_color="lightblue", node_size=800, edge_color="black")

    # Add step labels to the edges
    edge_labels = {edge: str(step) for edge, step in bfs_tree_edges}
    nx.draw_networkx_edge_labels(bfs_tree, pos, edge_labels=edge_labels, font_size=10, font_color="red")

    plt.title(f"BFS Tree Starting from Node {s}", fontsize=14)
    plt.show()

# Example usage
G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (5, 6), (4, 7)])

start_node = 1
bfs_with_step_labels(G, start_node)
