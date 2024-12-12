import numpy as np


def BFS(fsrep, point, start, end=None):
    unmarked = np.arange(1, max(np.unique([fsrep[0], fsrep[1]])) + 1).tolist()
    if end != None:
        if end not in unmarked:
            return [], []
    pred = -np.ones(len(unmarked))
    pred[start - 1] = 0
    distance = 10e10 * np.ones(len(unmarked))
    unmarked.remove(start)
    distance[start - 1] = 0
    LIST = [start]
    while len(LIST) > 0:
        init = point[LIST[0] - 1]
        for j in range(point[LIST[0]] - init):
            iterate = fsrep[1, (init + j)]
            if iterate in unmarked:
                pred[iterate - 1] = LIST[0] + 0
                distance[iterate - 1] = distance[LIST[0] - 1] + 1
                LIST.append(iterate)
                unmarked.remove(iterate)
        LIST.remove(LIST[0])
    if end != None:
        if end in unmarked:
            return [], []
    return pred, distance
