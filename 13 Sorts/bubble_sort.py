def bubble_sort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1-i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


def print_sorted(A):
    for i in range(len(A)):
        print(A[i], end="\t")


A = [40, 20, 50, 60, 30, 10]
bubble_sort(A)
print_sorted(A)
