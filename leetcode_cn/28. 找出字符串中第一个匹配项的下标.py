class Solution:
    def strStr(self, haystack, needle):

        n, m = len(haystack), len(needle)

        next = [0]  # 构造next数组
        k = 0
        for i in range(1, m):
            print(i)
            while k > 0 and needle[k] != needle[i]:
                k = next[k - 1]
            if needle[k] == needle[i]:
                k += 1
            next.append(k)

        print("n, m", n, m)
        print(next)
        # 主串位置判断
        j = 0
        for i in range(n):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == m:
                return i - j + 1
        return -1


if __name__ == '__main__':

    sol = Solution()
    print(sol.strStr('ababcabcacbab', "aaaaaaa"))