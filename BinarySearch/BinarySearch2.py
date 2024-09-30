from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # input: list of ints, target int
        # output: index of target or -1
        # solution:
        # 1. left right pointers, if middle > target, right move to m; middle < target, left move to m; else, return index
        l, r = 0, len(nums) - 1

        while l <= r:  
            # l needs to be able to equal to r, otherwise we can't find cases when nums[l] == target
            m = (l + r) // 2
            print(l, m, r)
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        return -1


if __name__ == "__main__":
    # nums = [-1, 0, 2, 4, 6, 8]
    # target = 3
    # nums = [-1, 0, 2, 4, 6, 8]
    # target = 4
    # nums = [-1, 0, 3, 5, 9, 12]
    # target = 9
    nums = [5]
    target = 5
    solution = Solution()
    res = solution.search(nums, target)
    print(res)
