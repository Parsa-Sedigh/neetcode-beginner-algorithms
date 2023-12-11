# Python implementation of Insertion Sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        j = i - 1 # j is the previous index

        # check j >= 0 , so that we don't go out of bounds(from the left side)
        while j >= 0 and arr[j + 1] < arr[j]:
            # arr[j] and arr[j + 1] are out of order so swap them
            tmp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = tmp

            j -= 1

    return arr