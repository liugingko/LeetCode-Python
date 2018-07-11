class Solution:
    def lemonadeChange(self, bills):
        five, ten = 0, 0
        for bill in bills:
            if bill == 5: five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:  # --- 出现 20 的情况
                if ten and five:  # 优先考虑 10+5，这个组合
                    ten -= 1
                    five -= 1
                elif five >= 3: five -= 3  # 如果 10+5组合找不开，考虑5+5+5组合
                else: return False  # 还找不开，就说明真的找不开了

        return True


if __name__ == '__main__':
    solu = Solution()
    bills = [5, 5, 5, 10, 20]
    print(solu.lemonadeChange(bills))