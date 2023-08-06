import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        n = len(nums)

        presums = collections.defaultdict(int)

        presums[0] = 1
        pre_sum = 0

        for i in range(n):

            pre_sum += nums[i]

            count += presums[pre_sum - k]

            presums[pre_sum] += 1

        return count