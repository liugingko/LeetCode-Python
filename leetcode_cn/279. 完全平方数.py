class Solution:
    def numSquares(self, n: int) -> int:

        f = [0] * (n + 1);
        for i in range(1, n+1):
            minn = float('inf')
            for j in range(1, i+1):
                tmp = j*j
                if tmp <= i:
                    minn = min(minn, f[i - tmp])
            f[i] = minn + 1
        return f[n]

    def numSquares(self, n: int) -> int:

        dp = [0] * (n + 1);
        for i in range(1, n+1):
            dp[i] = i
            for j in range(1, i+1):
                tmp = j*j
                if tmp <= i:
                    dp[i] = min(dp[i], dp[i - tmp] +1)

        return dp[n]


if __name__ == '__main__':
    solu = Solution()
    print(solu.numSquares(1))