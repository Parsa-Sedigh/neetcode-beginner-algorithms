## 02 RAM
### What is a data structure?
It's a way of structuring data inside of RAM.

RAM is where all of our variables are gonna be stored.

How do we store things in RAM?

RAM is measured in bytes. 1 Byte = 8 bits. What is a bit? A bit can be though of as a position that can store 0 or 1.

Individual bits can form multiple bits, which can form bytes, which can form RAM and RAM can be used to store advanced DSs.

It's common for integers to be represented not by a single byte but as 4 bytes. So we would have 32 bits. So 1 is gonna be represented as
31 zeros and a one at the end(right most bit): 000000...1. After doing this conversion, we can put it into RAM.

RAM can be thought of as a contiguous block of data. It also has two components: value and address. Every value is gonna be stored at a
distinct location which is called address.

Arrays are always gonna be stored in contiguous format in RAM. Now why at the img, the address of the elements of the arr stored in RAM are not
like: $0 $1 $2 ? Didn't we say arr is contiguous?

Remember each integer takes 4 bytes to store. So for example 1 represents 4 bytes.

We store arrays pretty much the same way that we use them. In memory, they look the same as the way we use them, a contiguous set of values.

Each char(assuming ASCII) only takes 1 byte to store in memory.

So we can store values contiguously regardless of how big or small they are(how many bytes each element of the arr requires), as long as we
increment the address by the size of the value in the RAM.

![](../img/2-arrays/2-1.png)

## 03 STATIC ARRAYS
The fact that we can go to any arbitrary address in our RAM and then read the value at that address, is a property of RAM, it's actually in the name
itself -> random access memory. We can randomly access any portion of the memory in constant time(O(1)). We don't have to start from the beginning of the
RAM until we arrive to the address we want it's value.

The biggest limitation of static arrays is they are fixed size.

In static arr, when we say remove an element, we can't actually delete or de-allocate that element of the static arr. Instead, we overwrite
the value there with a zero value. It's still in memory though.

In the worst case, if you're inserting a value at any arbitrary position of the arr, we might have to shift every value(worst case). We might have to
shift n values -> O(n). Where n is the number of values(not the size of the array). The exact same thing is true if we're removing a value at any
arbitrary index. When we say removing in this case, we're not saying replacing it with a 0 at that index, instead, we're saying we wanna pretend that
this element doesn't exist, we wanna move it to the end of the arr. So in the worst case which is removing the first element of the arr,
we have to shift all of the elements to the left by one index.

Note: Removing an element from a static arr, doesn't change the allocated memory for that arr. The removed elements would go to the end of the arr and have
a zero value.

- Read or write(actually overwriting) at any index -> O(1)
- insert or remove at the end -> O(1).
    - note: In inserting at the end, we have assumed we have at least one space left at the end / in removing from the end, we have assumed we have
    at least one element to remove
- insert at an arbitrary index -> O(n).
    - in worst case(inserting at the beginning) is O(n). Because we might have to shift evey value of the arr to the right.
    - for an empty arr to insert in the middle or beginning, it's very efficient -> O(1) . But we know we're talking about the worst case. That's what
    O() refers to.
- remove middle -> O(n)
    - worst case is removing the first element which we might have to shift every value of the arr to the left

![](../img/2-arrays/3-1.png)

## 04 DYNAMIC ARRAYS

## 05 STACKS