from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates = sorted(candidates)
        # print(candidates)
        res = list()
        def dfs(index, curr, remain):

            if remain == 0: res.append(curr[:])

            for i in range(index, len(candidates)):
                d = candidates[i]
                if d > remain: break  # 提前结束
                if i > index and d == candidates[i-1]:  # 如何和上位置数字一样，
                    continue
                curr.append(d)
                dfs(i+1, curr, remain - d)
                curr.pop()

        dfs(0, [], target)
        return res

if __name__ == '__main__':
    sol = Solution()
    candidates = [2, 3, 6, 7, 1]
    target = 7

    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8

    candidates = [2,5,2,1,2]
    target = 5

    print(sol.combinationSum2(candidates, target))
