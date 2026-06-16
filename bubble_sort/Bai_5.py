def Bai_5(A):
    n = len(A)
    swap = 0
    for i in range(n):
        for j in range(0,n-i-1):
            swap +=1
            if A[j] > A[j + 1]:
                A[j],A[j+1] = A[j+1],A[j]
    return swap
A = [1,2,3]
print(Bai_5(A))