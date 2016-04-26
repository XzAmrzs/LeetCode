# coding=utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 核心思想:将Node的值自该结点开始全部前移一位，然后删除最后一个Node就达到了删除一个结点得到目的
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None:  # 如果这个结点本身就是空，那么返回
            return
        node.val = node.next.val  # 那么把下一个结点的值前移
        if node.next.next is None:  # 如果这个结点的下下一个是空，那么说明下一个结点是最后一个结点，
            node.next = None        # 通过把下一个结点赋空来达到删除最后一个结点的目的
        self.deleteNode(node.next)  # 对下一个结点也这么处理，直到处理到倒数第二个结点的时候，参数变为None,直接返回
        return


if __name__ == '__main__':
    solution = Solution()
    L0 = ListNode(0)
    L1 = ListNode(1)
    L2 = ListNode(3)
    L3 = ListNode(4)
    L4 = ListNode(5)
    L0.next = L1
    L1.next = L2
    L2.next = L3
    L3.next = L4
    solution.deleteNode(L0)
    print L0.val
    print L0.next.val
    print L0.next.next.val
    print L0.next.next.next.val
