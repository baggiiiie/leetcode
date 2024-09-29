from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # input: list of string containing nums and operators
        # output: computation result, int
        # solution: (how about division)
        # if it's num, put into stack; else (operator), pop stack, join operator and pop again
        # put result back into stack

        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except Exception:
                # token is operator
                if len(stack) < 2:  # need 2 numbers to operate
                    return "error"
                a, b = stack.pop(), stack.pop()
                # assume operators and nums are always correct
                temp_string = f"{b} {token} {a}"
                stack.append(int(eval(temp_string)))
        return stack[-1]


if __name__ == "__main__":
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    s = Solution()
    print(s.evalRPN(tokens))
