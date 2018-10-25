
import networkx as nx
import matplotlib.pyplot as plt

g = nx.read_edgelist('facebook_combined.txt', create_using=nx.Graph())

print('网络节点个数：', g.number_of_nodes())
print('网络连边个数：', g.number_of_edges())

#print(g.edges())

# 可视化图
#nx.draw(g, node_size=30, with_labels=True)
#plt.show()

# 返回节点
print('节点列表：', g.nodes())
#print('边列表：', g.edges())
# 返回节点‘1’的度
print('节点‘1’的度：', g.degree('1'))
# 返回所有节点的度
print('所有节点的度：', g.degree())


# 节点度的频率分布直方图
# 返回网络中所有节点的度分布序列（从1至最大度的出现频次）
print('节点度的分布序列：', nx.degree_histogram(g))
degree_f = nx.degree_histogram(g)
# 生成x轴，从1到最大度
x = range(len(degree_f))
# 将频次转化为频率
y = [z / float(sum(degree_f)) for z in degree_f]
# 柱状图
plt.bar(x, degree_f)
# 调用plt.hist画直方图
#plt.hist(degree_f, 50)
#plt.plot(x,degree_f)
plt.show()

# 画出节点度大于n的网络
g_copy = g.copy()
dn = g_copy.degree()
for i in g.nodes():
    #print(dn[i])
    if dn[i] < 150:
        g_copy.remove_node(i)

print('筛选后网络节点个数：', g_copy.number_of_nodes())
print('筛选后网络连边个数：', g_copy.number_of_edges())
# 节点是否带标签 with_labels=True, 布局 pos=nx.spring_layout(g_copy)
# 随机布局
#nx.draw(g_copy, node_size=10, edge_color='b', alpha=0.2, pos=nx.random_layout(g_copy))
# 默认布局
#nx.draw(g, node_size=10, alpha=0.2)
#nx.draw(g, node_size=10, edge_color='b', alpha=0.2, pos=nx.random_layout(g))
#plt.savefig('facebook_spring_layout.png')
#plt.show()

# 计算网络特征系数
# 群聚/聚集系数：较高的聚集系数出现在网络中高连通性的区域，较低的聚集系数出现在网络中低连通性的区域，即节点聚集在一起的程度
#print('节点聚集系数：', nx.clustering(g))
#print('平均聚集系数：', nx.average_clustering(g))

# 中心性
# 中介中心性（Betweenness centrality）：中介中心性高的节点是网络的核心组成部分，介数节点，联通网络的门户
#print('中介中心性：', nx.betweenness_centrality(g))

# 度中心性（degree centrality）：与本节点有直接联系的节点占其余节点总数的百分比，连接数量越多，节点度中心性越高
#print('度中心性：', nx.degree_centrality(g))

# 接近中心性（closeness centrality）：节点与其他节点之间的接近/距离程度，接近中心性高的节点位于网络中心的节点，只需几次跳跃就可以到达其他节点
#print('接近中心性：', nx.closeness_centrality(g))

# 特征向量中心性（Eigenvector centrality）：图作为一个马尔科夫链，表示访问一个节点的静态分布概率，pagerank
#print('特征向量中心性：', nx.eigenvector_centrality(g))

import community

# 将网络划分为多个网络
part = community.best_partition(g)
print(part)

#计算模块度
mod = community.modularity(part,g)
print(mod)

#绘图
#values = [part.get(node) for node in g.nodes()]
#nx.draw_spring(g, cmap=plt.get_cmap('jet'), node_color = values, node_size=10, with_labels=False)
#plt.show()


# pagerank发现影响力中心
pr = nx.algorithms.pagerank(g)

print(pr)

# 两种排序方法
print(sorted(pr.items(), key=lambda item: item[1], reverse=True))
from collections import Counter

print('排序', Counter(pr).most_common(10))

# 取前几个关键节点
key_node = [n[0] for n in Counter(pr).most_common(10)]
print(key_node)

# 在图中绘制关键节点
plt.figure()
plt.subplot(1, 2, 1)
pos = nx.spring_layout(g)
nx.draw_networkx_nodes(g, pos, nodelist=key_node, node_size=30)
nx.draw_networkx_edges(g, pos, alpha=0.2)


plt.subplot(1, 2, 2)
nx.draw(g, pos, node_size=8)


plt.show()



