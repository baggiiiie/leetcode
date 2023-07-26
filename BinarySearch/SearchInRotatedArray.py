class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # input: rotated int array, ascending
        # output: int, index of target, or -1
        # requirement: log(n)

        # binary search to narrow the range
        # binary search in the range to locate the num

        # [5, 6, 0, 1, 2, 3, 4], t = 3
        # if left > right, still rotated,
        # mid > right > target, target is in [left, mid]
        # mid > right < target, target is in [left, mid]
        # right > target, mid > target, target is in [left, mid]
        # right > target, mid < target, target is in [mid, right]
        # if left < right, not rotated
        # basic binary search

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            print(nums[l], nums[m], nums[r])
            if nums[l] > nums[r]:
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m
            else:
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return m
        return -1


if __name__ == "__main__":
    nums = [
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([4, 5, 6, 7, 0, 1, 2], 3),
        ([3, 5, 1], 3),
        ([1], 1),
    ]
    s = Solution()
    for num in nums:
        print(s.search(num[0], num[1]))
        # break
