# @Time   :2018/6/26
# @Author :LiuYinxing
# 解题思路 大根堆

import heapq

class Solution:
    def sift(self, nums, low, high):
        i, j = low, 2 * low  # nums[j] 是 nums[i]的左孩子
        tmp = nums[i]
        while j <= high:
            if j < high and nums[j] < nums[j + 1]:  # 若右孩子较大，把 j 指向右孩子
                j += 1
            if tmp < nums[j]:
                nums[i] = nums[j]  # 将 nums[j] 调整到双亲节点的位置上
                i = j  # 修改 i 和 j 值，以便继续向下筛选
                j = 2 * i
            else: break  # 筛选结束
        nums[i] = tmp  # 被筛选节点的值放入最终位置

    def findKthLargest(self, nums, k):
        n = len(nums)
        for i in range(n//2, -1, -1):  # 循环建立初始堆
            self.sift(nums, i, n-1)
        for i in range(n-1, n-1-k, -1):  # 进行排序，每一趟堆排序的元素个数减1
            nums[i], nums[0] = nums[0], nums[i]  # 将最后一个元素同当前区间内 nums[0] 对换
            self.sift(nums, 0, i - 1)
        return nums[i]


    def findKthLargest1(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

if __name__ == '__main__':
    nums, k = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4
    solu = Solution()
    print(solu.findKthLargest(nums, k))