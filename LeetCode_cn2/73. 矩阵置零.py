class Solution:
    def setZeroes(self, matrix):

        first_col = False  # 用于记录 第一列是否有 0 没有为false

        n, m = len(matrix), len(matrix[0])

        for i in range(n):
            if matrix[i][0] == 0:  # 检测第一列是否有 0
                first_col = True
            for j in range(1, m):  # 从第二列开始，一行一行的扫描，然后在第一列和第一行上进行标记。
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0

        for i in range(1, n):  # 根据第一列和第一行的标记，对整个矩阵置0处理，不包括第一行和第一列。
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:  # 处理第一行
            for j in range(m):
                matrix[0][j] = 0

        if first_col:  # 处理第一列
            for i in range(n):
                matrix[i][0] = 0


if __name__ == '__main__':
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]]
    solu = Solution()
    solu.setZeroes(matrix)
    for row in matrix:
        print(row)
