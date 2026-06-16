class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertion_sort_linked_list(head):
    dummy = Node(0)
    curr = head
    while curr:
        prev = dummy
        while prev.next and prev.next.val <= curr.val:
            prev = prev.next
        next_temp = curr.next
        curr.next = prev.next
        prev.next = curr
        curr = next_temp
    return dummy.next

def print_ll(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    return "-".join(res) + "-null"

head = Node(3, Node(1, Node(2)))
print("Bài 15:", print_ll(insertion_sort_linked_list(head)))