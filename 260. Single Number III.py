# coding=utf-8
# Given an array of numbers nums,
# in which exactly two elements appear only once and all the other elements appear exactly twice.
# Find the two elements that appear only once.
#
# For example:
#
# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
#
# Note:
#
#   The order of the result is not important. So in the above example, [5, 3] is also correct.
#   Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

# operator 操作符函数库
import operator


# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         中心思想:按位异或同一个值两次(偶数次)，其值不会发生变化
        # return reduce(operator.xor, nums)


class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        # 所有数的异或
        x_xor_y = reduce(operator.xor, nums)
        #
        bit =  x_xor_y & -x_xor_y
        result = [0, 0]
        for i in nums:
            result[bool(i & bit)] ^= i
        return result

class Solution2:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        x_xor_y = 0
        for i in nums:
            x_xor_y ^= i

        bit = x_xor_y & ~(x_xor_y - 1)

        x = 0
        for i in nums:
            if i & bit:
                x ^= i

        return [x, x ^ x_xor_y]

if __name__ == "__main__":
    nums = [3, 5]
    print Solution().singleNumber(nums)
