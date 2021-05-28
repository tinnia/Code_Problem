class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = set([])

    def add(self, key: int) -> None:
        self.data.add(key)

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return True if key in self.data else False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)