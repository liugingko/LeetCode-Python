class Solution:
    def maxProfit(self, k, prices):
        n, res = len(prices), 0
        if n < 2: return 0
        if k > n //2:  # 现在这个情况，就相当于题目2
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    res += prices[i] - prices[i-1]
            return res

        hold, sold = [float('-inf')] * (k + 1), [0] * (k + 1)
        for price in prices:
            for j in range(1, k+1):
                hold[j] = max(hold[j], sold[j-1]-price)  # hold->hold, sold->hold
                sold[j] = max(sold[j], hold[j]+price)  # sold->sold, hold->sold
        return sold[k]


if __name__ == '__main__':
    prices, k = [7, 1, 5, 3, 6, 4], 4
    solu = Solution()
    print(solu.maxProfit(k, prices))