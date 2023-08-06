class Solution:
    def sumpeople(self, n, record):

        count_dict = {}

        for i in record:
            if count_dict.get(i):
                count_dict[i] += 1
            else:
                count_dict[i] = 1

        print(count_dict)


if __name__ == '__main__':
    n = 8
    record = [-1, 0, 0, 1, 2, 3, 1, 6]

    sol = Solution()
    print(sol.sumpeople(n, record))