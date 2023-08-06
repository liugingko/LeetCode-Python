class Solution:
    def removeElement(self, nums, val):

        if not nums: return 0

        n = len(nums)
        fast,  slow = 0, 0

        while fast < n:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast +=1

        return slow