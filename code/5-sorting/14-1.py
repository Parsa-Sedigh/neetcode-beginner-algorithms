def bucketSort(arr):
    # We're gonna have a 0 for each possible value in the range. Assuming arr only contains 0, 1 or 2.
    counts = [0, 0, 0]

    # Count the quantity of each val in arr
    for n in arr:
        counts[n] += 1

    # i tells us where to fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1

    return arr