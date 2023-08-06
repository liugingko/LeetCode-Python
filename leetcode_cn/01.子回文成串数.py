class Solution:
    def allstr(self, s):
        def f(str1):
            if len(str1) <= 1:
                return str1
            list1 = []
            for i in range(len(str1)):
                for j in f(str1[0:i] + str1[i + 1:]):
                    list1.append(str1[i] + j)
            return set(list1)

        return f(s)

    def countSubstrings(self, s):
        n = len(s)
        ans = 0
        for i in range(2 * n - 1):
            l = int(i / 2)
            r = int(i / 2) + i % 2
            while (l >= 0 and r < n and s[l] == s[r]):
                l -= 1
                r += 1
                ans += 1
        return ans


if __name__ == '__main__':

    sol = Solution()
    allstrlist = sol.allstr('abac')
    for s in allstrlist:
        print(s, sol.countSubstrings(s))