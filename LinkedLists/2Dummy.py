class Node:
    def __init__(self, val=-1, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def search(self, val):
        curr = self.head.next
        i = 0
        while curr:
            if curr.val == val:
                return i
            i += 1
            curr = curr.next

    def insertTail(self, val):
        newNode = Node(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev
        self.tail.prev.next = newNode
        self.tail.prev = newNode
        return
    
    def insertHead(self, val):
        newNode = Node(val)
        newNode.next = self.head.next
        newNode.prev = self.head
        newNode.next.prev = newNode
        self.head.next = newNode
        return
    
    def remove(self, val):
        curr = self.head
        while curr and curr.val != val:
            curr = curr.next
        if curr:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            curr.next = curr.prev = None
            return True
        else:
            return False

    def removeIdx(self, index):
        curr = self.head
        while curr and index >= 0:
            curr = curr.next
            index -= 1
        if curr and curr.next:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            curr.next = curr.prev = None
            return curr.val
        return -1

    def printList(self):
        curr = self.head.next
        print("List: ", end='')
        while curr and curr.val != -1:
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
