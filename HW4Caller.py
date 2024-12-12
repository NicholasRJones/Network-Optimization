import ForwardStar as fs
import BFS as b
import networkx as nx
import matplotlib.pyplot as plt


tails = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7, 7, 9]
heads = [2, 3, 5, 4, 5, 5, 6, 5, 8, 6, 7, 9, 4, 5, 8, 8]

fsrep, point = fs.fstar(tails, heads, '', '')
pred, distance = b.BFS(fsrep, point, 1)
print('pred:' + '___' + str(pred))
print('order:' + '___' + str(distance))

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
