class Solution:
    def generate(self, numRows):
        ret = list()
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i-1][j] + ret[i-1][j-1])
            print(row)
            ret.append(row)
        return ret[-1]
if __name__ == '__main__':
    sol = Solution()
    print(sol.generate(5))