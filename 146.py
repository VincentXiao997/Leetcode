class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.pre = None
        self.next = None
    


class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.map = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key in self.map:
            value = self.map[key].val
            self.remove(key)
            self.add(key, value)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            self.add(key, value)
            if len(self.map) > self.size:
                self.remove(self.tail.pre.key)
        else:
            self.remove(key)
            self.add(key, value)
    
    def remove(self, key):
        node = self.map[key]
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next, node.pre = None, None
        self.map.pop(key)
    
    def add(self, key, val):
        node = Node(key, val)
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node
        node.pre = self.head
        self.map[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)