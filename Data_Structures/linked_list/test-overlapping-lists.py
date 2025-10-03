def overlapping_lists(L1,L2):
    root1, root2 = has_cycle(L1), has_cycle(L2)

    if not root1 and not root2:
        return overlapping_no_cycle_lists(L1, L2)
    elif (root1 and root2) or(not root1 and root2):
        return None
    temp = root2
    while True:
        temp = temp.next
        if temp is root1 or temp is root2:

            if temp is not root1:
                return None
            def distance(a, b):
                dis = 0
                while a is not b:
                    a = a.next
                    dis += 1

                    return dis
                stem1_length, stem2_length = distance(L1, root1), distance(L2, root2)
                if stem1_length > stem2_length:
                    L2, L1 = L1, L2
                    root1, root2 = root2, root1
                    for _ in range(abs(stem1_length - stem2_length)):
                        L2 = L2.next
                        while L1 is not L2 and L1 is not root1 and L2 is not root2:
                            L1, L2 = L1.next, L2.next

                            return L1 if L1 is L2 else root1