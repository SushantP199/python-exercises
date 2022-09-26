def selection_sort(A):
    for i in range(len(A)-1):
        min = i
        for j in range(i+1, len(A)):
            if A[min] > A[j]:
                min = j
        A[i], A[min] = A[min], A[i]


def print_sorted(A):
    for i in range(len(A)):
        print(A[i], end="\t")


A = [5, 4, 1, 8, 3]
selection_sort(A)
print_sorted(A)