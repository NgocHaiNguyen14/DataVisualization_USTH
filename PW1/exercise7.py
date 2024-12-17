import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

def bfs_edges(G, s):
    """
    Perform a breadth-first search (BFS) on the graph G starting from node s.
    
    Parameters:
        G (networkx.Graph): The input graph.
        s (any): The starting node.
        
    Returns:
        list of tuple: List of edges (arcs) in the BFS tree starting from node s.
    """
    visited = set()  # Set to keep track of visited nodes
    bfs_tree_edges = []  # List to store edges of the BFS tree
    queue = deque([s])  # Initialize the queue with the starting node
    
    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in G.neighbors(current_node):
                if neighbor not in visited:
                    bfs_tree_edges.append((current_node, neighbor))  # Add edge to BFS tree
                    queue.append(neighbor)
    
    return bfs_tree_edges

# Example usage
G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (5, 6), (4, 7)])

start_node = 1
bfs_tree = bfs_edges(G, start_node)

print(f"BFS tree edges starting from node {start_node}: {bfs_tree}")

bfs_tree_graph = nx.DiGraph(bfs_tree)
pos = nx.spring_layout(G)

# Plot the graph
nx.draw_networkx(G, pos, with_labels=True, node_color="lightblue", node_size=800, alpha=0.5)
nx.draw_networkx_edges(bfs_tree_graph, pos, edge_color="red", width=2.5)

# Correct method to set the title
plt.gca().set_title(f"BFS Tree Starting from Node {start_node}")

plt.show()
