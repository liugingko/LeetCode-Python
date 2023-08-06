class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        if n==0:return 0
        if n==1:return 1

        dp = [1] * n
        for i in range(n):

            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        print(dp)
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()

    #print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
    print(sol.lengthOfLIS([1,3,6,7,9,4,10,5,6]))