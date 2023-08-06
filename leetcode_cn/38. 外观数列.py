class Solution:
    def countAndSay(self, n):

        if n == 1:return '1'

        s = self.countAndSay(n - 1)
        res, count = '', 0

        for i in range(len(s)):
            count += 1
            if i == len(s)-1 or s[i] != s[i+1]:
                res += str(count)
                res += s[i]
                count = 0
        return  res