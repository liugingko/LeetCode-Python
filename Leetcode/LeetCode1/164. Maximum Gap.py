import math


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N < 2: return 0

        min_n, max_n = min(nums), max(nums)  # 获取最大值和最小值

        gap = int(math.ceil((max_n-min_n)/float(N-1)))  # 向上取整

        buckets = [[None, None] for _ in range(N-1)]  # 建立一个桶

        for x in nums:
            if x == max_n:  # 如果等于最大值
                continue
            slot = int((x-min_n)/gap)  # 查找当前元素落在了那个桶里面了

            buckets[slot][0] = min(buckets[slot][0], x) if buckets[slot][0] else x  # 更新桶内元素，并维护桶内最大值和最小值
            buckets[slot][1] = max(buckets[slot][1], x) if buckets[slot][1] else x
        max_gap, prev_max = gap, buckets[0][1]

        # 获取最大间隔
        for b in buckets:
            if b[0] == None and b[1] == None:
                continue
            else:
                max_gap = max(max_gap, b[0]-prev_max)
                prev_max = b[1]
        if prev_max:
            max_gap = max(max_gap, max_n-prev_max)
        return max_gap

    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 1: return 0
        sorted_gap = 0
        nums = list(set(nums))

        nums.sort()

        for curr in range(len(nums[:-1])):
            gap = nums[curr + 1] - nums[curr]
            if gap > sorted_gap:
                sorted_gap = gap

        return sorted_gap


if __name__ == '__main__':
    nums = [3,6,9,1]
    solu = Solution()
    print(solu.maximumGap(nums))