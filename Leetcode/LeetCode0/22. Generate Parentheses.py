class Solution:
    def generateParenthesis(self, n):
        ans = []

        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if left < n:  # 一直添加左括号
                backtrack(s+'(', left+1, right)
            if left > right:  # 保证左括号的个数大于右括号的情况下，才能添加右括号
                backtrack(s+')', left, right+1)

        backtrack()
        return ans


if __name__ == '__main__':
    n = 3
    solu = Solution()
    print(solu.generateParenthesis(n))