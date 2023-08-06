class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = [-1] * n   # cnt 用计数，q用于已经放的位置，例如q[2]=3 表示第3行的放到了第4个位置
        count = 0
        def dfs(k, n):
            nonlocal count
            if k == n:
                count += 1
            else:
                for j in range(n):  # 一行一行的进行深度搜索
                    if self.place(k, j, q):
                        q[k] = j
                        dfs(k+1, n)
        dfs(0, n)
        return count

    def place(self, k, j, q):  # 判断该位置是否可以放一个棋子
        for i in range(k):
            if q[i] == j or abs(q[i]-j) == abs(i-k):  # 不同列，不同斜线
                return 0
        return 1


if __name__ == '__main__':
    solu = Solution()
    print(solu.totalNQueens(10))