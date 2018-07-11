class Solution:

    def twoSum(self, num, target):
        dicts = {}
        for i in range(len(num)):
            if num[i] not in dicts:
                dicts[target - num[i]] = i
            else:
                return dicts[num[i]], i
        return -1, -1


if __name__ == '__main__':

    sl = Solution()
    output = sl.twoSum([3,2,4], 6)
    print(output)