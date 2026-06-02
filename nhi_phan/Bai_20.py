def can_allocate(pages, students, max_pages):
    count_students = 1
    current_pages = 0
    for p in pages:
        if current_pages + p > max_pages:
            count_students += 1
            current_pages = p
        else:
            current_pages += p
    return count_students <= students

def book_allocation(pages, students):
    if students > len(pages):
        return -1
    left = max(pages)
    right = sum(pages)
    result = right
    while left <= right:
        mid = (left + right) // 2
        if can_allocate(pages, students, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result
pages = list(map(int, input().split()))
students = int(input())
print(book_allocation(pages, students))