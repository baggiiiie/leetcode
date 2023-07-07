class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # input: arr nums, int target
        # output: arr indexes
        # assumption: exactly 1 solution
        # note: 1-indexed, nums are sorted, constant extra space

        # 1. two pointers from l and r
        # 2. if sum > target, r--; else l++
        # 3. when sum = target, return [l+1, r+1]

        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            if numbers[l] + numbers[r] > target:
                r -= 1
            if numbers[l] + numbers[r] < target:
                l += 1
        return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))
