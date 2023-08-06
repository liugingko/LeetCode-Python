class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        out = 0
        if x > 0:
            out = int(str(x)[::-1])
        elif x == 0:
            out = 0
        else:
            out = -int(str(x)[1:][::-1])

        if out >= 2147483647 or out <= -2147483647:
            return 0
        else:
            return out


'''
        s = (x > 0) - (x < 0)
        r = int(str(x*s)[::-1])
        return s*r * (r < 2**31)

        s = cmp(x, 0)
        r = int(`s * x`[::-1])
        return (r < 2 ** 31) * s * r

'''

if __name__ == '__main__':
    solu = Solution()
    n = -103
    out = solu.reverse(n)

    print(out)