class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # goal: find indexes in nums where 2 nums sum up to target
        # assumption: always solution
        # restriction: cant use 1 num twice
        # 1. loop thru nums, keep num's index in dict as value, key = target - num
        # 2. while looping, check if num in dict
        # 3. if num in dict, append num's index and value in to final result
        numsDict = {}
        for i, num in enumerate(nums):
            if num in numsDict:
                results = [numsDict[num], i]
                return results
            numsDict[target - num] = i

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    target = 4
    print(s.twoSum(nums, target))