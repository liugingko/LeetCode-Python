class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0: return None
        summax, cur = nums[0], nums[0]
        for v in nums[1:]:
            if cur+v > v:
                cur = cur + v
            else:
                cur = v
            if cur > summax:
                summax = cur
        return summax

if __name__ == '__main__':
    solu = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    out = solu.maxSubArray(nums)
    print(out)