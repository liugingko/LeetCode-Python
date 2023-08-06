# @Time   :2022/1/26
# @Author :lyx


class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        leftSum = 0
        for i, x in enumerate(nums):
            if leftSum == (total - leftSum -x):
                return i
            leftSum += x
        return -1


if __name__ == '__main__':
    solu = Solution()
    nums = [1,7,3,6,5,6]
    print(solu.pivotIndex(nums))