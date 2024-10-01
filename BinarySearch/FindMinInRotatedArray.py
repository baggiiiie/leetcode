from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # input: list of int, sorted but rotated
        # output: int, minimun of array
        # note: all elements are distinct; required time complexity O(logn) -> binary search
        # solution:
        # find the sub list that's not in ascending order 
        # if m > l, left half is sorted; continue with rihgt half
        # if m < r, right half is sorted; continue with left half
        # we are converging l and r; aka finding the breaking point;
        # when l == r, we find the minimum
        if not nums:  return -1

        l, r = 0, len(nums) - 1
        while l < r:  # TODO: do we need = here
            m = (l + r) // 2
            if nums[l] <= nums[m] < nums[r]:
                return nums[l]
            if nums[m] > nums[r]:
                l = m + 1  
                # what if we use "m" here?
                # in the case of [3,2], m = 0, nums[m] > nums[r], l = m = 0 will get the loop stuck here
            elif nums[m] < nums[l]:
                r = m  # if m is the min, r = m - 1 will skip min
                # in the case of [2,3], m = 0, nums[m] = nums[l] will go to the first 'if', this part of code won't reach
        
        print(l, r)
        return nums[l]
 
    def findMin2(self, nums: List[int]) -> int:
        # binary to find which side has min
        # if m > r, min is in the right half
        # else min is in the left half
        if not nums:  return -1

        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] > nums[r]:  # m is already larger than r, m can't be min
                l = m + 1
            else:
                r = m - 1

        return min(res, nums[l])





if __name__ == "__main__":
    nums = [4,5,0,1,2,3]
    # 4, 0, 3 -> m < l -> r = m
    # nums = [4,5,1,2,3]
    # 4, 1, 3 -> m < l -> r = m
    # nums = [4,5,6,7,8,1,2,3]
    # 4, 7, 3 -> m > r -> l = m + 1 (m already > r, m can't be min)
    # nums = [1,2,3]
    solution = Solution()
    res = solution.findMin2(nums)
    print(res)
