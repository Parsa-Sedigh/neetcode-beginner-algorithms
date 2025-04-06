# We store pairs in the underlying arr using this class
class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val


# Approach 1: Using open addressing to workaround collisions.
# Note: This approach doesn't work on Leetcode
# In this implementation, we're using open-addressing to workaround the collision.
class HashMap:
    def __init__(self):
        # size is the actual number of keys in the hashmap
        self.size = 0

        # the 2 here is arbitrary. Optimally, it should be a prime number
        self.capacity = 2

        # map is maintained as an arr
        self.map = [None, None]

    # Given a key, we should be able to convert it into an integer that fits within the capacity of the arr.
    def hash(self, key):
        index = 0
        for c in key:
            index += ord(c)

        # the index could become a big integer and gets out of bounds of the arr(larger than self.capacity). So we mod
        # it by capacity.
        return index % self.capacity

    def rehash(self):
        # naive way of increasing the size. More optimally we could find the next prime number that's roughly double.
        self.capacity = 2 * self.capacity
        newMap = []

        # We want the capacity of the new underlying arr to be the new increased capacity.
        for i in range(self.capacity):
            newMap.append(None)

        oldMap = self.map

        # Since we will call self.put() later in the for loop, we need to assign the newMap to the self.
        self.map = newMap

        # The reason we reset the size to 0, is we know internally the put() in the next for loop is gonna INCREMENT
        # the size by 1 each time anyway and that will give us the correct size. So we set the size to be 0. Otherwise,
        # since put() is gonna increment the size, we would end up with the wrong size after this method finish executing.
        self.size = 0

        # put the values of the oldMap into the new map
        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.val)

    def get(self, key):
        index = self.hash(key)

        # if the key we want existed in the hashmap, it means it would be in this spot, but it's not, so we can stop.
        # This key doesn't exist at all in this hashmap.
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1

            # Here, the reason we're modding by the capacity is assume
            # Note: index could become larger than self.capacity, so we should do: index % self.capacity not self.capacity % index.
            index = index % self.capacity

        # key doesn't exist
        return None

    def put(self, key, val):
        index = self.hash(key)

        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()

                return

            # the key is the same, overwrite the value. Since we're not occupying an element of the arr, we don't need
            # to increment the size.
            elif self.map[index].key == key:
                self.map[index].val = val

                return

            index += 1

            # mod it so we sure it's still in the bounds of the capacity
            index = index % self.capacity

    def remove(self, key):
        if not self.get(key):
            return

        index = self.hash(key)
        while True:
            if self.map[index].key == key:
                # Removing an element using open-addressing actually causes a bug,
                # because we may create a hole in the list, and our get() may
                # stop searching early when it reaches this hole.
                self.map[index] = None
                self.size -= 1

                return

            index += 1
            index = index % self.capacity

    def print(self):
        for pair in self.map:
            if pair:
                print(pair.key, pair.val)
