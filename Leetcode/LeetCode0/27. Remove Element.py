class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
            else:
                start += 1
        return start

    def removeElement1(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index = index + 1
        return index


if __name__ == '__main__':
    nums, val = [3, 2, 2, 3], 3
    solu = Solution()
    print(solu.removeElement(nums, val))