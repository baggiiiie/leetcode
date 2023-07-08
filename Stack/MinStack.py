class MinStack(object):
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.minStack:
            val = min(self.minStack[-1], val)
        self.minStack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack = self.stack[:-1]
        self.minStack = self.minStack[:-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    # to achieve linear time complexity, we need more memory
    # -> another variable to store info on minVal
    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
