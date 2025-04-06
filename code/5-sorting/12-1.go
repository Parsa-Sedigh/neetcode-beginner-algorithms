package main

// T: O()
// M: O()
func mergeSort(nums []int, s, e int) []int{
	// Base case: if there's one element or no element
	if s >= e {
		return nums
	}

	m := (s + e) / 2

	// sort left and right halves
	/* The space required for the call stack is O(log(n)). Why?
	Because there are log(n) levels and the space complexity*/
	mergeSort(nums, s, m)
	mergeSort(nums, m+1, e)

	// merge sorted halves
	merge(nums, s, m, e) // or: mergeInPlace(nums, s, m, e)

	return nums
}

// T: O(n) - because every element must be processed once during the merge.
// M: O(1) - if we created new arrays for L and R, space would be O(n)
func merge(arr []int, s, m, e int) {
	L := arr[s:m+1]
	R := arr[m+1:e+1]

	i := 0
	j := 0
	k := s

	for i < len(L) && j < len(R) {
		if L[i] < R[j] {
			arr[k] = L[i]
			i++
		} else {
			arr[k] = R[j]
			j++
		}

		k++
	}

	for i < len(L) {
		arr[k] = L[i]
		i++
		k++
	}

	for j < len(R) {
		arr[k] = R[j]
		j++
		k++
	}
}

// T: O(n)
// M: O(1)
func mergeInPlace(arr []int, s, m, e int) {
	i := s
	j := m+1

	// Use a two-pointer approach for merging. i and j should be in bounds, meaning i <= m and j <= e
	for i <= m && j <= e{
		if arr[i] <= arr[j] {
			/* Element at i is already in the correct position.*/
			i++
		} else {
			/* If we reach this block, it means arr[i] > arr[j]. Meaning an el in the past, is actually greater than an el ahead.
			So arr[j] is not in the correct position. It should be at index `i`. So store arr[j] at tmp(since it's gonna get overwritten)
			and move backwards until the index after i and at each iteration, shift el to the right so that there's one space at index i,
			which is the place for arr[j], place it there.*/
			tmp := arr[j]

			/*
			Note: We shouldn't start at i+1 and go until j. Since it would overwrite the els with incorrect vals. Why?
			Because let's say it starts at index 1. Then it would do: arr[1] = arr[0]. Then it would do: arr[2] = arr[1] and ... .
			You see it's effectively overwriting all vals with the same val. For example, it overwrites all els with val 3.
			But if we do the loop backwards(starting at j until one element after i), each el will be overwritten with the el before itself.*/
			for k := j; k > i; k-- {
				arr[k] = arr[k-1]
			}

			arr[i] = tmp

			i++
			j++
		}
	}
}