# Dijkstra’s algorithm

## Purpose (solved problem)

An algorithm for **finding the shortest paths between nodes in a graph**.

The algorithm exists in many variants. Dijkstra's original algorithm found the shortest path between two given nodes but __a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree__.

### Use cases

* calculating least-cost paths to establish tracks of electricity lines or oil pipelines.
* calculating optimal long-distance footpaths in Ethiopia and contrast them with the situation on the ground.
* network routing protocols, most notably **IS-IS (Intermediate System to Intermediate System)** and **Open Shortest Path First (OSPF)**
* employed as a subroutine in other algorithms such as Johnson's.

### Current methods of solving the problem (addressed by the algorithm)