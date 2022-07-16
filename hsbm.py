import numpy as np
numV = 100
p_intra = 1 #probability of a hyperedge where vertices are in the same cluster
p_inter = 9 #probability of a hyperedge where vertices belong to different clusters
IDX = [0 for i in range(numV)]
for i in range(int(numV/2)):
    IDX[i] = 1
alloc = 1024
offset = 0
edges = np.zeros((3,alloc))

from random import random
from random import seed
seed(1)
for id1 in range(numV):
    for id2 in range(id1+1,numV):
        for id3 in range(id2+1,numV):
            if IDX[id1] == IDX[id2] and IDX[id2] == IDX[id3]:
                value = random()
                if value < p_intra:
                    if offset >= alloc:
                        edges = np.append(edges,np.zeros((3,alloc)),1)
                        alloc = alloc * 2
                    edges[0,offset] = id1
                    edges[1,offset] = id2
                    edges[2,offset] = id3
                    offset = offset + 1
            else:
                value = random()
                if value < p_inter:
                    if offset >= alloc:
                        edges = np.append(edges,np.zeros((3,alloc)),1)
                        alloc = alloc * 2
                edges[0,offset] = id1
                edges[1,offset] = id2
                edges[2,offset] = id3
                offset = offset + 1
edges = edges[:, 1: offset]


A = np.zeros((numV,numV))
numE = len(edges[1])
for eid in range(numE):
    V1id = int(edges[0,eid])
    V2id = int(edges[1,eid])
    V3id = int(edges[2,eid])

    A[V1id,V2id] += 1
    A[V2id,V1id] = A[V2id,V1id] + 1
    A[V2id,V3id] = A[V2id,V3id] + 1
    A[V3id,V2id] = A[V3id,V2id] + 1
    A[V1id,V3id] = A[V1id,V3id] + 1
    A[V3id,V1id] = A[V3id,V1id] + 1

D = np.zeros((len(A),len(A)))

deg = np.sum(A,axis=0)

for j in range(len(A)):
    D[j,j] = deg[j]

L = D - A

w, v = np.linalg.eig(L)
u = v[:,1]

from sklearn.cluster import KMeans
vec = u.reshape(-1,1)
kmeans = KMeans(n_clusters=2, random_state=0).fit(vec)
kmeans.labels_

