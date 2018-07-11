# @Time   :2018/7/8
# @Author :LiuYinxing


class Solution(object):
    def countAndSay(self, n):  # 递归实现
        if n == 1: return '1'  # 递归出口
        s = self.countAndSay(n-1)
        res, count = '', 0
        for i in range(len(s)):
            count += 1
            if i == len(s) - 1 or s[i] != s[i+1]:  # 最后一个字符串要提前终止
                res += str(count)
                res += s[i]
                count = 0
        return res

    def countAndSay1(self, n):  # 非递归实现
        if n == 1: return '1'
        res = '1'
        while n > 1:
            s, res, count = res, '', 0
            for i in range(len(s)):
                count += 1
                if i == len(s) - 1 or s[i] != s[i + 1]:  # 最后一个字符串要提前终止
                    res += str(count)
                    res += s[i]
                    count = 0
            n -= 1
        return res


if __name__ == '__main__':
    solu = Solution()
    print(solu.countAndSay(n=10))