# coding=utf-8
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: in
        """
        nums.sort()
        return nums[len(nums)/2]


if __name__ == '__main__':
    a= [3,2,3]
    print Solution().majorityElement(a)
