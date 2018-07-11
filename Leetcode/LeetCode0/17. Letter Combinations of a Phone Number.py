from itertools import product


class Solution:

    def letterCombinations(self, digits):
        if not digits: return []  # 如果为空，返回空列表
        dict = {'1': [''],
                '2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}

        # index 表示 digits字符串中的字符索引
        # paths 表示走过的字符串，走到头，就保存到 res， 然后回溯当上一个位置，继续。
        def dfs(dict, digits, index, paths, res):  # 定义内部，递归函数
            if index == len(digits):
                res.append(paths)
                return
            for s in dict[digits[index]]:
                dfs(dict, digits, index + 1, paths + s, res)

        res = []
        dfs(dict, digits, 0, '', res)
        return res
    def letterCombinations1(self, digits):
        if not digits: return []  # 如果为空，返回空列表
        dict = {'1': [''],
                '2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}

        input = [dict[digit] for digit in digits]

        return [''.join(i) for i in product(*input)]

    def letterCombinations2(self, digits):
        if not digits: return []  # 如果为空，返回空列表
        dict = {'1': [''],
                '2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}

        input = [dict[digit] for digit in digits]  # 获取对应的字符

        return [''.join(i) for i in product(*input)]  # 使用 product 做笛卡尔积


if __name__ == '__main__':
     digits = '92'
     solu = Solution()
     print(solu.letterCombinations(digits))