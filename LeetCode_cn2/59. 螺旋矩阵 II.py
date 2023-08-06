# @Time   :2018/11/21
# @Author :LiuYinxing


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1: return [[1]]

        matrix = [[0] * n for _ in range(n)]

        top = 0  # 上边
        bottom = n - 1  # 下边
        left = 0  # 左边
        right = n - 1  # 右边

        cnt = 1
        while top < bottom and left < right:

            for y in range(left, right + 1):  # 写入最上面一行数据
                matrix[top][y] = cnt
                cnt += 1

            for x in range(top + 1, bottom):  # 写入最右边一列数据
                matrix[x][right] = cnt
                cnt += 1

            for y in range(right, left - 1, -1):  # 写入最下面一行数据
                matrix[bottom][y] = cnt
                cnt += 1

            for x in range(bottom - 1, top, -1):  # 写入最左边一列数据
                matrix[x][left] = cnt
                cnt += 1

            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1  # 四个边界，分别向内部移动一个位置

        if top == bottom:  # 如果最后剩下一行数据
            for y in range(left, right + 1):
                matrix[top][y] = cnt
                cnt += 1

        elif left == right:  # 如果最后剩下一列数据
            for x in range(top, bottom + 1):
                matrix[x][right] = cnt
                cnt += 1

        return matrix


if __name__ == '__main__':
    matrix = Solution().generateMatrix(6)
    for row in matrix:
        print(row)

