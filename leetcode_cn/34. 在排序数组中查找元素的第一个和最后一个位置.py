class Solution:
    def searchRange(self, nums, target):

        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False) - 1

        # print(left, right)

        if left <= right and right < len(nums) and nums[left]==target and nums[right]==target:
            return [left, right]
        return [-1, -1]

    def binarySearch(self, nums, target, lower):

        lift, right = 0, len(nums) - 1
        res = len(nums)

        while lift <= right:
            mid = (lift + right) // 2

            if (nums[mid] > target) or (lower and nums[mid] >= target):
                right = mid - 1
                res = mid
            else:
                lift = mid + 1
           #  print(mid, res)
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    print(sol.searchRange(nums, 8))