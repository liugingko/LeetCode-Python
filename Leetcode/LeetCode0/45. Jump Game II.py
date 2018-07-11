class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        n = len(nums)
        if n == 1 or n == 0:
            return 0
        cur_max = 0  # 记录当前的可以达到的最远距离
        next_max = 0  # 记录下一步可以到达的最远值
        steps = 0  # 记录步数
        for i in range(n):
            if i > cur_max:  # 如下标 大于 当前可以到达的最远距离 则添加一步，并更新当前的可以到达的步数。
                steps = steps + 1
                cur_max = next_max
                if cur_max >= n:  # 如果当前到达的步数可以到达n 或者可以超过n 程序结束
                    break
            next_max = max(next_max, nums[i] + i)  # 更新下一步可以达到的最远距离
        return steps

    def jumpdp(self, nums):
        n = len(nums)
        if n==1 or n==0: return 0


if __name__ == '__main__':
    solu = Solution()
    nums = [2,3,1,1,4]
    out = solu.jump(nums)

    print(out)