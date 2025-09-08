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


l = [64, 34, 25, 12, 22, 11, 90]

insertion_sort(l)

print(l)