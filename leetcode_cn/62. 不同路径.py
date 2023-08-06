class Solution(object):
    def uniquePaths(self, m: int, n: int) -> int:

        if m == 1:return 1
        if n == 1:return 1

        dp = [[0] * n for _ in range(m)]

        for i in range(n):
            dp[0][i] = 1
        for j in range(m):
            dp[j][0] = 1

        for j in range(1, n):
            for i in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]


if __name__ == '__main__':

    solu = Solution()
    m, n = 3, 7
    m, n = 3, 3

    out = solu.uniquePaths(m, n)
    print(out)