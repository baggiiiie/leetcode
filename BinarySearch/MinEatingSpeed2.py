from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # input: list of int, hour(int)
        # output: int, min speed
        # goal: find the min speed which satisfies sum(ceiling(pile/speed) for pile in piles) == hour
        # solution:
        # find max speed, binary search to min speed
        # binary search get a speed, decrease by 1 to find out
        def get_time(speed):
            return sum(ceil(pile / speed) for pile in piles)  # time complexity O(n)

        # max speed is 1 pile per hour, as cannot eat from another pile in the same hour
        res = max_speed = max(piles)  # time complexity O(n)
        min_speed = 1
        while min_speed <= max_speed:  # time complexity O(nlogm) [m = max(piles)]
            speed = (min_speed + max_speed) // 2
            print(min_speed, speed, max_speed)
            time = get_time(speed)  # time complexity O(n)
            if time > h:
                min_speed = speed + 1
            elif time <= h:
                res = speed  # if time <= h, the speed is satisfactory, we save it first
                max_speed = speed - 1
        return res


if __name__ == "__main__":
    piles = [4]
    h = 3
    solution = Solution()
    res = solution.minEatingSpeed(piles, h)
    print(res)
