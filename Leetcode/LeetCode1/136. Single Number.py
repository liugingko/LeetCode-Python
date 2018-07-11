# @Time   :2018/6/26
# @Author :LiuYinxing
# 解题思路  运用异或运算的性质,对于任何数 x，都有 x ⊕ x=0，x ⊕ 0 = x


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0

        rst = 0
        for v in nums:
            rst ^= v

        return rst


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    solu = Solution()
    print(solu.singleNumber(nums))
