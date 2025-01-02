def reversePrint(llist):
    if llist is None:
        return
    reversePrint(llist.next)
    print(llist.data)