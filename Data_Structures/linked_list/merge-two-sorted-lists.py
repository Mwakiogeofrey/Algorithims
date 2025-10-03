#Consider two singly linked list in which each node holds a number, assume the list sorted appear in ascending order within each list. The merge of the two lists is a list consisting of the nodes of the lists in which numbers appear in ascending order
#Write a program that takes two lists, assumed to be sorted, and return their merge. The only field your program can change in a node is its next field

def merge_two_sorted_lists(L1, L2):
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

        #Appends the remaining nodes of L1 or L2
        tail.next = L1 or L2
        return dummy_head.next    