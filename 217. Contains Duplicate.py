# Given an array of integers,
# find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        a=set()
        for i in nums:
            if i not in a:
                a.add(i)
            else:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    nums = [0]

    print solution.containsDuplicate(nums)
