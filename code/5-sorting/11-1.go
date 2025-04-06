package main

// T: O(n^2)
// M: O(1)
func insertionSort(nums []int) []int {
	for i := 1; i < len(nums); i++ {
		j := i - 1

		for j >= 0  &&  nums[j] > nums[j+1]{
			nums[j], nums[j+1] = nums[j+1], nums[j]

			j--
		}
	}

	return nums
}

func main() {
	insertionSort(nil)
}
