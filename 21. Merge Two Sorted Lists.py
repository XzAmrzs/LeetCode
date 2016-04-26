# coding=utf-8
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
#
# Subscribe to see which companies asked this question

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


# 归并排序
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # 定义一个head放到list1之前

        l3 = ListNode(None)
        t3 = l3
        while l1 or l2:
            if l1 is None:
                t3.next = l2
                l2 = l2.next
            elif l2 is None:
                t3.next = l1
                l1 = l1.next
            elif l1.val <= l2.val:
                t3.next = l1
                l1 = l1.next
            else:
                t3.next = l2
                l2 = l2.next
            t3 = t3.next

        # 对于每一个list2中的元素判断是否比l1.val的值小

        return l3.next


if __name__ == '__main__':
    a = map(ListNode, [1, 3, 5])
    b = map(ListNode, [2, 4, 6])
    for i in range(len(a) - 1):
        a[i].next = a[i + 1]
    for i in range(len(a) - 1):
        b[i].next = b[i + 1]
    print Solution().mergeTwoLists(a[0], b[0])
