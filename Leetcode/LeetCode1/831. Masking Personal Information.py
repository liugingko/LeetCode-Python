import re

class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if '@' in S:
            left, right = S.lower().split('@')
            return left[0] + '*****' + left[-1] + '@' + right
        digits = re.sub('\D*', '', S)  # 删除非数字字符
        countryCode = len(digits) - 10
        print((countryCode and '+' + '*' * countryCode + '-' or ''))
        return (countryCode and '+' + '*' * countryCode + '-' or '') + '***-***-' + digits[-4:]


if __name__ == '__main__':
    solu = Solution()
    s = "LeetCode@LeetCode.com"
    s = "AB@qq.com"
    s = "1(234)567-890"
    s = "86-(10)12345678"
    print(solu.maskPII(s))