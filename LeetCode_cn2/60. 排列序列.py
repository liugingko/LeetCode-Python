import math


class Solution:
    def getPermutation(self, n, k):
        res = [0] * n
        numbers = [x for x in range(1, n + 1)]
        k = k - 1

        i = 0
        while i < n:
            fact = math.factorial(n - 1 - i)  # 获取阶乘
            index = k // fact
            res[i] = numbers[index]  # 确定一位数字
            numbers.pop(index)  # 使用过的数字，将不再使用

            # 更新 k
            k -= index * fact  # 或者 k = k % fact
            i += 1
        return ''.join([str(x) for x in res])


if __name__ == '__main__':
    print(Solution().getPermutation(17, 100))
