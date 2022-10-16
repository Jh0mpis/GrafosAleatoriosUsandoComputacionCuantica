import numpy as np
from matplotlib import pyplot as plt
import networkx as nx
import pandas as pd
import random
from qiskit import QuantumCircuit
import qiskit

np.random.seed(823)

n = 5

G1 = nx.balanced_tree(2,n)
G2 = nx.balanced_tree(2,n)
G3 = nx.union(G1,G2,rename=('1-','2-'))

HaveConnection = pd.Series({i:0 for i in range(2**(n)-1,2**(n+1)-1)})

def GenEdges(HaveConnection):
    return random.sample(list(HaveConnection.where(HaveConnection<2).dropna().index),2)

for i in range(2**n-1,2**(n+1)-1):
    newEdges = GenEdges(HaveConnection)
    for j in newEdges:
        G3.add_edge(f'1-{i}',f'2-{j}')
        HaveConnection[j] += 1

pos = {}
pos[f'1-0'] = (0,0.5)
pos[f'2-0'] = (1,0.5)

for i in range(1,n+1):
    print(i        /(2*n+1))
    for j in range(2**i,2**(i+1)):
        print(i        /(2*n+1),(j+1-2**i)/(2**i+1))
        pos[f'1-{j-1}'] = (i        /(2*n+1),(2*((j-2**i)/(2**i-1))-1)*(0.1*i)+0.5)
        pos[f'2-{j-1}'] = ((2*n-i+1)/(2*n+1),(2*((j-2**i)/(2**i-1))-1)*(0.1*i)+0.5)
xs = np.linspace(0,1,12)

# nx.draw(G1,with_labels=True)
# plt.show()
# nx.draw(G2,with_labels=True)
# plt.show()

# nx.draw(G3,with_labels=True)
# plt.show()

nx.draw(G3,pos,node_size=15,style='--',node_color='b')
# plt.show()

circ = QuantumCircuit(1,1)
circ.h(0)
circ.measure([0],[0])
# circ.draw('mpl')
SimBackend = qiskit.Aer.get_backend('qasm_simulator')

camino = ''
ys = [0.5]
for i in range(n+1):
    Circuito = qiskit.execute(circ,backend=SimBackend,shots=1)
    camino += max(Circuito.result().get_counts(),key=Circuito.result().get_counts().get)
    if i < n:
        dy = 1/((2*i+3)*2)
        if camino[-1] == '0':dy*=-1
        ys.append(ys[-1]+dy)
# plt.plot(xs[:len(ys)],ys,'r-')
print(camino)
plt.show()
