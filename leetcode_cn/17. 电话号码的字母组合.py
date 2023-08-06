class Solution:
    def letterCombinations(self, digits):
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if not digits:
            return []

        res = []
        res_tmp = []
        def dfs(index):

            if index == len(digits):
                res.append(''.join(res_tmp))
                return

            for i in phoneMap[digits[index]]:
                res_tmp.append(i)
                dfs(index+1)
                res_tmp.pop()

        dfs(0)
        return res
if __name__ == '__main__':
    sol = Solution()
    print(sol.letterCombinations('23'))

