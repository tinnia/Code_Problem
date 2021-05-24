class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack = []
        while self.data:
            self.stack.append(self.data.pop())
        self.data.append(x)
        while self.stack:
            self.data.append(self.stack.pop())
        return self.data

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.data.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.data[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.data) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()