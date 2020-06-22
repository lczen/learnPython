"""
输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的无向图为:
  1
 / \
2 - 3
"""

class Solution:
    def findRedundantConnection(self, edges):
        #用并查集，进来一对边，就查找两个结点的根结点，如果是一样的，那就不能要这对边，否则就增加这对边
        pre  = [0] * 1001 # 初始化所有的节点为单独的根节点
        for edge in edges:
            x = self.find(edge[0], pre)
            y = self.find(edge[1], pre)
            if x != y:
                pre[y] = x
            else:
                return edge

    def find(self, node, pre):
        while pre[node] != 0:
            node = pre[node]
        return node

print(Solution().findRedundantConnection([[1,2], [1,3], [2,3]]))

#冗余连接还是比较简单的。其实就是根据edge两头找祖先节点。如果祖先相同肯定不行。