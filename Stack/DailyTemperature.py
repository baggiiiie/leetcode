class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # input: int arr
        # output: int arr
        # find the first increment and record the index diff
        # return 0 if increment not found

        # brute force, O(n^2)
        # 1. loop thru arr
        # 2. if r > left, record index diff
        # 3. move to the end of arr

        # stack:
        # ans = [0] of len(input)
        # while num > s[-1]:
        # - s.pop
        # - popCount ++
        # - store popCount to ans[i-pC]
        # add num to stack
        # if num < s[-1]
        # - add num to stack
        stack = []
        ans = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                pos = stack.pop()
                ans[pos[0]] = i - pos[0]
            stack.append((i, temp))
        return ans


if __name__ == "__main__":
    nums = [
        [1, 1, 1, 2, 1, 1, 3],
        [73, 74, 75, 71, 69, 72, 76, 73],
        [30, 40, 50, 60],
        [30, 60, 90],
    ]
    s = Solution()
    for num in nums:
        print(s.dailyTemperatures(num))
        # break
