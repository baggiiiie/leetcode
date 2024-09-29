class Solution:
    def isValid(self, s: str) -> bool:
        # input: string of parentheses
        # output: bool -> whether string is valid parentheses
        # solution:
        # 1. loop thru string, if left -> put in stack; right -> pop stack
        # 2. after loop, if stack empty -> valid
        stack = []
        paren_pair = {  # Space: O(3)
            "}": "{",
            ")": "(",
            "]": "[",
        }
        for char in s:  # Time: O(n)
            if char in paren_pair.keys():  # right parentheses, Time: O(3)
                if not stack or paren_pair[char] != stack[-1]:  # if empty stack, return False
                    return False
                stack.pop()
            elif char in paren_pair.values():  # Time: O(3)
                stack.append(char)  # put left parenthesis into stack
            else:
                return False
        return not stack  # if stack is not empty, it's not valid parentheses



if __name__ == '__main__':
    s = "[(])"
    solution = Solution()
    res = solution.isValid(s)
    print(res)
