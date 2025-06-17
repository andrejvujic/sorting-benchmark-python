def selection_sort(arr):
    new_arr = list(arr)

    for i in range(0, len(new_arr) - 1):
        min_index = i
        for j in range(i + 1, len(new_arr)):
            if (new_arr[j] < new_arr[min_index]):
                min_index = j

        if (i != min_index):
            new_arr[i], new_arr[min_index] = new_arr[min_index], new_arr[i]

    return new_arr
