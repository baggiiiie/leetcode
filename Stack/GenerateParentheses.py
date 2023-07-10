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
        bracketString = ""
        stack = []
        pairCount = 0
        while pairCount < n:
            if not stack:  # if stack is empty
                bracketString += "("
                stack.append("(")
                pairCount += 1
                continue
            while stack:
                bracketString += "("
                stack.append("(")
                pairCount += 1
            while stack:
                bracketString += ")"
                stack.pop()
