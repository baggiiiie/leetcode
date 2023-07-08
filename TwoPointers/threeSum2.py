class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # input: int arr
        # output: 2d int arr of nums (no duplicates)
        # find all groups of 3 numbers that sum up to 0
        # note: int can be reused

        # think of it as a decreasing window and the pointers are sliding within the window
        # 1. sort nums
        # 2. l, r pointers stay, m moves
        # -> bad idea, essentially it's the same thing but could be implemented better
        # 2. l, r pointers to do sum, (target is 0-the first value)
        # 3. if sum = target, store in ans, move l and r
        # 4. if sum > target, r--; else l++
        # 5. when m = r, window decreases (first value + 1), l and r reset

        nums.sort()
        ans = []
        for i, num in enumerate(nums):
            l, r = i + 1, len(nums) - 1

            if i > 0 and num == nums[i - 1]:
                continue

            while l < r:
                sum = num + nums[l] + nums[r]
                if sum == 0:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
        return ans


if __name__ == "__main__":
    nums = [
        [0, 0, 0, 0],
        [-1, 0, 1, 2, -1, -4],
        [-1, 0, 1, 2, -1, -4],
        [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4],
    ]
    s = Solution()
    for num in nums:
        print(s.threeSum(num))
