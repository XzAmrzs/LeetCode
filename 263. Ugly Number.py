# coding=utf-8
#  Write a program to check whether a given number is an ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
#
# Note that 1 is typically treated as an ugly number.
from math import sqrt


class Solution(object):

    def memory_error_ugly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 能这么想问题的我真是个傻逼
        if num == 1:
            return True
        if num <= 0:
            return False
        a = [2, 3, 5]
        # 找出所有的因数
        for i in range(2, num + 1):
            if num % i == 0:
                # 对每个找到的因数判断是否是质数
                if self.isPrime(i) and i not in a:
                    # 若这个质因数是2,3,5以外的数
                    return False
                else:
                    continue
        return True

    # 思考问题的时候要有正反面，与其找到所有的质数不如直接用要求的数来判断能不能组成它！
    def isUgly(self, num):
        if num == 0:
            return False
        # 遍历2,3,5作为除数，最后得1即这是组成它的所有质数
        for i in [2, 3, 5]:
            # 将num能被2整除的部分都除完
            while num % i == 0:
                num /= i
        return num == 1

    def isPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


if __name__ == '__main__':
    print Solution().isUgly(214797179)
