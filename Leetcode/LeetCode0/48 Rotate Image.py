# @Time   :2018/6/7
# @Author :LiuYinxing


import numpy as np

class Solution:
    def rotate(self, matrix):  # 方法1， 使用zip()
        matrix[::] = zip(*matrix[::-1])
        return matrix

    def rotate1(self, matrix):  # 方法2
        matrix = matrix[::-1]  # 逆序操作
        for i in range(len(matrix)):  # 转置
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

    def rotate2(self, matrix):
        mat = np.array(matrix)
        a = mat.shape[0]
        k = mat[a - 1]
        k = k[:, np.newaxis]
        while a > 1:
            p = mat[a - 2]
            p = p[:, np.newaxis]
            a = a - 1
            k = np.hstack((k, p))
        return k

    def rotate1(self, matrix):  # 方法2
        matrix = matrix[::-1]  # 逆序操作
        for i in range(len(matrix)):  # 转置
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix



if __name__ == '__main__':
    solu = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    out = solu.rotate2(matrix)

    print(out)