import ForwardStar as fs
import Dijkstra as D
import networkx as nx
import matplotlib.pyplot as plt

tail = [1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 6]
head = [2, 3, 4, 3, 2, 5, 3, 5, 6, 4, 5]
cost = [2, 8, 3, 5, 6, 0, 1, 7, 6, 4, 2]

fsrep, point = fs.fstar(tail, head, cost, '')
pred, distance = D.DIJK(fsrep, point, 1)
print('pred:' + '___' + str(pred))
print('distance:' + '___' + str(distance))

nxG = nx.DiGraph()
LIST = []
for j in range(len(pred)):
    if pred[j] != 0:
        if pred[j] not in LIST:
            nxG.add_node(str(int(pred[j])))
            LIST.append(pred[j])
        nxG.add_edge(str(int(pred[j])), str(j + 1))

nx.draw(nxG, with_labels=True)
plt.plot()
plt.show()
