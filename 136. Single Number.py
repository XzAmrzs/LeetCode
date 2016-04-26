# coding=utf-8
# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# operator 操作符函数库
import operator


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 中心思想:按位异或同一个值两次(偶数次)，其值不会发生变化
        return reduce(operator.xor, nums)


if __name__ == "__main__":
    nums = [1, 5, 1, 2, 3, 2, 3]
    print Solution().singleNumber(nums)
