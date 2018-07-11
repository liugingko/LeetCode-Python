class Solution(object):
    def canTransform(self, start, end):
        if start.replace('X', '') != end.replace('X', ''): return False  # 判断相对位置是否一样

        cntL1 = cntL2 = cntR1 = cntR2 = 0
        for v1, v2 in zip(start, end):  # 进行统计计算
            if v1 == 'L': cntL1 += 1
            elif v1 == 'R': cntR1 += 1
            if v2 == 'L': cntL2 += 1
            elif v2 == 'R': cntR2 += 1
            if cntL1 > cntL2 or cntR1 < cntR2: return False
        return True


if __name__ == '__main__':
    start, end = 'RXXLRXRXL', 'XRLXXRRLX'
    solu = Solution()
    print(solu.canTransform(start, end))