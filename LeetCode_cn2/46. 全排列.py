from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        def dfs(remain_list, path):

            if not remain_list:
                res.append(path)

            for i in range(len(remain_list)):

                dfs(remain_list[:i] + remain_list[i+1:], path + [remain_list[i]])
        dfs(nums, [])
        return res

if __name__ == '__main__':
    solu = Solution()
    print(solu.permute(nums=[1, 2, 3]))
