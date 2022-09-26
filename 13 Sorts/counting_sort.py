def counting_sort(A):
    max = A[0]
    for i in range(len(A)):
        if A[i] > max:
            max = A[i]
    count = [0] * (max + 1)
    for i in range(len(A)):
        count[A[i]] += 1
    j = 0
    for i in range(len(count)):
        while count[i] > 0:
            A[j] = i
            j += 1
            count[i] -= 1


def print_sorted(A):
    for i in range(len(A)):
        print(A[i], end="\t")


A = [5, 3, 2, 3, 6, 1]
counting_sort(A,)
print_sorted(A)


"""
def counting_sort(A, high):
    count = [0] * (high + 1)
    for i in A:
        count[i] += 1
    start = 0
    for i in range(len(count)):
        while count[i] > 0:
            A[start] = i
            start += 1
            count[i] -= 1


def maximum(A):
    max = A[0]
    for i in range(len(A)):
        if A[i] > max:
            max = A[i]
    return max
"""