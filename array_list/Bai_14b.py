class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def add_two_numbers_ll(l1, l2):
    dummy = Node(0)
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.data if l1 else 0
        val2 = l2.data if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        curr.next = Node(total % 10)

        curr = curr.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dummy.next

num1 = Node(2);
num1.next = Node(4);
num1.next.next = Node(3)
num2 = Node(5);
num2.next = Node(6);
num2.next.next = Node(4)

result_sum = add_two_numbers_ll(num1, num2)

res = []
c = result_sum
while c:
    res.append(str(c.data))
    c = c.next
print("Bài 14 (LL) - Kết quả cộng:", " -> ".join(res))