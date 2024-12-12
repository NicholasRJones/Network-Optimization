import ForwardStar as fs
import BFS


def reverse(fsrep, end):
    head, tail = fsrep[0].tolist(), fsrep[1].tolist()
    rfsrep, point = fs.fstar(tail, head, '', '')
    pred, distance = BFS.BFS(rfsrep, point, end)
    return pred, distance
