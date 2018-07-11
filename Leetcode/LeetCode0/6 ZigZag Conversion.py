class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s)<=numRows: return s
        listtmp = ['']*numRows
        index, step = 0, 1

        for x in s:
            listtmp[index] += x
            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1
            index += step
        return ''.join(listtmp)

if __name__ == '__main__':
    solu = Solution()

    s = "PAYPALISHIRING"

    out = solu.convert(s,3)

    print(out)