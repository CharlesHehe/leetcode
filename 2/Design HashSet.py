class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = set()

    def add(self, key: int) -> None:
        self.items.add(key)

    def remove(self, key: int) -> None:
        if key in self.items:
            self.items.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.items:
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
