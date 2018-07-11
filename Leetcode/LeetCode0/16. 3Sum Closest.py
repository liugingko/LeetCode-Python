# @Time   :2018/7/6
# @Author :LiuYinxing


class Solution:
    def threeSumClosest(self, nums, target):

        n = len(nums)
        nums.sort()  # 排序
        result = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == target: return sum
                if abs(sum - target) < abs(result - target): result = sum  #更新最优值

                if sum < target: left += 1  # 向右移动
                elif sum > target: right -= 1  # 向左移动

        return result


if __name__ == '__main__':
    solu = Solution()
    nums, target = [-1, 0, 1, 2, -1, -4], 4
    print(solu.threeSumClosest(nums, target))