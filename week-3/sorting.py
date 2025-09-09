def insertion_sort(l):
    '''
    Implemention of the insertion sort algorithm
    '''
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1

        while j >= 0 and key < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key


def quick_sort(l):
    '''
    Implementation of the quick sort algorithm
    '''
    if len(l) <= 1:
        return l

    pivot = l[-1]  # Take the last element to be the pivot

    small = []
    large = []
    duplicate = []

    for el in l:
        if el > pivot:
            large.append(el)
        elif el < pivot:
            small.append(el)
        elif el == pivot:
            duplicate.append(el)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + duplicate + large


def bubble_sort(l):
    '''
    Implementation of the bubble sort algorithm
    '''
    for i in range(len(l)):
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


def effective_bubble_sort(l):
    '''
    Implementation of the effective bubble sort algorithm
    '''
    n = len(l)

    while True:
        swapped = False

        for i in range(1, n):
            if l[i - 1] > l[i]:
                l[i - 1], l[i] = l[i], l[i - 1]
                swapped = True

        if not swapped:
            break


l = [64, 34, 25, 12, 22, 11, 90]
m = l.copy()
o = l.copy()
p = l.copy()

insertion_sort(l)
bubble_sort(o)
effective_bubble_sort(p)

print("Insertion sort:", l)
print("Quick sort:", quick_sort(m))
print("Bubble sort:", o)
print("Effective bubble sort:", p)
