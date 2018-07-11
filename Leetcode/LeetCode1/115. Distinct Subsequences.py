# @Time   :2018/6/24
# @Author :LiuYinxing
# 解题思路 动态规划


class Solution:
    def numDistinct(self, s, t):

        m, n = len(s)+1, len(t)+1
        dp = [[1]*m for _ in range(n)]  # 初始化dp
        for i in range(1, n): dp[i][0] = 0

        for i in range(1, n):  # 开始计算
            for j in range(1, m):
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]*(t[i-1] == s[j-1])
        return dp[-1][-1]

    def numDistinct1(self, s, t):

        m, n = len(s)+1, len(t)+1
        dp = [0] * n  # 初始化dp
        dp[0] = 1

        for j in range(1, m):
            pre = dp[:]  # pre 表示前一列的值
            for i in range(1, n):
                dp[i] = pre[i] + pre[i - 1] * (t[i - 1] == s[j - 1])
        return dp[-1]


if __name__ == '__main__':
    S, T = 'babgbag', 'bag'
    solu = Solution()
    print(solu.numDistinct1(S, T))