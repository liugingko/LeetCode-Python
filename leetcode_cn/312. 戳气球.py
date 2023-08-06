# @Time   :2023/05/16
# 解题思路 区间动态规划


class Solution:
    def maxCoins(self, iNums):

        nums = [1] + [v for v in iNums if v !=0] + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for k in range(2, n):
            for left in range(n-k):
                right = left + k
                for i in range(left+1, right):
                    dp[left][right] = max(dp[left][right], nums[left]*nums[i]*nums[right] + dp[left][i] + dp[i][right])

        return dp[0][n-1]



if __name__ == '__main__':
    nums = [3,1,5,8]
    solu = Solution()
    out = solu.maxCoins(nums)
    print(out)