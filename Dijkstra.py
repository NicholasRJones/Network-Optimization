import numpy as np


def DIJK(fsrep, point, start):
    n = len(np.unique([fsrep[0], fsrep[1]]))
    distance = 10 ** 10 * np.ones(n)
    distance[start - 1] = 0
    pred = np.zeros(n)
    LIST = [start]
    MLIST = []
    PLIST = [start]
    while len(LIST) > 0:
        i = LIST[0]
        LIST.remove(i)
        init = point[i - 1]
        for j in range(point[i] - init):
            iterate = fsrep[1, (init + j)]
            if iterate not in MLIST and iterate not in PLIST:
                MLIST.append(iterate)
            dtest = distance[i - 1] + fsrep[2, (init + j)]
            if dtest < distance[iterate - 1]:
                distance[iterate - 1] = dtest
                pred[iterate - 1] = i
        if len(MLIST) > 0:
            offset = [x - 1 for x in MLIST]
            ntest = min(distance[offset])
            newnode = (distance[offset].tolist()).index(ntest)
            newnode = MLIST[newnode]
            MLIST.remove(newnode)
            LIST.append(newnode)
            PLIST.append(newnode)
    return pred, distance
