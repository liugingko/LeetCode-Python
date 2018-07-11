class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        return True if str(x)==str(x)[::-1] else False

if __name__ == '__main__':
    solu = Solution()
    x = 112
    out = solu.isPalindrome(x)

    print(out)