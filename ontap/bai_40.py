class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sort_list(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
        
    prev = None
    slow = fast = head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
        
    prev.next = None 
    
    left = sort_list(head)
    right = sort_list(slow)
    
    dummy = ListNode(0)
    curr = dummy
    while left and right:
        if left.val < right.val:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next
        
    curr.next = left if left else right
    return dummy.next

def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res))

head = ListNode(3, ListNode(1, ListNode(2)))
sorted_head = sort_list(head)
print_list(sorted_head) 
