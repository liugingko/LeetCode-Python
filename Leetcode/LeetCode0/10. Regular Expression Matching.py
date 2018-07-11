import re

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        n, m = len(s), len(p)
        dp = [[False]*(m+1) for _ in range(n+1)]
        dp[0][0] = True
        # 初始化第0行,除了[0][0]全为false，毋庸置疑，因为空串p只能匹配空串，其他都无能匹配
        for j in range(1, m+1): dp[0][j] = False

        # 初始化第0列，只有X*能匹配空串，如果有*，它的真值一定和p[0][i-2]的相同（略过它之前的符号）
        for i in range(1, n+1): dp[i][0] = (i>1) and (p[i-1] == '*') and (dp[i-2][0])

        for i in range(1, n+1):
            for j in range(1,m+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j - 2] or ((s[i - 1] == p[j - 2]) or (p[j - 2] == '.')) and dp[i - 1][j]
                else:
                    dp[i][j] = (p[j - 1] == '.' or s[i - 1] == p[j - 1]) and dp[i - 1][j - 1]
        return dp[n][m]


    def isMatch1(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]



if __name__ == '__main__':
    s = Solution()
    out = s.isMatch1("aa", "a*")
    print(out)
