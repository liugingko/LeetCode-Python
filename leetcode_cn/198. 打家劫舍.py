# @Time   :2018/10/01
# @Author :LiuYinxing


class Solution:
    def rob(self, nums):

        pre, cur = 0, 0
        for i in nums:
            pre, cur = cur,  max(i+pre, cur)
        return cur


if __name__ == '__main__':
    solu = Solution()
    nums = [2, 7, 9, 3, 1]
    print(solu.rob(nums))