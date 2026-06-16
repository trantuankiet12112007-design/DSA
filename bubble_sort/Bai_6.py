def Bai_6(A):
    n = len(A)
    for i in range(n):
        for j in range(0,n-i-1):
            if A[j] > A[j + 1]:
                A[j],A[j+1] = A[j+1],A[j]
    return A[-1]
A = [4, 2, 7, 1, 3]
print(Bai_6(A))