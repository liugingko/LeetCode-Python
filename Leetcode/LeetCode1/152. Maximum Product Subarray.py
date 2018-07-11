import sys


class Solution:
    def maxstrtest(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        dp1[i]=max(data[i],dp1[i-1]*data[i],dp2[i-1]*data[i]);
        dp2[i]=min(data[i],dp1[i-1]*data[i],dp2[i-1]*data[i]);
        """
        n = len(nums)
        if n == 1: return nums[0]
        if n < 1: None
        dpmax, dpmin = [0]*n, [0]*n
        dpmax[0] = dpmin[0] = nums[0]
        for i in range(1,n):
            dpmax[i] = max(nums[i], dpmax[i - 1] * nums[i], dpmin[i - 1] * nums[i])
            dpmin[i] = min(nums[i], dpmax[i - 1] * nums[i], dpmin[i - 1] * nums[i])
        return max(dpmax)

    def maxstrtest1(self, nums):
        if len(nums) == 1: return nums[0]
        dpmax, dpmin, maxout= 1, 1, float('-inf')
        for xi in nums:
            dpmax, dpmin = max(xi, dpmax * xi, dpmin * xi), min(xi, dpmax * xi, dpmin * xi)
            maxout = max(maxout, dpmax)
        return maxout

if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    nums = [2, -1, 1, 1]
    solu = Solution()
    #out = solu.maxProduct(nums)
    out = solu.maxstrtest1(nums)
    print(out)