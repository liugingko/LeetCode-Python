from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0] * (1 << n)
        print((1 << n), ans)
        for i in range(1 << n):
            print(i, (i >> 1))
            ans[i] = (i >> 1) ^ i
        return ans


if __name__ == '__main__':
    print(Solution().grayCode(4))