def bubble_sort(arr):
    new_arr = list(arr)
    for i in range(0, len(new_arr)):
        for j in range(0, len(new_arr) - 1 - i):
            if (new_arr[j] > new_arr[j + 1]):
                new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
    return new_arr
