import re
import collections


# class Solution(object):
#     def countOfAtoms(self, formula):
#         parse = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
#         print(parse)
#         stack = [collections.Counter()]
#         for name, m1, left_open, right_open, m2 in parse:
#             if name:
#               stack[-1][name] += int(m1 or 1)
#             if left_open:
#               stack.append(collections.Counter())
#             if right_open:
#                 top = stack.pop()
#                 for k in top:
#                   stack[-1][k] += top[k] * int(m2 or 1)
#
#         return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '')
#                        for name in sorted(stack[-1]))

class Solution:
    def countOfAtoms(self, formula):
        dic, coeff, stack, elem, cnt, i = collections.defaultdict(int), 1, [], '', 0, 0
        for c in formula[::-1]:
            if c.isdigit():
                cnt += int(c) * (10 ** i)  # 获取当前数子
                i += 1  # 当前数字的位数
            elif c == ')':  # 当前数字入栈，并更新当前元素的系数
                stack.append(cnt)
                coeff *= cnt
                i = cnt = 0
            elif c == '(':  # 出栈，并更新当前系数（相除哦）
                coeff //= stack.pop()
                i = cnt = 0
            elif c.isupper():  # 元素写入字典，
                elem = c + elem
                dic[elem] += (cnt or 1) * coeff  # 当前数字 * 当前的系数 + 之前已经存在的个数。
                elem = ''
                i = cnt = 0
            elif c.islower():  # 拼接，保留到 elem 中
                elem = c + elem
        return ''.join(k + str(v > 1 and v or '') for k, v in sorted(dic.items()))


if __name__ == '__main__':
    solu = Solution()
    formula = 'K4(ON(SO3)2)2'
    print('formula:', 'K4(ON(SO3)2)2')
    print(solu.countOfAtoms(formula))