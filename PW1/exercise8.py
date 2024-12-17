import matplotlib.pyplot as plt
import networkx as nx

def dfs_with_step_labels(G, s):
    """
    Perform a depth-first search (DFS) on the graph G starting from node s,
    and visualize the edges with step numbers.
    
    Parameters:
        G (networkx.Graph): The input graph.
        s (any): The starting node.
    """
    visited = set()
    dfs_tree_edges = []  # To store DFS tree edges with step numbers
    step = 1  # Step counter

    def dfs_recursive(node, step):
        visited.add(node)
        for neighbor in G.neighbors(node):
            if neighbor not in visited:
                dfs_tree_edges.append(((node, neighbor), step))
                step = dfs_recursive(neighbor, step + 1)
        return step

    # Start the DFS
    dfs_recursive(s, step)

    # Create a new graph with the DFS tree edges
    dfs_tree = nx.DiGraph()
    dfs_tree.add_edges_from([edge for edge, _ in dfs_tree_edges])

    # Generate positions for consistent visualization
    pos = nx.spring_layout(dfs_tree)

    # Draw the nodes and edges of the DFS tree
    plt.figure(figsize=(8, 6))
    nx.draw_networkx(dfs_tree, pos, with_labels=True, node_color="lightgreen", node_size=800, edge_color="black")

    # Add step labels to the edges
    edge_labels = {edge: str(step) for edge, step in dfs_tree_edges}
    nx.draw_networkx_edge_labels(dfs_tree, pos, edge_labels=edge_labels, font_size=10, font_color="blue")

    plt.title(f"DFS Tree Starting from Node {s}", fontsize=14)
    plt.show()

# Example usage
G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (5, 6), (4, 7)])

start_node = 1
dfs_with_step_labels(G, start_node)
