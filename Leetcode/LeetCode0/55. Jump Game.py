class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        next_max = 0
        for i in range(n):
            if next_max >= i and nums[i]+i > next_max:
                next_max = nums[i] + i
        return next_max>=n-1



if __name__ == '__main__':
    solu = Solution()
    A = [2, 3, 1, 1, 4]  # return true.

    A = [3, 2, 1, 0, 4]  # return false.
    A = [1, 0, 1, 0]

    out = solu.canJump(A)
    print(out)
