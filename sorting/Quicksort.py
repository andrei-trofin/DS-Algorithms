def partition(arr, low, high):
    # initialize pointer which will tell us pivot position
    i = low - 1

    for j in range(low, high):
        if arr[j] < arr[high]:
            # put all the smaller elements in the left of the array
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])

    # move pivot to the right of all the elements smaller than it
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])

    # return the new position of the pivot
    return i+1


def quicksort(arr, low, high):
    if low < high:
        partitionIndex = partition(arr, low, high)
        quicksort(arr, low, partitionIndex - 1)
        quicksort(arr, partitionIndex + 1, high)


arr = [2, 22, 23, 1, 76, 68, 69, 52]
quicksort(arr, 0, len(arr) - 1)
print(arr)
