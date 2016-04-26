# coding=utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        if self:
            return "{} : <{},{}>".format(self.val, repr(self.left.val, self.right.val))


global temp
temp = None


class Solution(object):
    # def __init__(self):
    #     self.temp = None
    def __init__(self):
        # 存储所有叶子节点
        self.temp = None
        self.temps = []
        # 存储两结点到LCA之间的距离
        self.length = 0

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.tools(root, p, q)
        return self.temp

    # 工具函数
    def tools(self, root, p, q):
        # 定义一个临时的标记量
        summer = 0
        # 如果root是空那么直接返回
        if root is None:
            return 0
        # 如果root是其中一个结点，那么summer+1
        if (root is p) or (root is q):
            summer += 1
        # summer加上这个结点的左子树的遍历到p或者q的长度
        summer += self.tools(root.left, p, q)
        # summer加上这个结点的右子树的遍历到p或者q的长度
        summer += self.tools(root.right, p, q)
        # 如果summer == 2 那么说明这个结点的子结点找到了p和q
        # 那么把这个结点给全局变量temp
        if summer == 2:
            self.temp = root
            # 让summer+1 避免更高的祖先结点赋值
            summer += 1
        return summer

    def getNodes(self, root):

        if (root.left is None) and (root.right is None):
            self.temps.append(root)
        if root.left:
            self.getNodes(root.left)
        if root.right:
            self.getNodes(root.right)
        return self.temps

    def getLength(self, root, p, q):
        if root is None:
            return 0
        if (root is p) or (root is q):
            self.length += 1
        self.length + self.getLength(root.left, p, q)
        self.length + self.getLength(root.right, p, q)
        return self.length


if __name__ == '__main__':
    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(4)
    root.left = a
    root.right = b
    a.right = c
    print Solution().getLength(root, a, c)
    # print Solution().lowestCommonAncestor(root, a, c).val

    # nodes = Solution().getNodes(root)
    # for i in nodes:
    #     for j in nodes:
    #         # 获得所有两结点到其LCA的距离
    #         Solution().lowestCommonAncestor(root, a, c)


    # class Solution:
    #     # @param {TreeNode} root
    #     # @param {TreeNode} p
    #     # @param {TreeNode} q
    #     # @return {TreeNode}
    #     def lowestCommonAncestor(self, root, p, q):
    #         if root in (None, p, q):
    #             return root
    #
    #         left, right = [self.lowestCommonAncestor(child, p, q) for child in (root.left, root.right)]
    #         # 1. If the current subtree contains both p and q,
    #         #    return their LCA.
    #         # 2. If only one of them is in that subtree,
    #         #    return that one of them.
    #         # 3. If neither of them is in that subtree,
    #         #    return the node of that subtree.
    #         return root if left and right else left or right
