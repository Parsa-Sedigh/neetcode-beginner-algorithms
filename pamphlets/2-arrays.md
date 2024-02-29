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
If you don't specify the size of the dynamic arr, usually it'll initialize it to some default size, like in java the default size is 10.
So at the beginning, the size is 10 but length is 0.

With the internal implementation of the dynamic arr, it will maintain a pointer or a variable telling what index is the last element of the arr?

When the dynamic arr becomes full or near full, we allocate a new bigger arr somewhere in memory and copy all the elements into the new arr.
Now we have enough space to add new elements to the dynamic arr. Now we don't need the original arr anymore, so we de-allocate or free the
memory of the original arr(we tell the OS that we're not using this arr anymore, you can free it to allocate other values).

Why we doubled the size rather than just increasing it by one?

Since we allocated a brand new arr, we did a O(n) operation because first allocating the memory itself takes `O(n)` where n is the size of the arr,
but we also had to copy the original values into the new arr. We had to push every single value which is also `O(n)` where n is the **length** of the arr.
So we don't want to allocate a brand new arr every single time, but also we don't want to allocate a giant arr. So we doubled the size.

Note: 
- Allocating the space took -> O(n)
- Then moving the original elements to the new arr took another -> O(n)

When we double the capacity, we get **amortized complexity** which means: yes, it took O(n) to add an element to the arr if we were ran out of capacity,
but we know it's gonna be infrequent when we run out of space. So we can still say that the amortized time complexity of pushing a value to a
dynamic arr is going to be O(1). You can think of it as being the average time complexity. Because the vast majority of the time when we push a value
to the end, it's gonna be O(1). There's actually a mathematical proof for why this is the case. In math, it has to do with power series. In high level,
the calculation here is always dominated by the last term. This means the last term is always going to be greater than or equal to the sum of
all previous terms. This is the reason why we're doubling the size rather than just increasing it by one.

The time complexity of dynamic arrs is the same as static arrs.

![](../img/2-arrays/4-1.png)

Note: The second row(pushing and popping) at the end is O(1) even though in some cases we might have to resize the arr, we still assume it's O(1).

Note: There's no amortization for insert middle and remove middle rows. In the worst case they're always O(n) time op.

**Note:** When we pop or remove an element from the middle, we don't delete the memory it occupies. In case of pop, we just update the length(pointer to the
last el) and in case of remove from the middle, we shift all the elements after that index, to the left by one. 

## 05 STACKS
Typically supports 3 ops:
- push to the end
- pop from the end
- read the last element in the stack

![](../img/2-arrays/5-1.png)

You can implement a stack with linked list or arr.

We don't need to design a DS from scratch to be able to implement this. The dynamic arrs satisfy all of these requirements(ops).
So a stack can be implemented using a dynamic arr.

Note: We need to maintain the number of elements that exist in the stack. So we would know exactly where to push or pop the next el.

Stack: LIFO - last in, first out

So we can use a stack to reverse a sequence(even though there are other ways of doing this). There are other use cases for stacks as well.