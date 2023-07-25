class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # input: a rotated array
        # output: the min of the array

        # [4, 5, 0, 1, 2, 3]
        # two pointers
        # if left < right, correct order, discard left except the first one
        # if left > right, rotated part, the min exists in this rotated part
        # and move the left to half way and repeat
        # if one element left, it's the min

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            # print(nums[l], nums[m], nums[r])
            if nums[l] < nums[r]:
                r = l
            if nums[l] > nums[r]:
                if nums[m] >= nums[r]:
                    l = m + 1
                if nums[m] < nums[r]:
                    r = m
        return nums[l]


if __name__ == "__main__":
    nums = [
        [3, 4, 5, 1, 2],
        [4, 5, 6, 7, 0, 1, 2],
        [11, 13, 15, 17],
        [2, 1],
        [3, 1, 2],
    ]
    s = Solution()
    for num in nums:
        print(s.findMin(num))
        # break
