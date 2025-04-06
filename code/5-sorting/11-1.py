# Python implementation of Insertion Sort
# T: Best case: O(n), worst case: O(n ^ 2)
# M: O(1)
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        j = i - 1  # j is the previous index

        # Note: check j >= 0 FIRST, so that we don't go out of bounds(from the left side)

        # Note: Don't work with arr[j - 1] here like saying: if arr[j] < arr[j - 1]. Because we it could go out of bounds. Instead,
        # work with arr[j + 1] and arr[j]

        # Note 2: Also do not work with arr[i] and arr[j] here. Because we could potentially move the arr[i] backwards MULTIPLE TIMES.
        # So i needs to be updated which we don't do. So work solely with `j` index because it's updated on each iteration. Allowing
        # moving it backwards multiple times.
        while j >= 0 and arr[j + 1] < arr[j]:
            # arr[j] and arr[j + 1] are out of order so swap them
            tmp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = tmp

            j -= 1

    return arr
