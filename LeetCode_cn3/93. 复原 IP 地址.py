from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        n = len(s)
        def dfs(s, start, k, tmp):
            if k == 4:
                if start == n:
                    res.append('.'.join(tmp))
                else:
                    return

            for i in range(1, 4):
                if start + i > n:
                    break

                if i > 1 and s[start] == '0':
                    continue

                if i != 3 or int(s[start:start+i]) < 256:
                    dfs(s, start+i, k + 1, tmp + [s[start:start+i]])

        dfs(s, 0, 0, [])
        return res