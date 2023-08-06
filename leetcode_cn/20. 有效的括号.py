class Solution:
    def isValid(self, s):

        if not s or len(s)==1: return False

        flag = {
            '(':1,
            '{':1,
            '[':1,
            ')':'(',
            '}':'{',
            ']':'['}
        stack = []

        for one in s:
            ff = flag.get(one)
            if ff == 1:
                stack.append(one)
            else:
                if len(stack) == 0:
                    return False

                tmp = stack.pop()
                if tmp == ff:
                    continue
                else:
                    return False
        return True if len(stack)==0 else False

if __name__ == '__main__':

    sol = Solution()
    print(sol.isValid('){'))