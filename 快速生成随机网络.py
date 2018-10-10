
import networkx as nx
import matplotlib.pyplot as plt

# 快速生成随机网络
G = nx.fast_gnp_random_graph(500, 0.01)
nx.draw_networkx(G)
plt.show(G)