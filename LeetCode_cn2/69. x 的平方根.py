class Solution:
    def mySqrt(self, x: int) -> int:

        low , high = 1, x

        while low <= high:

            mid = (low + high) // 2
            mid_value = mid * mid
            if mid_value == x:
                return mid

            elif mid_value < x:
                low = mid + 1
            else:
                high = mid - 1

        return high