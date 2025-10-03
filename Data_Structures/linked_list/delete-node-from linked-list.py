#Write a program which deletes a node in a singly linked list. The input node is guaranteed not to be the tail node
def deletion_from_list(node_to_delete):
    node_to_delete.data = node_to_delete.next.data
    node_to_delete.next = node_to_delete.next.next
    