#Node class for the linked list, code from lecture slides
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext (self, newnext):
        self.next = newnext

#LinkedList class, init and first few methods from lecture slides
class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, element):
        temp = Node(element)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, element):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == element:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, element):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == element:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    #part a, prints the list
    def printList(self):
        cur = self.head
        if cur.getData != None:
            s = '[' + str(cur.getData())
        while cur.getNext() != None:
            cur = cur.getNext()
            s = s + ', ' + str(cur.getData())
        print s + ']'

    #part b, finds all positions of where an element is
    def findAll(self, elem):
        num = 0
        positions = []
        cur = self.head
        pos = 0
        while cur != None:
            if cur.getData() == elem:
                num += 1
                positions.append(pos)
            cur = cur.getNext()
            pos += 1
        #prints result
        if num == 0:
            print str(elem) + ' was not found.'
        else:
            print str(elem) + ' is found ' + str(num) + ' time(s) at position(s) ' + str(positions) + '.'

    #part c, inserts an element at a specified position
    def insert(self, pos, elem):
        if pos == 0:
            add(elem)
        else:
            cur = self.head
            for i in range(pos-1):
                cur = cur.getNext()
            newNode = Node(elem)
            newNode.setNext(cur.getNext())
            cur.setNext(newNode)

    #part d, pops an element at a specified position
    def popAtIndex(self, pos):
        cur = self.head
        for i in range(pos-1):
            cur = cur.getNext()
        val = cur.getNext().getData()
        cur.setNext(cur.getNext().getNext())
        return val

    #part 3, appends an element to the end of the list
    def appendLast(self, elem):
        cur = self.head
        while cur.getNext() != None:
            cur = cur.getNext()
        newNode = Node(elem)
        cur.setNext(newNode)
