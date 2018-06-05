# ShortestPathAlgorithms
Dijkstra’s algorithm and Bellman Ford algorithm.

DIJKSTRA’S

The algorithm stores all nodes in a priority queue ordered by
distance of the node from the root – in the first iteration of the algorithm, only root has distance set to 0, distance of all other nodes is equal to infinity. Than in each step Dijkstra's algorithm picks from the queue a node with the highest priority (least distance from the root) a processes it and reevaluates
distances of all unprocessed descendants of the node. This means that the algorithm checks for all descendants that the following
condition holds.


BELLMAN FORD

The Bellman-Ford algorithm is based on the relaxation operation. The relaxation procedure takes two nodes as arguments and an edge connecting these nodes. If the distance from the source to the first node plus the edge length is less than distance to the second node, than the first node is denoted as the predecessor of the second node and the distance to the second node is recalculated. Otherwise no changes are applied
