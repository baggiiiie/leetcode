from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # input: 2D matrix,
        # output: bool, find if target is in 2D matrix
        # note: time complexity O(log(m*n)) -> two binary searches
        # solution:
        # 1. binary search on first col, 2. binary search on row

        if not matrix or not matrix[0]:
            return False
        # col binary search, find the row_num where the first element <= target
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            middle = (top + bottom) // 2
            print(top, middle, bottom)
            if matrix[middle][0] == target:
                return True
            if matrix[middle][0] > target:
                bottom = middle - 1
            elif matrix[middle][-1] < target:
                top = middle + 1

        if top > bottom:
            return False

        # after col binary search, top = bottom = row to find
        # then we do binary search on within that row
        left, right = 0, len(matrix[top]) - 1
        while left <= right:
            middle = (left + right) // 2
            if matrix[top][middle] == target:
                return True
            if matrix[top][middle] > target:
                right = middle - 1
            elif matrix[top][middle] < target:
                left = middle + 1

        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        # flatten the array into 1D and perform basic binary search
        matrix = [
            cell for row in matrix for cell in row
        ]  # len(matrix) == m*n -> flattening takes O(n*m) time complexity
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[m] == target:
                return True
            if matrix[m] < target:
                l = m + 1
            elif matrix[m] > target:
                r = m - 1
        return False

    def searchMatrix3(self, matrix: List[List[int]], target: int) -> bool:
        # treat 2D array just like a 1D array
        # find middle point in the whole 2D array
        if not matrix or not matrix[0]:  # Time Complexity: O(1)
            return False
        row, col = len(matrix), len(matrix[0])  # Time Complexity: O(1)
        l, r = 0, row * col - 1
        while l <= r:  # Time Complexity: O(log(row*col))
            m = (l + r) // 2
            i = m // col
            j = m - (i * col)
            m_val = matrix[i][j]
            if m_val == target:
                return True
            if m_val < target:
                l = m + 1
            elif m_val > target:
                r = m - 1
        return False


if __name__ == "__main__":
    matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
    target = 1
    solution = Solution()
    res = solution.searchMatrix3(matrix, target)
    print(res)
