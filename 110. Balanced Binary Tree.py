# coding=utf-8
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which
# the depth of the two subtrees of every node never differ by more than 1.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return (self.getHeight(root) >= 0)

    # 每个节点的深度=MAX(左结点的深度+右结点的深度)+1
    # 一旦一个结点出现负数，那么肯定是是已经不平衡了，所以三个判断条件
    def getHeight(self, root):
        if root is None:
            return 0
        left_height, right_height = self.getHeight(root.left), self.getHeight(root.right)
        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
