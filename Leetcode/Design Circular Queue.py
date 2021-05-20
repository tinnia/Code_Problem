class MyCircularQueue:

    def __init__(self, k: int):
        self.Q = [None] * k
        self.front = 0
        self.rear = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % len(self.Q)
        self.Q[self.rear] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.Q)
        self.Q[self.front] = 0
        self.count -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.Q[(self.front + 1) % len(self.Q)]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.Q[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == len(self.Q)