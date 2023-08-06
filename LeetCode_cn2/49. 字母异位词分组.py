from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}

        for s in strs:
            k = ''.join(sorted(s))
            if res.get(k):
                res[k].append(s)
            else:
                res[k] = [s]

        return  [res[k] for k in res]
