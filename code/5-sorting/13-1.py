# Implementation of QuickSort
# s: start
# e: end
# T: - worst case(if input is already sorted): O(n^2)
#    - average case: O(n * log n)
# M: O(1)

# Note: Everything is happening in place so there's no need for a merge() step.
def quickSort(arr, s, e):
    # an individual element(which means e - s + 1 <= 1) is already sorted, so we don't do anything in that case
    if e - s + 1 <= 1:
        return

    pivot = arr[e]

    # This pointer tells us where we should insert the next value that's less than or equal to the pivot
    left = s  # pointer for left side

    # Partition: elements smaller than pivot on left side
    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp

            left += 1

    # Move pivot in-between left & right sides(Swap the el pointed by l and the pivot). Why? Because we know
    # every value before the one pointed by `left`, is smaller than pivot and every value after `left`,
    # is larger than pivot. So pivot should go to the place where is pointed by `left`.
    arr[e] = arr[left]
    arr[left] = pivot

    # Quick sort left side. We're taking left - 1 because we know `left` is the index where we put our pivot and we
    # know the pivot is in the perfect spot. So we ignore it for the rest of the algo.
    quickSort(arr, s, left - 1)

    # Quick sort right side
    quickSort(arr, left + 1, e)

    return arr
