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

# 没有详细考虑到算法的情况，无法处理两个链表的最后一个点
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
        list_1 = ListNode(float("-inf"))
        list_1.next = l1
        list_2 = l2
        # current=head.next(list[0])
        current_1 = list_1
        current_2 = list_2
        # 对于每一个list2中的元素判断是否比current_1.val的值小
        while current_2:
            while current_1:
                if current_2.val < current_1.next.val:
                    # 如果小那么就把这个元素插入到current_1之前
                    list_2 = list_2.next
                    current_2.next = current_1.next
                    current_1.next = current_2
                    current_1 = current_2
                    break
                else:
                    # 如果大那么就遍历list1的下一个元素list1[1]
                    # 一直到找到比它小的元素或者遍历完list1
                    current_1 = current_1.next
            current_2 = list_2

        # 然后list2的下一个元素再次与current.val做比较
        # 最后返回list1.next
        return list_1.next


if __name__ == '__main__':
    a = map(ListNode, [1, 3, 5])
    b = map(ListNode, [2, 4, 6])
    for i in range(len(a) - 1):
        a[i].next = a[i + 1]
    for i in range(len(a) - 1):
        b[i].next = b[i + 1]
    print Solution().mergeTwoLists(a[0], b[0])
