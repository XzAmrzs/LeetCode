# coding=utf-8
# Given an integer, write a function to determine if it is a power of two.
# 如何判断一个数是2的幂，主要是要找出2的幂次方的数的特点。(就相当于判断是不是一个10进制数一样，如果是判断是不是10进制的话那么那就)
# 我们知道，1个数乘以2就是将该数左移1位，而2的0次幂为1，
# 所以2的n次幂（就是2的0次幂n次乘以2）就是将1左移n位，
# 这样我们知道如果一个数n是2的幂，则其只有首位为1，
# 其后若干个0，必然有n & (n - 1)为0。
# (在求1个数的二进制表示中1的个数的时候说过，n&(n-1)去掉n的最后一个1)
# 因此，判断一个数n是否为2的幂，只需要判断n&(n-1)是否为0即可

# 如果一个数是2的阶次方数，那么它的二进制数的首位一般是1，后面接若干位0。比如8就是1000，64是1000000。如果将这个数减1再与该数做&运算，则应该全部位都是0。所以如果一个数d，满足d&(d-1)==0，则这个数必定是可以被2的幂整除的数。

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 不是正数就返回False
        # 是正数就判断是不是2的幂
        if n <= 0:
            return False        return (n & (n - 1)) == 0


if __name__ == "__main__":
    print Solution().isPowerOfTwo(6)
