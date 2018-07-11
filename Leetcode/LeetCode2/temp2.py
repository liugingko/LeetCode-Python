# @Time   :2018/6/7
# @Author :LiuYinxing


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


if __name__ == '__main__':
    solu = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solu.rotate(matrix))