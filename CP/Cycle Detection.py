def has_cycle(head):
    c1=head
    c2=head
    while c2 is not None and c2.next is not None:
        c1 = c1.next
        c2= c2.next.next
        if c1==c2: return 1
    return 0