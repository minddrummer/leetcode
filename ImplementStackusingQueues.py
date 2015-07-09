# Implement the following operations of a stack using queues.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# Notes:
# You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
# Update (2015-06-11):
# The class name of the Java function had been updated to MyStack instead of Stack.

# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and all test cases.


class Stack:
    # initialize your data structure here.
    def __init__(self):
    	self.val = []
        

    # @param x, an integer
    # @return nothing
    def push(self, x):
    	self.val.append(x) 
        

    # @return nothing
    def pop(self):
        self.val.pop()

    # @return an integer
    def top(self):
        return self.val[-1]

    # @return an boolean
    def empty(self):
    	return len(self.val) == 0



if __name__ == '__main__':
	test = Stack()
