import numpy as np


def fstar(tail, head, cost, cap):
    n = len(head)
    if cost == '' and cap == '':
        fsrep = np.array((tail, head)).reshape((2, n))
    elif cap == '':
        fsrep = np.array((tail, head, cost)).reshape((3, n))
    elif cost == '':
        fsrep = np.array((tail, head, cap)).reshape((3, n))
    else:
        fsrep = np.array((tail, head, cost, cap)).reshape((4, n))
    fsrep = fsrep[:, fsrep[0, :].argsort()]
    list = np.unique(tail + head)
    point = np.zeros(max(list), dtype=int)
    for i in range(1, max(list) + 1):
        if i in tail:
            point = np.insert(point, i, point[i - 1] + tail.count(i))
            a, b = point[i - 1], point[i]
            fsrep[:, a:b] = fsrep[:, (fsrep[1, a:b].argsort() + a)]
        else:
            point = np.insert(point, i, point[i - 1])
    return fsrep, point
