class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        res = [0] * (len(num1) + len(num2))

        pos = len(res) - 1

        for s1 in reversed(num1):
            tmp_pos = pos
            for s2 in reversed(num2):
                res[tmp_pos] += int(s1) * int(s2)
                res[tmp_pos -1] += res[tmp_pos] // 10
                res[tmp_pos] %= 10
                tmp_pos -= 1
            pos -= 1

        index = 0
        while index < len(res) - 1 and res[index] == 0:
            index += 1

        return ''.join(map(str, res[index:]))

if __name__ == '__main__':
    num1, num2 = "123", "456"
    solu = Solution()
    print(solu.multiply(num1, num2))


