from random import choice
import random
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return choice([idx for idx, val in enumerate(self.nums) if val==target])

    def pick1(self, target):
        n, rst = 0, None

        for idx, num in enumerate(self.nums):
            if (target == num):
                n += 1
                if (random.random() < 1 / n): rst = idx

        return rst

if __name__ == '__main__':
    A, B = 'aabc', 'abca'
    solu = Solution()
    print(solu.kSimilarity(A, B))