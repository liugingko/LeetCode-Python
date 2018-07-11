class Solution:
    def strStr(self, haystack, needle):
        if len(needle) == 0: return 0

        n, m = len(haystack), len(needle)
        next = [0] * m
        self.GetNext(needle, next)  # 初始化next数组

        i, j = 0, 0
        while i < n and j < m:
            if j == -1 or haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                j = next[j]

        return i - m if j >= m else -1

    def GetNext(self, t, next):  # 计算next数组
        j, k, next[0], n = 0, -1, -1, len(next)
        while j < n-1:
            if k == -1 or t[j] == t[k]:
                j, k = j + 1, k + 1
                next[j] = k
            else:
                k = next[k]

    def GetNext1(self, t, next):  # 计算改进版next数组
        j, k, next[0], n = 0, -1, -1, len(next)
        while j < n-1:
            if k == -1 or t[j] == t[k]:
                j, k = j + 1, k + 1
                if t[j] != t[k]:
                    next[j] = k
                else:
                    next[j] = next[k]
            else:
                k = next[k]
                
    def strStr1(self, haystack, needle):
        if needle == "":
            return 0
        if haystack == "" or needle == "" or len(haystack.split(needle)) == 1:
            return -1
        return len(haystack.split(needle)[0])

    def strStr2(self, haystack, needle):
        return haystack.find(needle)


if __name__ == '__main__':
    haystack, needle = 'hello', 'll'
    # haystack, needle = 'aaaaa', 'bba'
    solu = Solution()
    print(solu.strStr(haystack, needle))