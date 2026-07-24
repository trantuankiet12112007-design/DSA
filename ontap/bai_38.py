class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detect_cycle_entry(head: ListNode) -> ListNode:
    slow = fast = head
    has_cycle = False
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
            
    if not has_cycle:
        return None
        
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
        
    return slow

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2 

entry = detect_cycle_entry(node1)
print("Đầu chu trình là nút có giá trị:", entry.val if entry else "Không có chu trình") 
