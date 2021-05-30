# Dijkstra’s algorithm

## Purpose (solved problem)

An algorithm for **finding the shortest paths between nodes in a graph**.

The algorithm exists in many variants. Dijkstra's original algorithm found the shortest path between two given nodes but __a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree__.

### Use cases

* calculating least-cost paths to establish tracks of electricity lines or oil pipelines.
* calculating optimal long-distance footpaths in Ethiopia and contrast them with the situation on the ground.
* network routing protocols, most notably **IS-IS (Intermediate System to Intermediate System)** and **Open Shortest Path First (OSPF)**
* employed as a subroutine in other algorithms such as Johnson's.
* game development - path finding for eg. enemy entities
* It is most widely used in finding shortest possible distance and show directions between 2 geographical locations such as in Google Maps.
* Social Networking Applications
* Widely used in routing of data in networking and telecommunication domains for minimizing the delay occurred for transmission.
* Robotic Path: the robot/drone moves in the ordered direction by following the shortest path to keep delivering the package in a minimum amount of time.

### Current methods of solving the problem (addressed by the algorithm)

* game development - A* algorithm seems to be more frequently in use nowadays
* Dijkstra’s Algorithm doesnt work for graphs with negative edges. Algorithms like Bellman-Ford Algorithm will be used for such cases.
