class Node:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
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
        self.tail.next = newNode
        self.tail = self.tail.next
        return
    
    def insertHead(self, val):
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next = newNode
        if self.head == self.tail:
            self.tail = self.tail.next
        return
    
    def remove(self, val):
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
        curr = self.head
        while curr and index > 0:
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
        curr = self.head.next
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
