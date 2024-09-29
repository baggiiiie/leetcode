from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # input: list of int
        # output: list of three ints, which sum up to 0

        # solution:
        # 1. sort list and loop through
        # 2. for sub lists, two pointers loop through
        #    move l if sum < 0, move r if sum > 0
        # note: can't have duplicates -> move to next diff int when moving
        # 3. append to res if sum == 0
        res = []
        nums.sort()
        for l, num in enumerate(nums):
            if l > 0 and num == nums[l-1]:
                continue
            if num > 0: break
            m, r = l + 1, len(nums) - 1
            while m < r:    
                three_sum = num + nums[m] + nums[r] 
                print(l, m, r, three_sum)
                if three_sum > 0: 
                    r -= 1
                    continue
                elif three_sum < 0: 
                    m += 1
                else: 
                    res.append([num, nums[m], nums[r]])
                    m += 1
                    r -= 1
                while nums[m] == nums[m-1]:
                    m += 1

        return res

if __name__ == '__main__':
    s = "AAABAAABBBBBBBBBB"
    nums = [-1,0,1,2,-1,-4,5]
    # sorted_nums = [-4,-1,-1,0,1,2,5]
    k = 1
    solution = Solution()
    r = solution.threeSum(nums)
    print(r)
