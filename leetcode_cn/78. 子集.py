class Solution:
    def subsets(self, nums):
        res = [[]]

        for i in nums:
            tmp = []
            for zl in res:
                tmp.append([i] + zl)

            print("tmp", tmp)
            res = res + tmp
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets([1,2,3]))