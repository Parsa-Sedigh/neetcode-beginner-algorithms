# Section 13 BIT MANIPULATION

## 35 Bit Operator
`Logic and` AKA `bitwise and`.

xor is `exclusive or`. The result will be 1 only if one of the bits is 1 (not if both are 1). So it's similar to `or` except it's
exclusive `or`. Only exclusively one of the bits can be 1 in order the result to be 1(not both of them).

Those tables at the top of the img are called truth tables.

```python
# AND
n = 1 & 1

# OR
n = 1 | 0

# XOR
n = 0 ^ 1

# NOT(negation)
n = ~n

# bit shifting
n = 1
n = n << 1 # shift left 
n = n >> 1 # shift right 
```

## Bit shifting to left
Usually in programming langs, we're talking about 32-bit integers. Python has unlimited bits for values.

In any base, shifting to the left, means multiply that int by the base.

### In base 2
Multiply the int by 2.

When we have some binary integer, like `001` in binary representation or `1`, if we take it and bit shift it to the left by 1,
it takes all the bits of our int and shift them to the left by 1. So: the result of this: `001 << 1`, is: `010`.

So when we shift `010` to the left by 1, we get `100`, which in base 10 is 2 multiplied by 2, which get us 4.

Now what if we did this op again on the result? `100`. If we do it again(assuming our int is only 3 bits): `000`. So the bit 1
is gonna get dropped, it won't circle back at the right again.

### In base 10
In base 10, shifting to the left, is essentially take the int and multiply it by 10.

## Bit shifting to right
`100 >> 010 >> 001`. So as we shift to right, we're dividing by 2. Because we went from 4 to 2 to 1. But if we have an odd number,
like 1001 >> 0100 (9 to 4), we're gonna **round down** because 9 / 2 = 4.5 , but we got 4. So we round down.

---

`Question 35-1: Count the number of `1` bits of a given int.`

For example, we're given 23, in binary it's: `10111`. Since in most langs, the int is 32bit, we have 27 zeroes at the left.

Note: When we take any number and bitwise and it with 1(x & 1), the result that we get is always gonna be either 0 or 1.
The reason is in binary, 1 is represented as `000...1`. It has only zeroes at the left with a 1 at the right, so in the resulting int,
every bit is gonna be 0, except possibly the last 1(the right most bit). If right most bit in `x` is 1, the result would be 1,
but if the right most bit in x is 0, 0 & 1, would be 0, so the result would be 0.

![](../img/13-bit-manipulation/35-1.png)

**So the result of x & 1, depends on the right most bit of x.**