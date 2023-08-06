class Solution:
    def addBinary(self, a: str, b: str) -> str:

        n, m = len(a) -1 , len(b) -1

        res = []
        s = 0

        while n >= 0 or m >=0 or s:
            if n >= 0:
                s += int(a[n])
                n -= 1
            if m >= 0:
                s +=int(b[m])
                m -= 1
            res.append(s % 2)

            s //= 2
        # print(res[::-1])
        return ''.join([str(v) for v in res[::-1]])

if __name__ == '__main__':
    a = "1010"
    b = "1011"
    print(Solution().addBinary(a,b))