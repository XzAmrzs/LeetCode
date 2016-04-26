# coding=utf-8
#  Given an integer, write a function to determine if it is a power of three.
#
# Follow up:
# Could you do it without using any loop / recursion?

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 不是正数就返回False
        if n <= 0:
            return False
        # 判断是否是3的幂:
        # 采用不断相除的方法
        a = 1
        while True:
            if a > n:
                return False
            if a == n:
                return True
            a *= 3
if __name__ == "__main__":
    for i in range(30):
        print i
        print Solution().isPowerOfThree(i)
