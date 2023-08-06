import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        count = collections.Counter(t)

        miss = len(t)
        i = m = n = 0
        for j, v in enumerate(s, 1):
            miss -= (count[v] > 0)
            count[v] -= 1
            if not miss:
                while i < j and count[s[i]] < 0:
                    count[s[i]] += 1
                    i += 1
                if not n or j-i <= n-m:
                    n, m = j, i

        return s[m:n]


if __name__ == '__main__':
    solu = Solution()
    s, t = 'ADOBECODEBANC', 'ABC'
    print(solu.minWindow(s, t))



