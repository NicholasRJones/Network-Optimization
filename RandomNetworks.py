import random
import numpy as np
import ForwardStar as fs

def generate_random_network(n, m, U):
    edges = []
    # Guarantee at least one s-t path
    for i in range(1, n):
        edges.append((i, i + 1))
    # Randomly add the remaining arcs to satisfy the arc count m
    while len(edges) < m:
        u = random.randint(1, n)
        v = random.randint(1, n)
        if u != v and (u, v) not in edges and (v, u) not in edges:
            edges.append((u, v))
    # Convert to tail, head, capacity lists
    tail = []
    head = []
    cap = []
    for i in range(len(edges)):
        tail.append(edges[i][0])
        head.append(edges[i][1])
        cap.append(random.randint(1, U))
    return tail, head, cap


# Open the file to write the output
with open("random_networks_output.txt", "w") as f:
    for n in range(1, 21):
        for iteration in range(50):
            nodes = 10 * n
            edges = 3 * nodes
            capacity = nodes / 2
            tail, head, cap = generate_random_network(nodes, edges, capacity)
            fsrep, point = fs.fstar(tail, head, '', cap)
            np.set_printoptions(threshold=np.inf)
            fsrep_rows = ['[' + ', '.join(map(str, row)) + ']' for row in fsrep]
            fsrep_str = ', '.join(fsrep_rows)
            point_str = ', '.join(map(str, point))
            f.write(f"Network {50 * (n - 1) + iteration + 1}:\n")
            f.write(f"Nodes:{nodes}\n")
            f.write(f"Edges:{edges}\n")
            f.write(f"Capacity:{capacity}\n")
            f.write("ForwardStar Representation:\n")
            f.write(f"fsrep: {fsrep_str}\n")
            f.write(f"point: [{point_str}]\n")
            f.write("-" * 40 + "\n")
