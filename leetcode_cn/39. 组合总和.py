class Solution:
    def combinationSum(self, candidates, target):

        candidates = sorted(candidates)
        res = []

        def dfs(index, current, remain):

            for i in range(index, len(candidates)):
                d = candidates[i]
                if d == remain:
                    res.append(current+[d])
                elif d < remain:
                    dfs(i, current+[d], remain - d)
                else:
                    return

        dfs(0, [], target)
        return res


if __name__ == '__main__':
    sol = Solution()
    candidates = [2, 3, 6, 7, 1]
    target = 7

    print(sol.combinationSum(candidates, target))