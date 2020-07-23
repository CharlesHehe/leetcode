class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = k
        self.items = [-1] * k
        self.rear, self.head = -1, -1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if (self.rear + 1) % self.size == self.head:
            return False
        elif self.rear == -1:
            self.rear, self.head = 0, 0
            self.items[self.rear] = value
            return True
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.rear == -1:
            return False
        elif self.head == self.rear:
            self.rear = -1
            self.head = -1
            return True
        else:
            self.items[self.head] = None
            self.head = (self.head + 1) % self.size
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.head == -1:
            return -1
        else:
            return self.items[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.rear == -1:
            return -1
        else:
            return self.items[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.head == -1:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if (self.rear + 1) % self.size == self.head:
            return True
        else:
            return False


if __name__ == "__main__":
    obj = MyCircularQueue(3)
    param_1 = obj.enQueue(1)
    param_1 = obj.enQueue(2)
    param_1 = obj.enQueue(3)
    param_1 = obj.enQueue(4)
    param_2 = obj.deQueue()
    param_3 = obj.Front()
    param_4 = obj.Rear()
    param_5 = obj.isEmpty()
    param_6 = obj.isFull()
