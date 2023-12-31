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

        # 1. sort nums
        # 2. l, r pointers stay, m moves
        # 3. if sum = target, ans.append(nums[l, m, r])
        # 4. if sum > target, r--; else m++
        # 5. when m = r, l++, m = l+1

        nums.sort()
        ans = []
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + 1
            while m < r:
                sum = nums[l] + nums[r] + nums[m]
                if sum == 0:
                    if [nums[l], nums[m], nums[r]] not in ans:
                        ans.append([nums[l], nums[m], nums[r]])
                    m += 1
                elif sum < 0:
                    m += 1
                elif sum > 0:
                    r -= 1
            l += 1
            r = len(nums) - 1
        return ans


if __name__ == "__main__":
    # nums = [0, 0, 0, 0]
    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [-2, 0, 1, 1, 2]
    # nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    s = Solution()
    print(s.threeSum(nums))
