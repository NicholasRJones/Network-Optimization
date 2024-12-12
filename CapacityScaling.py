import numpy as np
import ForwardStar as fs
import BFS as BFS


def capacityscaling(fsrep, Opoint, start, end):
    # Initialize algorithm
    # 1) Create residual network
    n, m = len(np.unique([fsrep[0], fsrep[1]]).tolist()), len(fsrep[0].tolist())
    tail, head, cap = fsrep[0].tolist(), fsrep[1].tolist(), fsrep[2].tolist()
    Delta = 2 ** np.floor(np.log(max(cap)))
    flow = np.zeros(m, dtype=int).tolist()
    ResNet, point = fs.fstar(tail + head, head + tail, '', cap + flow)
    while Delta >= 1:
        # Iterate while Delta is large enough.
        third_row = ResNet[2, :]
        filtered_columns = third_row >= Delta
        DeltaRes = ResNet[:, filtered_columns]
        DeltaRes, Dpoint = fs.fstar(DeltaRes[0].tolist(), DeltaRes[1].tolist(), '', DeltaRes[2].tolist())
        pred, distance = BFS.BFS(DeltaRes, Dpoint, start, end)
        while len(pred) > 0:
            # Identify the s-t path
            PathIndex = []
            RPathIndex = []
            PathCap = []
            i = end + 0
            while i != start:
                j = int(pred[i - 1])
                PathIndex.append(np.where(ResNet[1, point[j - 1]:point[j]] == i)[0][0] + point[j - 1])
                RPathIndex.append(np.where(ResNet[1, point[i - 1]:point[i]] == j)[0][0] + point[i - 1])
                PathCap.append(ResNet[2, PathIndex[len(PathIndex) - 1]])
                i = j + 0
            MinCap = min(PathCap)
            for k in range(len(PathIndex)):
                # Update capacities in residual network
                ResNet[2, PathIndex[k]] -= MinCap
                ResNet[2, RPathIndex[k]] += MinCap
            # Check for more paths
            third_row = ResNet[2, :]
            filtered_columns = third_row >= Delta
            DeltaRes = ResNet[:, filtered_columns]
            DeltaRes, Dpoint = fs.fstar(DeltaRes[0].tolist(), DeltaRes[1].tolist(), '', DeltaRes[2].tolist())
            pred, distance = BFS.BFS(DeltaRes, Dpoint, start, end)
        Delta = Delta / 2
    for k in range(m):
        # Recover flow from residual network
        i, j = fsrep[0, k], fsrep[1, k]
        index = np.where(ResNet[1, point[i - 1]:point[i]] == j)[0][0]
        flow[k] = fsrep[2, k] - ResNet[2, index + point[i - 1]]
    flowvalue = sum([flow[Opoint[start - 1] + k] for k in range(Opoint[start] - Opoint[start - 1])])
    return flowvalue, flow
