# C. Meximum Array 2

### Description

You are given three positive integers `n`, `k`, and `q`. You are also given `q` tuples `(c, l, r)`.

An array `a₁, a₂, …, aₙ` is called **meximum** if `0 ≤ a[i] ≤ 10⁹` for each `i` in `[1, n]`, and for each given tuple `(c, l, r)`:

- If `c = 1`, then  
  `min(a[l], a[l+1], …, a[r]) = k`
- If `c = 2`, then  
  `MEX(a[l], a[l+1], …, a[r]) = k`

The value `k` is the **same for all tuples**.

The **MEX (Minimum Excluded Value)** of a collection of integers is defined as the smallest non-negative integer that does not occur in the collection.

You are guaranteed that at least one valid array exists.  
If multiple valid arrays are possible, you may output **any one of them**.

### Input

- The first line contains an integer `t` — the number of test cases `(1 ≤ t ≤ 500)`.
- For each test case:
  - The first line contains three integers `n`, `k`, and `q`  
    `(1 ≤ k ≤ n ≤ 100, 1 ≤ q ≤ 100)` — the length of the array, the fixed value for `min`/`MEX`, and the number of tuples.
  - The next `q` lines each contain a tuple `(c, l, r)`  
    `(1 ≤ c ≤ 2, 1 ≤ l ≤ r ≤ n)` describing a constraint on the subarray `a[l…r]`.

There are no constraints on the sum of `n`, `k`, or `q` over all test cases.

### Output

For each test case, print one line containing a valid meximum array  
`a₁, a₂, …, aₙ`.

---

### Sample

**Input:**

```text
4
6 2 2
1 1 3
2 2 6
3 3 1
2 1 3
3 3 2
1 1 1
1 3 3
3 2 2
2 1 2
2 2 3

```

**Output:**

```
2 5 4 3 0 1
2 0 1
3 3 3
1 0 1

```
