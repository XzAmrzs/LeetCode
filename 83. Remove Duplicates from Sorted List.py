# coding=utf-8
#  Given a sorted linked list,
#  delete all duplicates such that each element appear only once.
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = head
        while dummy:
            # 把dummy的下一个节点赋值给runner
            runner = dummy.next
            # 当runner存在并且和dummy的值一样的时候说明list的下一个元素和这个重复了
            # 循环删除直到这个值不出现重复
            while runner and runner.val == dummy.val:
                runner = runner.next
            # 把没有当前元素重复的runner链赋给dummy的下一个元素
            dummy.next = runner
            # 把当前元素赋值给dummy
            dummy = runner
        return head


if __name__ == '__main__':
    a = map(ListNode, [1, 1, 1])
    for i in range(2):
        a[i].next = a[i + 1]
    print Solution().deleteDuplicates(a[0])
