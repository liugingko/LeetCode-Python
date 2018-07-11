# @Time   :2018/6/27
# @Author :LiuYinxing
import math


class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))


if __name__ == '__main__':
    n = 6
    solu = Solution()
    print(solu.bulbSwitch(n))