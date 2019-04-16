# Pocket Cube

The goal of this project it to determine the speed up associated with computational optimisations using mathematical methods to find God's number. In this case the2x2x2 Rubik's Cube (commonly called the Pocket Cube) can be represented as a group of moves, G,  where each move, m in G, takes the cube from a solved configuration to a unique configuration of the Pocket Cube. There are 3,674,160 such configurations and, respectively, unique moves which make up the group G.

--------------------------------------------------------------
Step 1:

The first step is to run a brute force method to finding God's number. This is done using a breadth first search beginning at the solved configuration (initial node). The node's of this graph are the possible valid configurations of the Pocket Cube and the edges between nodes are the half-turn metric basic moves (U1, F1, R1, U2, ...) which take the Pocket Cube from one configuration to another. The shortest path from the initial node to each and every node represents the elements of the group G, and the longest of these shortest paths represents God's number.
