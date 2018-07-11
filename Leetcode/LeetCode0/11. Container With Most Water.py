class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left, right, maxarea = 0, len(height)-1, 0
        while left < right:

            if height[left] < height[right]:
                tmp = height[left]*(right-left)
                left += 1
            else:
                tmp = height[right] * (right - left)
                right -= 1
            if maxarea < tmp:
                maxarea = tmp
        return maxarea

if __name__ == '__main__':
    solu = Solution()
    height = [1, 1]
    print(solu.maxArea(height))