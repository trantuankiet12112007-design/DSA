class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def bubble_sort_linked_list(head):
    if not head:
        return head
    swapped = True
    while swapped:
        swapped = False
        curr = head
        while curr.next:
            if curr.val > curr.next.val:
                curr.val, curr.next.val = curr.next.val, curr.val
                swapped = True
            curr = curr.next
    return head

def print_linked_list(head):
    res = []
    curr = head
    while curr:
        res.append(str(curr.val))
        curr = curr.next
    res.append("null")
    return "-".join(res)

head = Node(1, Node(3, Node(2)))
sorted_head = bubble_sort_linked_list(head)
print(print_linked_list(sorted_head))