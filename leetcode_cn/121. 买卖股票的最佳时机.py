# @Time   :2023/05/14
# @Author :LiuYinxing
# 解题思路 遍历数组


class Solution:
    def maxProfit(self, prices):

        minprice, maxprofit, n = float('inf'), 0, len(prices)
        for item in prices:
            if item < minprice:
                minprice = item
            elif item - minprice > maxprofit:
                maxprofit = item - minprice
        return maxprofit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    solu = Solution()
    print(solu.maxProfit(prices))