from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if len(intervals) == 0:
            return [newInterval]

        i = 0
        while i < len(intervals):
            if intervals[i][0] > newInterval[0]:
                break
            i += 1
        intervals.insert(i, newInterval)

        res = [intervals[0]]
        for i, e in enumerate(intervals, start=1):
            if res[-1][1] >= e[0]:
                res[-1][1] = max(e[1], res[-1][1])  # 合并选择最大的一个
            else:
                res.append(e)

        return res