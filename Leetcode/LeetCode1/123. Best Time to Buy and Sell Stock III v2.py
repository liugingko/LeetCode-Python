# @Time   :2018/7/2
# @Author :LiuYinxing
# 解题思路  区间dp


class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n < 2: return 0

        dp1, dp2 = [0] * n, [0] * n  # 初始化dp
        minprice, maxprice, result = prices[0], prices[n - 1], 0

        for i in range(1, n):  # 正向，第一个区间的最优值
            minprice = min(minprice, prices[i])
            dp1[i] = max(dp1[i-1], prices[i]-minprice)

        for i in range(n-2, -1, -1):  # 逆向，第二个区间的最优值
            maxprice = max(maxprice, prices[i])
            dp2[i] = max(dp2[i + 1], maxprice - prices[i])

        for v1, v2 in zip(dp1, dp2):  # 获取最优值
            result = max(result, v1+v2)
        return result


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    solu = Solution()
    print(solu.maxProfit(prices))