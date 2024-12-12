import ForwardStar as fs
import LabelCorrecting as L
import networkx as nx
import matplotlib.pyplot as plt

tail = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7]
head = [2, 3, 3, 6, 4, 7, 2, 5, 6, 7, 5]
cost = [3, 2, 4, 5, 1, -4, -1, 5, -2, -4, 6]

print('------------------------------------------------------------------------------------------------------------------------------')
print('Solving Network using FIFO Label Correcting Algo')
print('------------------------------------------------------------------------------------------------------------------------------')

fsrep, point = fs.fstar(tail, head, cost, '')
pred, distance = L.labelcorrect(fsrep, point, 1)
print('pred:' + '___' + str(pred))
print('distance:' + '___' + str(distance))

nxG = nx.Graph()
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
