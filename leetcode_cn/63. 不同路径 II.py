class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:

        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]  # 初始化dp

        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 0:
                    if i + 1 < n:  # 更新下面的方格
                        dp[i + 1][j] += dp[i][j]
                    if j + 1 < m:  # 更新右边的方格
                        dp[i][j + 1] += dp[i][j]
                else:  # 如果有障碍物，则标记为0
                    dp[i][j] = 0
        return dp[n - 1][m - 1]



if __name__ == '__main__':

    solu = Solution()

    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    out = solu.uniquePathsWithObstacles(obstacleGrid)
    print(out)