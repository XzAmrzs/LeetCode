# coding=utf-8
# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given two binary trees, write a function to check if they are equal or not.
#
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
#


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 二叉树的处理一般都涉及到递归处理，想清楚最后一个结点该返回什么值即可
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        # 涉及到python的值是否相等，严谨的来说必须要用==
        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    p = TreeNode(68)
    p.left = TreeNode(41)
    p.left.left = TreeNode(-85)
    p.left.left.left = TreeNode(-73)
    p.left.left.right = TreeNode(-49)
    p.left.left.left.left = TreeNode(-98)
    p.left.left.left.left.left = TreeNode(-124)

    q = TreeNode(68)
    q.left = TreeNode(41)
    q.left.left = TreeNode(-85)
    q.left.left.left = TreeNode(-73)
    q.left.left.right = TreeNode(-49)
    q.left.left.left.left = TreeNode(-98)
    q.left.left.left.left.left = TreeNode(-124)
    print solution.isSameTree(p, q)

# [68,41,null,-85,null,-73,-49,-98,null,null,null,-124]
# [68,41,null,-85,null,-73,-49,-98,null,null,null,-124]