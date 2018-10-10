
import networkx as nx
import matplotlib.pyplot as plt

# 快速生成随机网络
# 建立一个具有500个节点，连接概率是1%的随机网络
G = nx.fast_gnp_random_graph(500, 0.01)
nx.draw_networkx(G)
plt.show(G)