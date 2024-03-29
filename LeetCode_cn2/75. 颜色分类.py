class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        cnt = [0] * 3
        for v in nums:
            cnt[v] += 1

        j = 0
        for i in range(3):
            while cnt[i]:
                nums[j] = i
                j += 1
                cnt[i] -= 1