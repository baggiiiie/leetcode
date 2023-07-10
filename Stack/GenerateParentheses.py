class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # input: int
        # output: array of strings
        # find all valid combo of n pairs of parentheses

        # what qualify as a valid pair of parentheses
        # -> every right bracket has a left bracket
        # 1. if stack empty, put left
        # 2. if stack not empty, put left/right
        # 3. if put left, add to stack;
        # 3. if put right, pop stack
        # 4. keep track of brackets used
        # 5. store to res when brackets exhausted

        res = []
        stack = []

        def myFunction(leftCount, rightCount):
            print(stack, res)
            if leftCount == rightCount == n:
                res.append("".join(stack))
                return
            if leftCount < n:
                stack.append("(")
                myFunction(leftCount + 1, rightCount)
                stack.pop()
            if rightCount < leftCount:
                stack.append(")")
                myFunction(leftCount, rightCount + 1)
                stack.pop()

        myFunction(0, 0)
        return res


if __name__ == "__main__":
    nums = [
        3,
    ]
    s = Solution()
    for num in nums:
        print(s.generateParenthesis(num))
