class Solution(object):
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result


if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    solu = Solution()
    out = solu.subsets(nums)
    print(out)