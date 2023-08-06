class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0: return 1.0
        if n == -1: return 1.0/x
        return self.myPow(x*x, n//2) * ([1, x][n%2])

if __name__ == '__main__':
    solu = Solution()
    print(solu.myPow(2, 4))