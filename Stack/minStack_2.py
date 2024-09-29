class MinStack:

	def __init__(self):
		self.stack = []
		self.min_val = []


	def push(self, val: int) -> None:
		# when push, need to check if new val is min
		if not self.min_val or val <= self.min_val[-1]:
			self.min_val.append(val)
		self.stack.append(val)


	def pop(self) -> None:
		# when pop, need to check if stack_top is min val, and what's the next min val
		if not self.stack or not self.min_val:
			return None
		if self.top() == self.min_val[-1]:
			self.min_val.pop()

		self.stack.pop()


	def top(self) -> int:
		return self.stack[-1] if self.stack else None


	def getMin(self) -> int:
		return self.min_val[-1] if self.min_val else None

# [3,2,2,1]


if __name__ == '__main__':
	minStack = MinStack()
	print(minStack)
	minStack.push(-2)
	print(minStack)
	minStack.push(-2)
	print(minStack)
	minStack.push(-3)
	print(minStack)
	minStack.push(-3)
	print(minStack)
	res = minStack.getMin()
	print(res)
	minStack.pop()
	print(minStack)
	res = minStack.getMin()
	print(res)
