class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        if m == 0:return n
        if n == 0:return m
        dp = [[0]*(n+1) for _ in range(m+1)]  # 初始化dp和边界
        for i in range(1, m+1): dp[i][0] = i
        for j in range(1, n+1): dp[0][j] = j
        for i in range(1, m+1):  # 计算dp
            for j in range(1, n+1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i][j - 1] + 1, dp[i - 1][j] + 1)
        return dp[m][n]
    def minDistance1(self, word1, word2):
        m, n = len(word1), len(word2)
        if m == 0: return n
        if n == 0: return m
        cur = [0] * (m + 1)  # 初始化cur和边界
        for i in range(1, m+1): cur[i] = i

        for j in range(1, n+1):  # 计算cur
            pre, cur[0] = cur[0], j  # 初始化当前列的第一个值
            for i in range(1, m+1):
                temp = cur[i]  # 取出当前方格的左边的值
                if word1[i - 1] == word2[j - 1]:
                    cur[i] = pre
                else:
                    cur[i] = min(pre + 1, cur[i] + 1, cur[i - 1] + 1)
                pre = temp
        return cur[m]

if __name__ == '__main__':
    solu = Solution()
    word1, word2 = 'horse', 'ros'
    print(solu.minDistance(word1, word2))