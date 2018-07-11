class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (high + low)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid -1
            if nums[mid] < target:
                low = mid + 1
        return ((high+low)//2) + 1

        # num = [i for i in nums if i < target]
        # return len(num)

if __name__ == '__main__':
    solu = Solution()
    nums, target = [1], 1
    print(solu.searchInsert(nums, target))