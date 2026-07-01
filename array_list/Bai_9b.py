class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_two_sorted_ll(l1, l2):
    dummy = Node(0)
    curr = dummy
    while l1 and l2:
        if l1.data <= l2.data:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 else l2
    return dummy.next

list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)

list2 = Node(2)
list2.next = Node(4)

merged_head = merge_two_sorted_ll(list1, list2)

res = []
c = merged_head
while c:
    res.append(str(c.data))
    c = c.next
print("Bài 9 (LL):", " -> ".join(res))