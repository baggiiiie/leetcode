import math


class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # input: int arr, int
        # output: int

        # 1. loop from min to max
        # 2. speed to l + r // 2
        # 3. hours = pile in piles // speed + 1
        # 4. if hours > target, too slow, l = speed + 1; vice versa
        # 5. if housr <= target, too fast, r = speed - 1
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)
            if totalTime <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res


if __name__ == "__main__":
    nums = [
        ([3, 6, 7, 11], 8),
        ([30, 11, 23, 4, 20], 5),
        ([30, 11, 23, 4, 20], 6),
    ]
    s = Solution()
    for num in nums:
        print(s.minEatingSpeed(num[0], num[1]))
        # break
