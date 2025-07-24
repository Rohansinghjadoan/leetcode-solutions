class MyLinkedList:

    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = None
        self.n = 0

    def get(self, index):
        if index < 0 or index >= self.n:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        new_node = self.Node(val)
        new_node.next = self.head
        self.head = new_node
        self.n += 1

    def addAtTail(self, val):
        new_node = self.Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.n += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.n:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.n:
            self.addAtTail(val)
            return

        new_node = self.Node(val)
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        self.n += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.n:
            return
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            if curr and curr.next:
                curr.next = curr.next.next
        self.n -= 1
