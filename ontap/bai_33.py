def rotate(a, k):
    n = len(a)
    k %= n
    def reverse(l, r):
        while l < r:
            a[l], a[r] = a[r], a[l]
            l += 1; r -= 1
            
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return a

print(rotate([1, 2, 3, 4, 5], 2)) 
