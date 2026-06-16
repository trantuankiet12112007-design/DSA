def Bai_1(A):
    n = len(A)
    for i in range(1):
        for j in range(0,n-i-1):
            if A[j] > A[j + 1]:
                A[j],A[j+1] = A[j+1],A[j]
    return A
A = [5, 1, 4, 2, 8]
print(Bai_1(A))