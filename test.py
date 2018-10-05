from __future__ import print_function
from networkx import read_edgelist
import networkx as nx

G = read_edgelist('hartford_drug.edgelist')
print(G.number_of_nodes())
print(G.number_of_edges())

import matplotlib.pyplot as plt
nx.draw(G)
plt.show()

# 寻找社区/联通子图
from networkx.algorithms import number_connected_components, connected_components

print(number_connected_components(G))
for subG in connected_components(G):
    print(subG)

# 获取联通子图的图结构
from networkx.algorithms import connected_component_subgraphs

for i, subG in enumerate(connected_component_subgraphs(G)):
    print('G%s' % i, subG.number_of_nodes(), subG.number_of_edges())

# 通过三角计算强化社区发现
# 三角计数(triangles counts)和集束系数/聚类系数（clustering coefficient）衡量社区/子图的紧密程度
from networkx.algorithms import triangles, transitivity, average_clustering

# 三角计数
print(triangles(G))
# 平均三角计数
print(transitivity(G))
# 平均集束系数
print(average_clustering((G)))

# 利用pagerank发现影响力中心
from collections import Counter
from networkx.algorithms import pagerank

pr = pagerank(G)
for p in Counter(pr).most_common():
    print(p)