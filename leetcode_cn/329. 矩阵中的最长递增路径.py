from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix):

        if not matrix: return 0  # 为空

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 确定四个方向，下、上、左、右
        rows, columns = len(matrix), len(matrix[0])

        # print(rows, columns)
        @lru_cache(maxsize=None)
        def dfs(row, column):
            best = 1

            for dx, dy in dirs:
                new_row, new_column = dx + row, dy + column
                if 0 <= new_row < rows and \
                    0 <= new_column < columns and \
                        matrix[row][column] > matrix[new_row][new_column]:

                    best = max(best, dfs(new_row, new_column)+1)
            return best

        res = 0

        for i in range(rows):
            for j in range(columns):
                res = max(res, dfs(i, j))

        dfs.cache_clear()
        return res


if __name__ == '__main__':
    sol = Solution()
    matrix = [[9,9,4],[6,6,8],[2,1,1]]

    print(sol.longestIncreasingPath(matrix))




