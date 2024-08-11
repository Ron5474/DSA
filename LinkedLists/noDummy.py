class Node:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def search(self, val):
        curr = self.head
        i = 0
        while curr:
            if curr.val == val:
                return i
            i += 1
            curr = curr.next

    def insertTail(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.tail = self.head
            return
        if self.head == self.tail:
            self.head.next = newNode
            self.tail = self.tail.next
            return
        self.tail.next = newNode
        self.tail = self.tail.next
        return
    
    def insertHead(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.tail = self.head
            return
        newNode.next = self.head
        self.head = newNode
        return
    
    def remove(self, val):
        if self.head.val == val:
            self.head = self.head.next
            return True
        curr = self.head
        while curr and curr.next and curr.next.val != val:
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        else:
            return False

    def removeIdx(self, index):
        if index == 0:
            removeNode = self.head
            self.head = self.head.next
            removeNode.next = None
            return removeNode.val
        curr = self.head
        while curr and index > 1:
            curr = curr.next
            index -= 1
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            removeNode = curr.next
            curr.next = curr.next.next
            removeNode.next = None
            return removeNode.val
        return -1

    def printList(self):
        curr = self.head
        print("List: ", end='')
        while curr:
            print(curr.val, end=' ')
            curr = curr.next
        print()

L = LinkedList()
L.insertTail(1)
L.insertTail(2)
L.insertTail(3)
L.insertHead(0)
L.insertTail(4)
L.printList()

print(L.remove(4))
L.printList()
print(L.remove(0))
L.printList()
print(L.remove(2))
L.printList()
print(L.remove(2))
L.printList()
print(L.remove(1))
L.printList()
print(L.remove(3))
L.printList()

L.insertTail(1)
L.insertTail(2)
L.insertTail(3)
L.insertHead(0)
L.insertTail(4)
L.printList()

print(L.removeIdx(4))
L.printList()
print(L.removeIdx(0))
L.printList()
print(L.removeIdx(2))
L.printList()
print(L.removeIdx(2))
L.printList()
print(L.removeIdx(1))
L.printList()
print(L.removeIdx(3))
L.printList()
