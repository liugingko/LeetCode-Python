# @Time   :2022/1/28
# @Author :lyx


class Solution:
    def isSubsequence1(self, s, t):
        n = len(s)
        m = len(t)
        if n == 0: return True
        if m == 0: return False
        dp = [[False] * m for _ in range(n)]  # 初始化dp
        dp[0][0] = s[0] == t[0]
        for i in range(n):
            for j in range(1, m):
                if i == 0:
                    dp[i][j] = dp[i][j-1] or (s[i] == t[j])
                else:
                    dp[i][j] = dp[i][j-1] or (dp[i-1][j] and s[i]==t[j])
        print(dp)
        return dp[n-1][m-1]

    def isSubsequence(self, s, t):
        n = len(s)
        m = len(t)
        if n == 0: return True
        if m == 0: return False
        i = 0
        for j in range(m):
            if i < n and s[i] == t[j]:
                i += 1

        return i == n


if __name__ == '__main__':
    solu = Solution()
    s = "abc"
    t = "ahbgdc"
    s = "aaaaaa"
    t = "bbaaaa"
    print(solu.isSubsequence(s, t))