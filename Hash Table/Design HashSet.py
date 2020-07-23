class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()

    def add(self, key: int) -> None:
        self.s.add(key)

    def remove(self, key: int) -> None:
        if key in self.s:
            self.s.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.s


# Your MyHashSet object will be instantiated and called as such:
if __name__ == "__main__":
    obj = MyHashSet()
    obj.add(1)
    obj.add(2)
    obj.contains(1)
    obj.contains(3)
    obj.add(2)
    obj.contains(2)
    obj.remove(2)
    obj.contains(2)