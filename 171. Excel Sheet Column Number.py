# Given a column title as appear in an Excel sheet
# return its corresponding column number

# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
from math import sqrt


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = 0
        for i,j in enumerate(s[::-1]):
            a = a +(ord(j)-64)*(26**i)
        return a

if __name__ == '__main__':
    solution = Solution()
    print solution.titleToNumber('AB')