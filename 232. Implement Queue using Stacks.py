# coding=utf-8
#  Implement the following operations of a queue using stacks.
#
#     push(x) -- Push element x to the back of queue.
#     pop() -- Removes the element from in front of queue.
#     peek() -- Get the front element.
#     empty() -- Return whether the queue is empty.
#
# Notes:
#
# You must use only standard operations of a stack --
# which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively.
# You may simulate a stack by using a list or deque (double-ended queue),
# as long as you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue)

# 核心思想：使用两个栈从而颠倒放入的顺序就可以了
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A, self.B = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.A.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.peek()
        self.B.pop()

    def peek(self):
        """
        :rtype: int
        """
        # 防止正在转化的时候调用了其他函数，所以保证这个B是空的时候才进行转换
        if not self.B:
            # 可以直接对这个A这个列表进行判断，如果列表为空，那么python会自动判定他的布尔值为False
            while self.A:
                self.B.append(self.A.pop())
        return self.B[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.A and not self.B


if __name__ == '__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    print q.peek()
    q.push(4)
    q.pop()
    print q.peek()


