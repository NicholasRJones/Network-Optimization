import numpy as np
import ForwardStar as fs
import ReverseSearch as rs


def preflowpush(fsrep, Opoint, start, end):
    # Initialize algorithm
    # 1) Create residual network
    n, m = len(np.unique([fsrep[0], fsrep[1]]).tolist()), len(fsrep[0].tolist())
    tail, head, cap = fsrep[0].tolist(), fsrep[1].tolist(), fsrep[2].tolist()
    flow = np.zeros(m, dtype=int).tolist()
    excess = np.zeros(n, dtype=int)
    ACTIVE = []
    for i in range(Opoint[start] - Opoint[start - 1]):
        flow[Opoint[start - 1] + i] = fsrep[2, Opoint[start - 1] + i] + 0
        excess[fsrep[1, Opoint[start - 1] + i] - 1] = fsrep[2, Opoint[start - 1] + i] + 0
        cap[Opoint[start - 1] + i] = 0
        ACTIVE.append(fsrep[1, Opoint[start - 1] + i])
    ResNet, point = fs.fstar(tail + head, head + tail, '', cap + flow)
    # 2) Obtain distance labels
    distance = rs.reverse(fsrep, end)[1]
    distance[start - 1] = n
    while len(ACTIVE) > 0:
        # Iterate while flow balance is not met
        i = ACTIVE[0]
        while i in ACTIVE:
            admissible = False
            init = point[i - 1]
            check = []
            # Find an admissible arc
            for j in range(point[i] - init):
                if ResNet[2, init + j] != 0:
                    check.append(distance[ResNet[1, (init + j)] - 1])
                    if check[len(check) - 1] < distance[i - 1]:
                        index = init + j
                        admissible = True
                        break
            if admissible:
                # Push flow along admissible arc
                delta = min(excess[i - 1], ResNet[2, index])
                ResNet[2, index] -= delta
                j = ResNet[1, index]
                index = np.where(ResNet[1, point[j - 1]:point[j]] == i)[0] + point[j - 1]
                ResNet[2, index] += delta
                excess[i - 1] -= delta
                excess[j - 1] += delta
                # Update lists
                if j not in ACTIVE and j != start and j != end:
                    ACTIVE.append(j)
                if excess[i - 1] == 0:
                    ACTIVE.remove(i)
            else:
                # Correct distance labels
                distance[i - 1] = min(check) + 1
                ACTIVE.remove(i)
                ACTIVE.append(i)
                break
    for k in range(m):
        # Recover flow from residual network
        i, j = fsrep[0, k], fsrep[1, k]
        index = np.where(ResNet[1, point[i - 1]:point[i]] == j)[0][0]
        flow[k] = fsrep[2, k] - ResNet[2, index + point[i - 1]]
    flowvalue = sum([flow[Opoint[start - 1] + k] for k in range(Opoint[start] - Opoint[start - 1])])
    return flowvalue, flow
