def remove_if(a, condition):
    write_ptr = 0
    for read_ptr in range(len(a)):
        if not condition(a[read_ptr]):
            a[write_ptr] = a[read_ptr]
            write_ptr += 1
    del a[write_ptr:]
    return a
a = [1, 2, 3, 4]
print(remove_if(a, lambda x: x % 2 == 0))
