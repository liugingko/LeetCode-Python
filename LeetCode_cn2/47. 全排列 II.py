from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(remain_list, path):

            if not remain_list:
                res.append(path)

            for i in range(len(remain_list)):
                if i > 0 and remain_list[i] == remain_list[i-1]: continue
                dfs(remain_list[:i] + remain_list[i + 1:], path + [remain_list[i]])
        dfs(nums, [])
        return res