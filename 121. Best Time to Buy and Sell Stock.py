# coding=utf-8
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.


class Solution(object):
    # 遍历价格 存放之前的一个最小价格和最大利润。当前价格-之前的最小价格就是利润
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # max_profit记录当前最大利润
        # min_price记录当前最小价格，初值是正无穷
        max_profit, min_price = 0, float("inf")
        for price in prices:
            # 取得当前最小价格
            min_price = min(min_price, price)
            # 取得当前最大利润
            max_profit = max(max_profit, price - min_price)
        return max_profit

    def timeExceedMaxProfit(self, prices):
        compares = float("-inf")
        for i, j in enumerate(prices):
            max_price = float("-inf")
            for b in prices[i + 1:]:
                current = b - j
                if max_price < current:
                    max_price = current
            if compares < max_price:
                compares = max_price
        return 0 if compares < 0 else compares


if __name__ == '__main__':
    a = [6, 3, 7]
    print Solution().maxProfit(a)
