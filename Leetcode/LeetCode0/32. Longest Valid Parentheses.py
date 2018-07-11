class Solution:

    def longestValidParentheses(self, s):
        dp, res = [0] * len(s), 0  # 初始化dp、定义最优结果变量
        for i in range(len(s)):
            if s[i] == ')':  # 只考虑以')'结尾的子串
                if i > 0 and s[i - 1] == '(':  # 第一中情况，直接加 2
                    dp[i] = dp[i - 2] + 2
                if i > 0 and s[i - 1] == ')':  # 第二种情况，
                    if i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                        if i - dp[i - 1] - 1 > 0:  # 当前合法子串，前面还有子串，的情况
                            dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                        else:  # 当前合法子串，前面--没有--子串，的情况
                            dp[i] = dp[i - 1] + 2
                res = max(res, dp[i])  # 更新最长的合法子串
        return res

    def longestValidParentheses1(self, s):
        stack, res = [-1], 0
        for i, e in enumerate(s):
            if e == '(':
                stack.append(i)
            elif e == ')':
                stack.pop()
                if not stack:  # 如果栈为空，当前 位置索引 进栈
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res


if __name__ == '__main__':
    s = ')()())'
    solu = Solution()
    print(solu.longestValidParentheses1(s))
