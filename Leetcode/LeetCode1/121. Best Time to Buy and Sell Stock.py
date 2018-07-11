# @Time   :2018/6/29
# @Author :LiuYinxing
# 解题思路 遍历数组


class Solution:
    def maxProfit(self, prices):

        minprice, maxprofit, n = float('inf'), 0, len(prices)
        for i in range(n):
            if prices[i] < minprice:
                minprice = prices[i]  # 更新最小值
            elif prices[i] - minprice > maxprofit:  # 与当前的最优值比较，如果比之前更优，则更新
                maxprofit = prices[i] - minprice
        return maxprofit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    solu = Solution()
    print(solu.maxProfit(prices))
