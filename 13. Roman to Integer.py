# coding=utf-8
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
                }
        sum = 0
        # 循环一遍，如果前边的那个罗马数字比这个数字小就做相应的处理
        for i, j in enumerate(s):
            if i == 0:
                sum = temp[j] + sum
            elif temp[j] > temp[s[i - 1]]:
                    sum = sum + temp[j] - 2*temp[s[i - 1]]
            else:
                sum = sum + temp[j]
        return sum


if __name__ == '__main__':
    s = 'VIV'
    print Solution().romanToInt(s)
