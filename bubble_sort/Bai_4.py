def Bai_4(A):
    n = len(A)
    swap = 0
    for i in range(n):
        for j in range(0,n-i-1):
            if A[j] > A[j + 1]:
                A[j],A[j+1] = A[j+1],A[j]
                swap += 1
    return swap
A = [3,2,1]
print(Bai_4(A))