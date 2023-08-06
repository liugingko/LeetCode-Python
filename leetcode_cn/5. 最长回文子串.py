import numpy as np
'''
5. Longest Palindromic Substring
最长字符串，回文
马拉车算法 动态规划， 中心扩散法
'''

class Solution:
    # Manacher algorithm
    # http://en.wikipedia.org/wiki/Longest_palindromic_substring

    def dplongestPalindrome(self, s):

        if len(s) == 1: return s

        n = len(s)

        dp = [[0]*n for _ in range(n)]
        start, end, maxlen = 0, 0, 0
        for j in range(n):
            for i in range(j):
                dp[i][j] = s[i]==s[j] and ((j-i < 2) or dp[i+1][j-1])
                if dp[i][j] and j - i + 1 > maxlen:
                    start, end, maxlen = i, j, j-i +1
            dp[j][j]=1

        return s[start:end+1]

if __name__ == '__main__':

    solu = Solution()
    s = "babad"
    s1 = "abccba"

    out = solu.dplongestPalindrome(s1)
    print(out)
