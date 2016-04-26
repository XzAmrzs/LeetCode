class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 == 0:
            return False
        else:
            return True


if __name__ == '__main__':
    solution = Solution()
    print solution.canWinNim(8)
