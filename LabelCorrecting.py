import numpy as np


def labelcorrect(fsrep, point, start):
    n = len(np.unique([fsrep[0], fsrep[1]]))
    distance = 10 ** 10 * np.ones(n)
    pred = np.zeros(n)
    distance[start - 1] = 0
    LIST = [start]
    while len(LIST) > 0:
        i = LIST[0]
        LIST.remove(i)
        init = point[i - 1]
        for j in range(point[i] - init):
            iterate = fsrep[1, (init + j)]
            dtest = distance[i - 1] + fsrep[2, (init + j)]
            if dtest < distance[iterate - 1]:
                distance[iterate - 1] = dtest
                pred[iterate - 1] = i
                if iterate not in LIST:
                    LIST.append(iterate)
    return pred, distance
