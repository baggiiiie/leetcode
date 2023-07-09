class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # input: string of nums and operators
        # output: int
        # goal: deal with numbers when operators found

        # 1. loop thru input
        # 2. if nums, add to stack
        # 2. if operators, pop stack until empty
        # 3. do calculation when stack is being popped
        # 4. put the result back in stack

        stack = []
        for char in tokens:
            # print(stack, char)
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                stack.append(0 - stack.pop() - stack.pop())
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(char))
        return stack.pop()


if __name__ == "__main__":
    nums = [
        ["2", "1", "+", "3", "*"],
        ["4", "13", "5", "/", "+"],
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
    ]
    s = Solution()
    for num in nums:
        print(s.evalRPN(num))
