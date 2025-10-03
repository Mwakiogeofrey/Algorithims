def even_odd_merge(L):
    if not L:
        return L
    even_dummy_head, odd_dummy_head = ListNode(0), ListNode(0)
    tails, turn = [even_dummy_head, odd_dummy_head], 0
    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1
        tails[1].next = None
        tails[0].next = odd_dummy_head.next
        return even_dummy_head.next