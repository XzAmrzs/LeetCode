# coding=utf-8
#  Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


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


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        first_head = ListNode(float("-inf"))
        first_head.next = head
        c = first_head
        while c.next:
            a = c
            b = c.next.next
            # 处理奇数情况
            if b is None:
                break
            a.next.next = b.next
            b.next = a.next
            a.next = b
            c = b.next
        return first_head.next


# 程序尚未对当给定的链表个数是奇数的时候做处理
if __name__ == '__main__':
    a = map(ListNode, [1, 3, 5, 1])
    for i in range(len(a) - 1):
        a[i].next = a[i + 1]
    print Solution().swapPairs(a[0])
