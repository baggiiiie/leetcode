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
                    ans.append([nums[l], nums[m], nums[r]])
                    break  # break the loop once a solution is found, so no duplicates
                elif sum < 0:
                    m += 1
                elif sum > 0:
                    r -= 1
            l += 1
        return ans


# the question rn is that r is not reset when m is reset
# is this a question?
# e.g., [-2, -1, -1, 0, 1, 1, 2, 4]
# no i dont think it'd cause any problem

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    print(s.threeSum(nums))
