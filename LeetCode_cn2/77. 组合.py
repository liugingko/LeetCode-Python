
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        def dfs(i, tmp):

            if len(tmp) == k:
                res.append(tmp)
                return
            for j in range(i, n+1):
                dfs(j+1, tmp+[j])
        dfs(1, [])
        return res

if __name__ == '__main__':
    pass