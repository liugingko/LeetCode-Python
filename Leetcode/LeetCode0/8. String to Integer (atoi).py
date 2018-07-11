class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.replace(' ', '')
        if len(str) == 0:
            return 0
        elif int(str) >= 2**31:
            return 2**31
        elif int(str) <= -2**31:
            return -2**31
        else:
            return int(str)


if __name__ == '__main__':
    solu = Solution()
    n = ''
    out = solu.myAtoi(n)
    print(out)