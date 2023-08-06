class Solution:
    def divide(self, dividend, divisor):

        if abs(dividend) < abs(divisor): return 0

        limit = 2**31 -1
        neg = (dividend <0) != (divisor <0)
        dividend, divisor =  abs(dividend), abs(divisor)

        res, div, temp = 0, divisor, 1
        while dividend > divisor:
            while dividend > (div<<1):
                div <<= 1
                temp <<= 1

            dividend -= div
            div = divisor
            res += temp
            temp = 1

        res = -res if neg else res
        return res if -2**31 <= res <= 2**31-1 else limit

