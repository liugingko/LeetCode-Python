class Solution:

    def twoSum(self, num, target):
        dicts = {}

        for i in range(len(num)):
            if dicts.get(target-num[i]):
                return dicts.get(target-num[i]), i
            else:
                dicts[num[i]] = i
        return -1, -1


if __name__ == '__main__':

    sl = Solution()
    # output = sl.twoSum([3,2,4], 6)
    output = sl.twoSum([2,7,11,15], 9)
    print(output)