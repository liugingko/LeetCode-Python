class Solution:
    def fourSum(self, nums, target):
        res = []
        length = len(nums)
        if not nums or length < 4:
            return res

        nums.sort()

        for i in range(length - 3):

            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 不能重复

            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target: break  # 前几个都和都大于目标值，所以没必要继续了
            if nums[i] + nums[length-3] + nums[length-2] + nums[length-1] < target: continue  # 最大的 都小于target 所以直接进入下一个循环

            for j in range(i+1, length-2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target: break  # 前几个都和都大于目标值，所以没必要继续了
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target: continue  # 最大的 都小于target 所以直接进入下一个循环

                left, right = j + 1,  length -1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:

                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        left += 1

                        while right > left and nums[right] == nums[right-1]:
                            right -= 1
                        right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return res

if __name__ == '__main__':
    sol = Solution()

    print(sol.fourSum([2,2,2,2,2], 8))
