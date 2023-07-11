class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # input: m*n int arr(ascending), int target
        # output: boolean

        # 1. flatten the matrix and perform binary search
        # 2. compare each row's first and last int with target
        # 3. binary search the first num of all rows, then bSearch that row

        for row in matrix:
            if row[0] > target or row[-1] < target:
                continue
            if row[0] <= target and row[-1] >= target:
                left, right = 0, len(row) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if row[mid] < target:
                        left = mid + 1
                    elif row[mid] > target:
                        right = mid - 1
                    elif row[mid] == target:
                        return True
        return False


if __name__ == "__main__":
    nums = [
        ([[1]], 1),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13),
    ]
    s = Solution()
    for num in nums:
        print(s.searchMatrix(num[0], num[1]))
        # break
