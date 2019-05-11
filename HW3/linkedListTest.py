from linkedList import LinkedList

def main():
    #init
    myList = LinkedList()
    #test isEmpty()
    print "isEmpty: " + str(myList.isEmpty())
    print "True if the initialized list is empty\n"
    #test size
    print "size: " + str(myList.size())
    print "Size of empty list should be 0\n"
    #test add
    myList.add(5)
    print "isEmpty: " + str(myList.isEmpty())
    print "Should be false since the list is no longer empty\n"
    print "size: " + str(myList.size())
    print "Size of list should now be 1 after adding one element\n"
    myList.add(4)
    myList.add(3)
    myList.add(2)
    myList.add(1)
    myList.add(0)
    print "size: " + str(myList.size())
    print "Size of list should now be 6 after adding five more elements\n"
    #test search
    print "search: " + str(myList.search(4))
    print "Search should return true since 4 is an element of the list\n"
    print "search: " + str(myList.search(6))
    print "Search should return false since 6 is not an element of the list\n"
    #test remove
    myList.remove(5)
    print "size: " + str(myList.size())
    print "Size of list should now be 4 after removing an element\n"
    print "search: " + str(myList.search(5))
    print "Search should return false since 5 is no longer an element of the list\n"
    #test printList
    print "printList:"
    myList.printList()
    print "Should print [0,1,2,3,4,5]"
    #test findAll
    print "findAll:"
    myList.findAll(6)
    print "Shoudn't find anything since 6 is not in the list\n"
    print "findAll:"
    myList.findAll(2)
    print "Should return [2] since there is only one element 2 in the index 2\n"
    myList.add(2)
    print "findAll:"
    myList.findAll(2)
    print "Should return [0,3] since another 2 was added to the head of the list\n"
    #test insert
    print "printList:"
    myList.printList()
    print "list before insertion\n"
    myList.insert(1, 1)
    myList.insert(7, 5)
    print "printList:"
    myList.printList()
    print "should return [2,1,0,1,2,3,4,5] after inserting 1 in position 1 and 5 in position 7(at the end)\n"
    #test popAtIndex
    print "popAtIndex: " + str(myList.popAtIndex(2))
    print "should return 0 since the element at position 2 was popped\n"
    print "printList:"
    myList.printList()
    print "list should now be [2,1,1,2,3,4,5] after popping 0\n"
    #test appendLast
    myList.appendLast(6)
    print "printList:"
    myList.printList()
    print "list should now be [2,1,1,2,3,4,5,6] after appending 6 using appendLast\n"

main()
