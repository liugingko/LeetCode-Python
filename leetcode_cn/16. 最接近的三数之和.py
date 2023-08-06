class Solution:
    def threeSumClosest(self, nums, target):

        n = len(nums)
        nums.sort()
        min_sum = 10**7

        for a in range(n):

            if a > 0 and nums[a] == nums[a - 1]:
                continue

            b = a + 1
            c = n - 1  # 倒着来
            print(nums)
            while b < c:
                s = nums[a] + nums[b] + nums[c]
                print('index:', a,b,c)
                print(min_sum, s, '-->:', nums[a] , nums[b] , nums[c], '\n')
                if s == target:
                    return target

                if abs(s - target) < abs(min_sum-target):
                    min_sum = s

                if s > target:
                    k0 = c - 1
                    while b < k0 and nums[k0]==nums[c]:
                        k0 -= 1
                    c = k0
                else:
                    j0 = b + 1
                    while j0 < c and nums[j0]==nums[b]:
                        j0 += 1
                    b = j0

        return min_sum


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    sol = Solution()
    print(sol.threeSumClosest(nums, target))