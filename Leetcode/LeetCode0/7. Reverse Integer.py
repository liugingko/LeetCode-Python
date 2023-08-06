class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        out = 0
        if x>0:
            out = int(str(x)[::-1])
        elif x == 0:
            out = 0
        else:
            out = -int(str(x)[1:][::-1])

        if out >=2147483647  or out <=-2147483647:
            return 0
        else:
            return out



if __name__ == '__main__':
    solu = Solution()
    n = -103
    out = solu.reverse(n)

    print(out)