from astroid import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n, m = len(matrix), len(matrix[0])
        x, y = 0, m-1

        while x < n and y >= 0:

            if matrix[x][y] == target:
                return True

            if matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False
