# coding=utf-8

# Write a function that takes an unsigned integer and returns the number of ’1' bits it has
# (also known as the Hamming weight).
# For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011,
# so the function should return 3.


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 模拟十进制转二进制，余数相加就是1的个数啊！
        i = 0
        while n != 0:
            i += n % 2
            n /= 2
        return i


if __name__ == '__main__':
    print Solution().hammingWeight(11)
