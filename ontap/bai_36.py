class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list_iterative(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        nxt = curr.next 
        curr.next = prev 
        prev = curr 
        curr = nxt 
    return prev

def reverse_list_recursive(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head

def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res))

head = ListNode(1, ListNode(2, ListNode(3)))
print("Danh sách đảo ngược (Lặp):")
print_list(reverse_list_iterative(head)) 
