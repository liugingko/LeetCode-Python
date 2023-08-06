# @Time   :2022/1/26
# @Author :lyx


class Solution:
    def runningSum(self, nums):
        sum = 0
        res = []

        for v in nums:
            sum += v
            res.append(sum)

        return res


if __name__ == '__main__':
    solu = Solution()
    nums = [1,2,3,4]
    print(solu.runningSum(nums))