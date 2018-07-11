# @Time   :2018/6/27
# @Author :LiuYinxing



class Solution:
    def canWinNim(self, n):
        return n % 4 != 0


if __name__ == '__main__':
    n = 5
    solu = Solution()
    print(solu.canWinNim(n))