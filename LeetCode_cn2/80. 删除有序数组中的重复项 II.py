class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums: return 0
        n = len(nums)
        if n < 2: return n
        fast,  slow = 2, 2

        while fast < n:
            if nums[fast] != nums[slow-2]:
                nums[slow] = nums[fast]
                slow += 1
            fast +=1
        return slow


