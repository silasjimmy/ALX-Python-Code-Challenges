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

l = [11, 2, 26, 18, 23]

insertion_sort(l)

print(l)