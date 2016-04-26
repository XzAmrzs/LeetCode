# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        root.left, root.right = root.right, root.left
        if root.left is not None:
            self.invertTree(root.left)
        if root.right is not None:
            self.invertTree(root.right)
        return root



if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right= TreeNode(3)
    root.right.left= TreeNode(7)
    root.right.right=TreeNode(9)
    print root.left.val
    print root.right.val
    print root.left.left.val
    root = Solution().invertTree(root)
    print root.left.val
    print root.right.val
    print root.left.left.val
