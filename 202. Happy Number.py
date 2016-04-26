# coding=utf-8
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
#
#     12 + 92 = 82
#     82 + 22 = 68
#     62 + 82 = 100
#     12 + 02 + 02 = 1
import math


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 如果这个数是1直接返回
        # 求出这个数每位上的值
        # 将每位的值求平方然后相加求和
        # 如果和为之前出现过的数字返回False
        # 循环上面步骤一直到和为1返回true
        if n == 1:
            return True
        result = n
        temp = set()
        while result != 1:
            n, result = result, 0
            while n != 0:
                result += (n % 10) ** 2
                n /= 10
            if result not in temp:
                temp.add(result)
            else:
                return False
        return True


if __name__ == '__main__':
    a = 19
    print Solution().isHappy(2)
