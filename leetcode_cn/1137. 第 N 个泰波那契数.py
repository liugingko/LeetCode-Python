class Solution:
    def tribonacci(self, n):
        if n == 0: return 0
        if n == 1: return 1

        pre0, pre1, cur = 0, 1, 1
        for i in range(2, n):
            # print(i, pre0, pre1, cur)
            pre0, pre1, cur = pre1, cur, pre0 + pre1 + cur

        # print(cur)
        return cur


if __name__ == '__main__':
    sol = Solution()
    print(sol.tribonacci(4))
    print(sol.tribonacci(25))