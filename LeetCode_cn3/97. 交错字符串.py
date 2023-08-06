# @Time   :2019/02/05
# @Author :LiuYinxing
# 动态规划


class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != len(s1) + len(s2):
            return False

        dp = [[None] * (len(s2) + 1) for _ in range(len(s1)+1)]  # 初始化dp

        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:  # 计算上边界
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:  # 计算下边界
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                else:  # 从两个方向向左下角计算
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1][-1]


if __name__ == '__main__':
    solu = Solution()
    s1, s2, s3 = "aabcc", "dbbca", "aadbbcbcac"
    print(solu.isInterleave(s1, s2, s3))

