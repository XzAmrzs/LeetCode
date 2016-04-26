# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        a = [1, 2]
        for i in range(2, n):
            a.append(a[i - 2] + a[i - 1])
        return a.pop()


if __name__ == '__main__':
    n = 4
    print Solution().climbStairs(n)
