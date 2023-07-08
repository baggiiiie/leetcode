import collections


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # input: string of brackets
        # output: boolean
        # goal: check if all right bracket has a left bracket
        # and they are in correct order

        # 1. loop thru the string
        # 2. add left bracket to stack; pop stack if the correspoding left bracket is seen in stack
        # 3. if stack empty, valid; else, invalid
        stack = []
        bracketMap = {")": "(", "]": "[", "}": "{"}
        for bracket in s:
            # print(stack, bracket)
            if bracket in bracketMap:
                if stack and bracketMap[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return not stack


if __name__ == "__main__":
    strs = ["()", "()[]{}", "(]", "({[})]", "(){}}{", "({{{{}}}))", "}"]
    sol = Solution()
    for s in strs:
        print(sol.isValid(s))
