# @Time   :2018/6/22
# @Author :LiuYinxing
# 解题思路 区间动态规划


class Solution:
    def maxCoins(self, iNums):
        nums = [1] + [i for i in iNums if i > 0] + [1]  # 清除为0的数字，因为0不会得分，然后首位添加[1],方便计算
        n = len(nums)
        dp = [[0] * n for _ in range(n)]  # 初始化dp
        for k in range(2, n):  # k 确定一个滑动窗口的大小，从2开始
            for left in range(0, n - k):  # 滑动窗口，从左向右滑动，确定区间的开始（left）、结束（right）位置
                right = left + k
                for i in range(left + 1, right):  # 开始枚举，区间内哪一个数字作为最后一个被打掉，使其得分最高
                    dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n - 1]


if __name__ == '__main__':
    nums = [3,1,5,8]
    solu = Solution()
    out = solu.maxCoins(nums)
    print(out)