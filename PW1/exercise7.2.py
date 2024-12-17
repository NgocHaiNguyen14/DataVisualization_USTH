import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import time

def bfs_edges_step_by_step(G, s):
    """
    Perform a breadth-first search (BFS) on the graph G starting from node s.
    Visualize the traversal step-by-step.
    
    Parameters:
        G (networkx.Graph): The input graph.
        s (any): The starting node.
    """
    visited = set()  # Set to keep track of visited nodes
    queue = deque([s])  # Initialize the queue with the starting node
    pos = nx.spring_layout(G)  # Layout for consistent visualization

    plt.ion()  # Turn on interactive mode for live plotting
    fig, ax = plt.subplots(figsize=(8, 6))

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in G.neighbors(current_node):
                if neighbor not in visited:
                    # Draw the graph up to this point
                    ax.clear()
                    nx.draw_networkx(G, pos, with_labels=True, node_color="lightblue", node_size=800, alpha=0.5)
                    nx.draw_networkx_edges(
                        G, pos, edgelist=[(current_node, neighbor)], edge_color="red", width=2.5
                    )
                    plt.title(f"Exploring Edge: ({current_node}, {neighbor})", fontsize=14)
                    plt.pause(1)  # Pause for visualization
                    queue.append(neighbor)

    plt.ioff()  # Turn off interactive mode
    plt.show()

# Example usage
G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (5, 6), (4, 7)])

start_node = 1
bfs_edges_step_by_step(G, start_node)
