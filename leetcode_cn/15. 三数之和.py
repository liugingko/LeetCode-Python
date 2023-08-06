class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        res = list()

        for a in range(n):

            if a > 0 and nums[a] == nums[a-1]:
                continue

            c = n -1  # 倒着来
            target = - nums[a]

            for b in range(a+1, n):
                if b > a+1 and nums[b] == nums[b - 1]:
                    continue

                while b < c and nums[c] + nums[b] > target:
                    c -= 1
                
                if b == c: break

                if nums[b] + nums[c] == target:
                    res.append([nums[a], nums[b],  nums[c]])
        return res


