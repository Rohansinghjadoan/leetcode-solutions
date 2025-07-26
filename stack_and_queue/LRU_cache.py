

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache(object):
    

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache=dict()
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.next=self.head
        
        
    def _remove(self,node):
        prevnode=node.prev
        nextnode=node.next

        prevnode.next=nextnode
        nextnode.prev=prevnode
    
    def _insert(self,node):
        node.next=self.head.next
        node.prev=self.head

        self.head.next.prev=node
        self.head.next=node
        self.cache[node.key]=node
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node= self.cache[key]
            self._remove(node)
            self ._insert(node)
            return node.value
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value  
            self._remove(node)
            self._insert(node)
        else:
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            self._insert(Node(key, value))

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)