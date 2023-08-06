from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n, m = len(matrix), len(matrix[0])
        left, right = 0, n*m -1

        while left <= right:

            mid = left + (right - left) // 2  # 比较特殊，要考虑前面的前面的长度
            cur = matrix[mid//m][mid%m]  # 第一行有多少数据，

            if cur == target: return True
            elif cur < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
