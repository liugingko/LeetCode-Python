from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res, tmp = [1] * (n:=len(nums)), 1

        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            tmp *= nums[i +1]

            res[i] *= tmp

        return res


if __name__ == '__main__':
    print(Solution().productExceptSelf([1,2,3,4]))