# coding=utf-8
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security system connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 有点类似爬梯子的题目70.climbing stairs
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        # 取出第一个数和下一个相比当中的最大值以及第一个数,处理只有两个数的情况
        num_max, num_i_1 = max(nums[0], nums[1]), nums[0]

        for i in xrange(2, len(nums)):
            num_i_2 = num_i_1
            num_i_1 = num_max
            # 用当前的数+不报警的最近的数 与 之前的最大值相比
            # 较大者用来更新成为新的最大值
            num_max = max(nums[i] + num_i_2, num_max)

        return num_max


if __name__ == '__main__':
    a = [1, 2, 3, 1]
    print Solution().rob(a)
