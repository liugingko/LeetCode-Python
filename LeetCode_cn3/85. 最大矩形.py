from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        res_nums = [0] * len(matrix[0])
        max_s = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if int(matrix[i][j]) == 0:
                    res_nums[j] = 0
                res_nums[j] += int(matrix[i][j])
            max_s = max(max_s, self.largestRectangleArea(res_nums))  # 求出当前形成柱形的面积，与之前比较取最大的面积
        return max_s

    def largestRectangleArea(self, heights: List[int]) -> int:

        heights.append(0)
        stack = [-1]

        max_area = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h*w)

            stack.append(i)
        heights.pop()
        return max_area