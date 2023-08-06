class Solution:
    def getRow(self, rowIndex: int):
        ret = list()
        for i in range(rowIndex):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i-1][j] + ret[i-1][j-1])
            ret.append(row)
        return row

if __name__ == '__main__':
    sol = Solution()
    print(sol.getRow(3))