import sys
import networkx as nx

# Custom class
# for extracting minimal length path from source to destination node,
# on a NetworkX undirected Graph,
# using my dijkstra algorithm implementation
class DijkstraSolver:
    def __init__(self, _graph: nx.Graph):
        self.graph = _graph

    # Get node, that:
    # - is not in shortest path tree,
    # - has the minmal distance value in dist list
    def min_distance_node(self, dist, sptSet):
        # Initilaize the min with the greatest value
        min = sys.maxsize

        # Iterate through nodes finding the right one
        for node in self.graph.nodes:
            if dist[node] < min and sptSet[node] == False:
                min = dist[node]
                min_index = node

        # Retrun nearest node not in the shortest path tree
        return min_index

    # Get node, that:
    # - has edge to current_node
    # - creates the shortest path with current_node
    def prev_path_node(self, current_node, source_node, dist, sptSet):
        min_path_val = sys.maxsize
        edge_start = current_node

        if current_node == source_node:
            return current_node
        else:
            for prev_node in self.graph.nodes:
                if sptSet[prev_node] == True and current_node in self.graph.neighbors(
                    prev_node
                ):
                    edge_lenght = self.graph[prev_node][current_node]["weight"]
                    curr_path = dist[prev_node] + edge_lenght
                    if curr_path < min_path_val:
                        min_path_val = curr_path
                        edge_start = prev_node

        # return the prev_node
        return edge_start

    # Extract shortest path from source to destination node
    def get_min_path(self, src, dest):
        # Initilaize minimal distances (from source node)
        # to all nodes with the greatest value
        dist = [sys.maxsize] * len(self.graph.edges)
        # set minimal distance (from source node)
        # to source node as 0
        dist[src] = 0
        # Initilaize shortest paths to all nodes as not found
        sptSet = [False] * len(self.graph.edges)
        # Initilaize shortest paths to all nodes as empty
        paths = [[]] * len(self.graph.edges)

        for node in self.graph.nodes:
            # Choose the node of minimum distance from
            # the nodes without set shortest path tree
            u = self.min_distance_node(dist, sptSet)

            # when adding a new node to the path (stpSet[node] == True)
            # find a node already on the path (u_path_predecesor), that
            # creates the shortest path with the new node
            u_path_predecesor = self.prev_path_node(u, src, dist, sptSet)
            # save the shortest path to the new node as
            # the shortest path to u_path_predecesor
            # with appended new node
            paths[u] = paths[u_path_predecesor].copy()
            paths[u].append(u)

            # Set the shortest path tree for the current node as found
            sptSet[u] = True

            # Set new distance value of neighbouring nodes
            # of the picked node only if the current
            # distance is greater than new distance and
            # the node does not have the shotest path tree set
            for v in self.graph.neighbors(u):
                if (
                    sptSet[v] == False
                    and dist[v] > dist[u] + self.graph[u][v]["weight"]
                ):
                    dist[v] = dist[u] + self.graph[u][v]["weight"]

        # Return dict containing
        # minimum distance from source to destination node
        # path (node list) from source to destination node of min distance
        return {
            "length": dist[dest],
            "path": paths[dest],
        }
