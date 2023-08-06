class Solution:
    def maxArea(self, height):

        left, right, max_area = 0, len(height)-1, 0

        while left < right:

            if height[left] < height[right]:
                tmp_area = height[left] * (right - left)
                left += 1
            else:
                tmp_area = height[right] * (right - left)
                right -= 1

            max_area = max(max_area, tmp_area)

        return max_area