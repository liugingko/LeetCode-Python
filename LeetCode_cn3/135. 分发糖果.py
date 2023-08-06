class Solution:
    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)
        res = [1] * n

        lbase, rbase = 1, 1

        for i in range(1, n):

            if ratings[i] > ratings[i-1]:
                lbase += 1
            else:
                lbase = 1

            res[i] = lbase

        for i in range(n-2, -1, -1):

            if ratings[i] > ratings[i+1]:
                rbase += 1
            else:
                rbase = 1

            res[i] = max(rbase, res[i])

        return sum(res)