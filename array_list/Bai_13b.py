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


def merge_sort_ll(head_node):
    if not head_node or not head_node.next:
        return head_node

    prev_slow = None
    slow = head_node
    fast = head_node
    while fast and fast.next:
        prev_slow = slow
        slow = slow.next
        fast = fast.next.next

    prev_slow.next = None

    left_side = merge_sort_ll(head_node)
    right_side = merge_sort_ll(slow)

    return merge_two_sorted_ll(left_side, right_side)

head = Node(3)
head.next = Node(1)
head.next.next = Node(2)
head = merge_sort_ll(head)

res = []
c = head
while c:
    res.append(str(c.data))
    c = c.next
print("Bài 13 (LL) - Sau khi sắp xếp:", " -> ".join(res))