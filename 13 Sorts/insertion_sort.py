def insertion_sort(A):
    for i in range(1, len(A)):
        val = A[i]
        j = i - 1
        while j >= 0 and A[j] > val:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = val


def print_sorted(A):
    for i in range(len(A)):
        print(A[i], end="\t")


A = [9, 6, 7, 3, 2]
insertion_sort(A)
print_sorted(A)
