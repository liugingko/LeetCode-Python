class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        print(len(s), len(s) >> 1)

        return s[:len(s) >> 1] == s[: - (len(s) >> 1) - 1: -1]


if __name__ == '__main__':

    sol = Solution()

    print(sol.isPalindrome(100020001))