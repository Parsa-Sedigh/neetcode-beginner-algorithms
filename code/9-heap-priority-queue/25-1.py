class Heap:
	def __init__(self):
		# We know the zeroth index of heap is not used during calculations. So this zero element is kinda a dummy.
		# So this is essentially an empty heap.
		self.heap = [0]

	# T: O(h) and we know in heaps, the binary tree is always complete, so it can never be unbalanced => O(log(n))
	# M: O(1)
	def push(self, val):
		# Put the value at the last index of array(heap is implemented as an array).
		self.heap.append(val)

		# Get the index that we just inserted at:
		i = len(self.heap) - 1

		# Percolate up. This word means shifting up(percolating up) the new inserted node, while the order property is not being satisfied
		# Continue this loop until the new inserted node is in the correct position
		while self.heap[i] < self.heap[i // 2]:
			tmp = self.heap[i]
			self.heap[i] = self.heap[i // 2]
			self.heap[i // 2] = tmp

			# we do this, because we just went from the new inserted position to it's parent position and now we wanna
			# potentially(in the next iteration) compare the new node in it's parent position to it's new parent and potentially swap it.
			i = i // 2

	# T: O(log(n))
	# M: O(1)
	def pop(self):
		# If the heap is empty(meaning there is only one element which is the zeroth index), there's nothing to pop.
		if len(self.heap) == 1:
			return None

		# If this is true, it means we only have the root, so remove it from the array and return that value
		if len(self.heap) == 2:
			return self.heap.pop()

		# store the original root node that we're trying to get rid of, into `res`
		res = self.heap[1]

		# Move last value to root
		# So pop the last value in the array(self.heap) and then move it to index 1
		self.heap[1] = self.heap.pop()

		# This means our pointer is at the root node
		i = 1

		# Percolate down
		# Note: only run this loop while we have a left child
		while 2 * i < len(self.heap):
			# Do we have both children? We can check this with `2 * i + 1 < len(self.heap)`.
			# Note: self.heap[2 * i + 1] < self.heap[2 * i] means is right child smaller than left child?
			# Note: self.heap[i] > self.heap[2 * i + 1] means the current child that we're at(current parent) is graeter than the right child
			if (2 * i + 1 < len(self.heap) and
				self.heap[2 * i + 1] < self.heap[2 * i] and
				self.heap[i] > self.heap[2 * i + 1]):
				# Swap right child
				tmp = self.heap[i]
				self.heap[i] = self.heap[2 * i + 1]
				self.heap[2 * i + 1] = tmp

				i = 2 * i + 1
			elif self.heap[i] > self.heap[2 * i]:
				# Swap left child
				tmp = self.heap[i]
				self.heap[i] = self.heap[2 * i]
				self.heap[2 * i] = tmp

				# Point it at the left child
				i = 2 * i

			# if the current node is not greater than the right child and also not greater than it's left child, break out of this while loop.
			# Why we would do this? Because we know the node we're percolating down, is already in the proper position, we don't want to
			# swap it anymore, we don't want to shift it down, it's already where it needs to be, that's why we would break out the loop.
			# Note: We're popping. So if we arrived to a position that is a valid position, we don't move further.
			else:
				break

		return res

	# T: O(n) where n is number of elms in the arr
	# M: O(1)
	def heapify(self, arr):
		# 0-th position is moved to the end
		arr.append(arr[0])

		self.heap = arr

		cur = (len(self.heap) - 1) // 2

		while cur > 0:
			# percolate down
			# We have another copy of cur and we name it `i`
			i = cur

			while 2 * i < len(self.heap):
				if (2 * i + 1 < len(self.heap) and
					self.heap[2 * i + 1] < self.heap[2 * i] and
					self.heap[i] > self.heap[2 * i + 1]):
					# Swap right child
					tmp = self.heap[i]
					self.heap[i] = self.heap[2 * i + 1]
					self.heap[2 * i + 1] = tmp

					i = 2 * i + 1
				elif self.heap[i] > self.heap[2 * i]:
					# Swap left child
					tmp = self.heap[i]
					self.heap[i] = self.heap[2 * i]
					self.heap[2 * i] = tmp

					i = 2 * i
				else:
					break

			# Remember that we're going in reverse order(backwards) in our array and for each of these, we're gonna percolate them down if
			# it's needed(using a while loop)
			cur -= 1