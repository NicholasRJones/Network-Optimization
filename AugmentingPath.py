import numpy as np
import ReverseSearch as rs
import ForwardStar as fs


def augpath(fsrep, Opoint, start, end):
    # Initialize algorithm
    # 1) Create residual network
    n, m = len(np.unique([fsrep[0], fsrep[1]]).tolist()), len(fsrep[0].tolist())
    tail, head, cap = fsrep[0].tolist(), fsrep[1].tolist(), fsrep[2].tolist()
    flow = np.zeros(m, dtype=int).tolist()
    ResNet, point = fs.fstar(tail + head, head + tail, '', cap + flow)
    # 2) Obtain exact distance labels
    distance = rs.reverse(fsrep, end)[1]
    pred = -np.ones(n, dtype=int)
    visited = np.zeros(n, dtype=int)
    i = start + 0
    while distance[start - 1] < n:
        admissible = False
        init = point[i - 1]
        check = [distance[i - 1]]
        # Find an admissible arc
        for j in range(point[i] - init):
            iterate = ResNet[1, (init + j)]
            if ResNet[2, init + j] != 0:
                check.append(distance[iterate - 1])
                if distance[iterate - 1] < distance[i - 1]:
                    admissible = True
                    break
        if admissible and visited[iterate - 1] == 0:
            # Move to next node
            pred[iterate - 1] = i + 0
            visited[iterate - 1] = 1
            i = iterate + 0
            if i == end:
                # Use this augmenting path
                PathIndex = []
                RPathIndex = []
                PathCap = []
                while i != start:
                    j = pred[i - 1] + 0
                    PathIndex.append(np.where(ResNet[1, point[j - 1]:point[j]] == i)[0][0] + point[j - 1])
                    RPathIndex.append(np.where(ResNet[1, point[i - 1]:point[i]] == j)[0][0] + point[i - 1])
                    PathCap.append(ResNet[2, PathIndex[len(PathIndex) - 1]])
                    i = j + 0
                MinCap = min(PathCap)
                for k in range(len(PathIndex)):
                    # Update capacities in residual network
                    ResNet[2, PathIndex[k]] -= MinCap
                    ResNet[2, RPathIndex[k]] += MinCap
        else:
            # Correct distance labels and reset
            distance[i - 1] = min(check) + 1
            visited = np.zeros(n, dtype=int)
            i = start + 0
    for k in range(m):
        # Recover flow from residual network
        i, j = fsrep[0, k], fsrep[1, k]
        index = np.where(ResNet[1, point[i - 1]:point[i]] == j)[0][0]
        flow[k] = fsrep[2, k] - ResNet[2, index + point[i - 1]]
    flowvalue = sum([flow[Opoint[start - 1] + k] for k in range(Opoint[start] - Opoint[start - 1])])
    return flowvalue, flow
