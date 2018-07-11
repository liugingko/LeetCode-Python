class Solution:
    def maxProfit1(self, prices):

        if len(prices) < 2: return 0

        c1, c2, h1, h2 = 0, 0, -prices[0], -prices[0]
        for p in prices[1:]:
            # c1, c2, h1, h2=max(c1,h1+p), max(c2,h2+p), max(h1,-p), max(h2,c1-p)
            c1 = max(c1, h1+p)
            c2 = max(c2, h2+p)
            h1 = max(h1, -p)
            h2 = max(h2, c1-p)
        return max(c1, c2)
    def maxProfit(self, prices):
        if len(prices) == 2: return 0
        buy1, buy2, sell1, sell2 = -prices[0], -prices[0], 0, 0
        for p in prices:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, buy1 + p)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, buy2 + p)
            print(p,':',buy1, sell1, buy2, sell2)
        return sell2

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    prices = [1, 2, 3, 5, 2, 4, 5, 6, 7]
    print(prices)
    solu = Solution()
    print(solu.maxProfit(prices))