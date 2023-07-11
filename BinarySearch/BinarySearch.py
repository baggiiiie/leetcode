class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # input: int arr(ascending) and int target
        # output: int index or -1
        # goal: perform binary search

        # 1. break to halves
        # 2. if mid < target, left = mid
        # 2. if mid > target, right = mid
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return -1


if __name__ == "__main__":
    nums = [([-1, 0, 3, 5, 9, 12], 9), ([-1, 0, 3, 5, 9, 12], 2), ([5], 5), ([5], 0)]
    s = Solution()
    for num in nums:
        print(s.search(num[0], num[1]))
        # break
