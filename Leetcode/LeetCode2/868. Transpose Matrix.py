# @Time   :2018/7/9
# @Author :LiuYinxing


class Solution:
    def transpose(self, A):
        A[::] = zip(*A)
        return A

    def transpose1(self, A):
        if len(A) == 0: return []
        r, c = len(A), len(A[0])
        return [[A[i][j] for i in range(r)] for j in range(c)]


if __name__ == '__main__':
    solu = Solution()
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solu.transpose(A))