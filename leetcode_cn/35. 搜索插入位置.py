class Solution:
    def searchInsert(self, nums, target):

        lift, right = 0, len(nums) - 1
        res = len(nums)

        while lift <= right:
            mid = (lift + right) // 2
            if nums[mid] >= target:
                right = mid - 1
                res = mid
            else:
                lift = mid + 1
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    target = 2
    target = 7
    print(sol.searchInsert(nums, target))