def compare_lists(llist1, llist2):
    while llist1 is not None and llist2 is not None:
        if llist1.data!=llist2.data:
            return 0
        llist1 = llist1.next
        llist2 = llist2.next
    return llist1 is None and llist2 is None