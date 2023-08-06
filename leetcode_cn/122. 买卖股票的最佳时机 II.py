# @Time   :2018/6/29
# @Author :LiuYinxing
# 解题思路 类似于贪心


class Solution:
    def maxProfit(self, prices):

        n, maxprofit = len(prices), 0
        for i in range(1, n):
            tmp = prices[i] - prices[i-1]
            if tmp > 0:
                maxprofit += tmp
        return maxprofit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    solu = Solution()
    print(solu.maxProfit(prices))