import ForwardStar as fs
import PreflowPush as pp
import networkx as nx
import matplotlib.pyplot as plt

tail = [1, 1, 1, 2, 3, 3, 4, 4, 5, 5]
head = [2, 3, 4, 5, 4, 6, 2, 6, 4, 6]
cap = [3, 3, 2, 4, 1, 2, 1, 2, 1, 1]

print(
    '------------------------------------------------------------------------------------------------------------------------------')
print('Solving Network using Preflow-Push Algo')
print(
    '------------------------------------------------------------------------------------------------------------------------------')

fsrep, point = fs.fstar(tail, head, '', cap)
flowvalue, flow = pp.preflowpush(fsrep, point, 1, 6)
print('Flow Value:' + '___' + str(flowvalue))
print('Flow Vector:' + '___' + str(flow))


nxG = nx.DiGraph()
LIST = []
for j in range(len(fsrep[0])):
    if fsrep[0, j] not in LIST:
        nxG.add_node(str(int(fsrep[0, j])))
        LIST.append(fsrep[0, j])
    if fsrep[1, j] not in LIST:
        nxG.add_node(str(int(fsrep[1, j])))
        LIST.append(fsrep[1, j])
    nxG.add_edge(str(int(fsrep[0, j])), str(fsrep[1, j]), flow=str(flow[j]))

edge_labels = nx.get_edge_attributes(nxG, 'flow')
pos = nx.spring_layout(nxG)
nx.draw(nxG, pos, with_labels=True, arrows=True)
nx.draw_networkx_edge_labels(nxG, pos, edge_labels=edge_labels)
plt.plot()
plt.show()
