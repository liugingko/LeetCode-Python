import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        return max(c.keys(), key=c.get)