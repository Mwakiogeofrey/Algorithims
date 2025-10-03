def is_linked_list_a_palindrome(L):
    slow = fast = L
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

        first_half_iter. second_half_iter = L, reverse_Linked_list(slow)
        while second_half_iter.data != first_half_iter.data:
            return False
        second_half_iter, first_half_iter = (second_half_iter.next, first_half_iter.next)
        return True
