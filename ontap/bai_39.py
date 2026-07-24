class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0, head)
    fast = slow = dummy
    
    for _ in range(k + 1):
        if not fast:
            return head 
        fast = fast.next
        
    while fast:
        fast = fast.next
        slow = slow.next
        
    slow.next = slow.next.next
    return dummy.next

def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res))

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
new_head = remove_nth_from_end(head, 2)
print_list(new_head)
