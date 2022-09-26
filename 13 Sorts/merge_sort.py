def merge_sort(A):
    if len(A) > 1:
        midpoint = len(A) // 2
        L = A[: midpoint]
        R = A[midpoint:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1


def print_sorted(A):
    for i in range(len(A)):
        print(A[i], end="\t")


A = [15, 5, 24, 8, 1, 3, 16, 10, 20]
merge_sort(A)
print_sorted(A)

