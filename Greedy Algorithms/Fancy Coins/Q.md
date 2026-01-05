#  Fancy Coins

### Description

Monocarp is going to make a purchase with a total cost of exactly `m` burles.

He has **two types of coins**, each of which comes in two variants: **regular** (limited quantity) and **fancy** (infinite quantity).

- Coins worth **1 burle**:
  - `a1` regular coins
  - infinitely many fancy coins
- Coins worth **k burles**:
  - `ak` regular coins
  - infinitely many fancy coins

Monocarp wants to pay **exactly `m` burles**, with **no change**.

He can use **both regular and fancy coins**, but his goal is to **minimize the total number of fancy coins used**.

Determine the **minimum number of fancy coins** required to complete the purchase.

---

### Input

- The first line contains an integer `t` — the number of test cases  
  `(1 ≤ t ≤ 3·10⁴)`

For each test case, a single line contains four integers:

- `m` — total cost of the purchase
- `k` — value of the second type of coin
- `a1` — number of regular coins worth `1`
- `ak` — number of regular coins worth `k`

Constraints:

- `1 ≤ m ≤ 10⁸`
- `2 ≤ k ≤ 10⁸`
- `0 ≤ a1, ak ≤ 10⁸`

---

### Output

For each test case, print a single integer — the **minimum number of fancy coins** Monocarp needs to use.

---

### Sample

**Input:**

```text
4
11 3 0 0
11 3 20 20
11 3 6 1
100000000 2 0 0
```

**Output:**

```text
5
0
1
50000000

```
