from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # input: list of int
        # output: list of int,
        # where each element represents the index diff between e and next bigger element
        # if no next bigger element return 0, length of output == length of input

        # solution1: brute force, loop thru whole array and track down index diff
        # solution2:
        # loop thru array, unsettled ones put in stack with their index:value
        # if current > whatever in stack -> pop stack and update res
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                idx, temp_ = stack.pop()
                res[idx] = i - idx

            stack.append([i, temp])

        return res

    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        # input: list of int
        # output: list of int,
        # where each element represents the index diff between e and next bigger element
        # if no next bigger element return 0, length of output == length of input

        # solution1: brute force, loop thru whole array and track down index diff
        # solution2:
        # loop thru array, unsettled ones put in stack with their index:value
        # if current > whatever in stack -> pop stack and update res
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            for idx, temp_ in reversed(stack):
                if temp > temp_:
                    stack.pop()
                    res[idx] = i - idx

            stack.append([i, temp])

        return res


if __name__ == "__main__":
    n = [30, 38, 30, 36, 35, 40, 28]
    # n = [22, 21, 20]
    s = Solution()
    print(s.dailyTemperatures(n))
