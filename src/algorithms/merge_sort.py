def combine(a, b):
    i, j = 0, 0
    a = a + [float('inf')]
    b = b + [float('inf')]
    combined = []
    while i < len(a) - 1 or j < len(b) - 1:
        a0 = a[i]
        b0 = b[j]

        if (a0 < b0):
            combined.append(a[i])
            i += 1
        else:
            combined.append(b[j])
            j += 1

    return combined


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    middle = len(arr)//2

    return combine(merge_sort(arr[:middle]), merge_sort(arr[middle:]))
