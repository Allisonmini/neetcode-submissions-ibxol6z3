class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new = Node(value)
        last = self.tail.prev
        last.next = new
        new.prev= last
        new.next = self.tail
        self.tail.prev = new

    def appendleft(self, value: int) -> None:
        new = Node(value)
        first = self.head.next
        first.prev = new
        new.prev = self.head
        new.next = first
        self.head.next = new

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last = self.tail.prev
        value = last.value

        prev = last.prev
        prev.next =self.tail
        self.tail.prev= prev

        return value
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first = self.head.next
        value = first.value
        next = first.next
        next.prev = self.head
        self.head.next = next

        return value
        
