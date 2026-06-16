def da_sap_xep(A):
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            return False
    return True
def Bai_8(A, k):
    n = len(A)
    for i in range(k):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return da_sap_xep(A)
A = [3, 2, 1]
k = int(input("Nhap k: "))
print(Bai_8(A, k))