from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        n = len(digits)
        if digits[-1] < 9 :
            digits[-1] += 1
        else:
            i = -1

            while digits[i] == 9:
                digits[i] = 0  # 变成0 然后进一位
                if (-i) < n:
                    if digits[i -1] != 9:
                        digits[i - 1] += 1
                    else:
                        i -= 1
                else:
                    digits.insert(0, 1)

        return digits