class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
        """

        stack = []
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            else:
                if not stack or {')': '(', ']': '[', '}': '{'}[i] != stack[-1]:
                    return False
                stack.pop()
        return not stack


if __name__ == '__main__':
    solu = Solution()
    s = '['
    print(solu.isValid(s))