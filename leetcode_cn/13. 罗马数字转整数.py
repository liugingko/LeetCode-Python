class Solution:
    SYMBOL_VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    def romanToInt(self, s):
        n = len(s)
        res = 0

        for i, ch in enumerate(s):
            value = Solution.SYMBOL_VALUES[ch]
            if i < n-1 and value < Solution.SYMBOL_VALUES[s[i + 1]]:
                res -= value
            else:
                res += value
        return res
