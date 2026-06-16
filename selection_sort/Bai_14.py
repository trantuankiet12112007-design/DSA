class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def selection_sort_linked_list(head):
    dummy = Node(0)
    tail = dummy
    
    while head:
        min_node = head
        min_prev = None
        curr = head
        prev = None
        
        while curr:
            if curr.val < min_node.val:
                min_node = curr
                min_prev = prev
            prev = curr
            curr = curr.next
            
        if min_prev:
            min_prev.next = min_node.next
        else:
            head = head.next
            
        tail.next = min_node
        tail = min_node
        tail.next = None
        
    return dummy.next

def print_ll(node):
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    return "-".join(res) + "-null"

head = Node(3, Node(1, Node(2)))
print("Bài 14:", print_ll(selection_sort_linked_list(head)))