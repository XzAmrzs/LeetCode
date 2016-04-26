# coding=utf-8
# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
#
# Example:
# For num = 5 you should return [0,1,1,2,1,2].
#
# Follow up:
#
# It is very easy to come up with a solution with run time O(n*sizeof(integer)).
# But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss?
# Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # 位运算>>二进制右移操作符
        # 可以使用(i&1)来判断奇偶性a
        a = [0]
        for i in xrange(1, num + 1):
            a.append((i & 1) + a[i >> 1])
        return a


if __name__ == '__main__':
    # print Solution().countBits(1)
    print Solution().countBits(16) == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1]

