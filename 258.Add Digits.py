class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            abc = 0
            while num != 0:
                abc = abc + num % 10
                num = num / 10
            num = abc
        return num


if __name__ == '__main__':
    solution = Solution()
    print solution.addDigits(3888)
