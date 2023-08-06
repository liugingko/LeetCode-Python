class Solution:

    def twoSum(self, nums, target):
        dicts = {}
        for i in range(len(nums)):

            if nums[i] not in dicts:
                return dicts[nums[i]], i
            else:
                dicts[target - nums[i]] = i
        return -1, -1


if __name__ == '__main__':

    sl = Solution()
    output = sl.twoSum([3,2,4], 6)
    print(output)