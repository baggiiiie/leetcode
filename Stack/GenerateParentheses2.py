from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def addParenthesis(left_count, stack, string):
            if left_count < n:
                # if left_count < n, we can put (
                addParenthesis(left_count + 1, stack + ["("], string + "(")
            if stack:
                # if stack is not empty -> there's already (, we can put )
                addParenthesis(left_count, stack[:-1], string + ")")
            if left_count == n and not stack:
                # when left_count = 0 and stack is empty, we return
                res.append(string)

        addParenthesis(0, [], "")

        return res


if __name__ == "__main__":
    n = 3
    s = Solution()
    print(s.generateParenthesis(n))
