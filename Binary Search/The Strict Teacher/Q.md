# The Strict Teacher (Hard Version)

### Time Limit

1.5 seconds

### Memory Limit

256 megabytes

---

### Description

This is the **hard version** of the problem.  
The only differences between the two versions are the constraints on `m` and `q`.  
In this version:

- `m, q ≤ 10⁵`

Narek and Tsovak were busy preparing this round, so they did not manage to do their homework and decided to steal David's homework. Their strict teacher noticed that David has no homework and now wants to punish him. She hires other teachers to help her catch David. Now, `m` teachers together are chasing him.

Luckily, the classroom is big, so David has many places to hide.

The classroom can be represented as a **one-dimensional line** with cells numbered from `1` to `n` (inclusive).

---

### Movement Rules

At the start:

- All `m` teachers and David are in **distinct cells**

Then they repeatedly make moves. During each move:

1. **David** goes to an adjacent cell or stays in the current one.
2. **Each of the `m` teachers**, simultaneously, goes to an adjacent cell or stays in the current one.

This continues until David is caught.

---

### Catch Condition

David is **caught** if **any teacher** (possibly more than one) is located in the **same cell** as David.

Everyone sees everyone else’s moves, and **all players act optimally**.

---

### Objective

Your task is to determine **how many moves** it will take for the teachers to catch David if everyone acts optimally.

- David acts to **maximize** the number of moves before being caught.
- Teachers coordinate to **minimize** the number of moves needed to catch David.

Additionally, you are given `q` **queries**, each specifying David’s starting position.

---

### Input

The first line contains a single integer `t` — the number of test cases  
`(1 ≤ t ≤ 10⁵)`.

For each test case:

- The first line contains three integers `n`, `m`, and `q`  
  `(3 ≤ n ≤ 10⁹, 1 ≤ m, q ≤ 10⁵)`  
  — the number of cells, teachers, and queries.

- The second line contains `m` **distinct integers**  
  `b₁, b₂, …, bₘ`  
  `(1 ≤ bᵢ ≤ n)` — positions of the teachers.

- The third line contains `q` integers  
  `a₁, a₂, …, a_q`  
  `(1 ≤ aᵢ ≤ n)` — David’s starting cell for each query.

---

### Guarantees

- For all `i, j`: `bᵢ ≠ aⱼ`
- The sum of `m` over all test cases ≤ `2 · 10⁵`
- The sum of `q` over all test cases ≤ `2 · 10⁵`

---

### Output

For each test case, output `q` lines.  
The `i`-th line should contain the answer to the `i`-th query.

---

### Example

#### Input

```text
2
8 1 1
6
3
10 3 3
1 4 8
2 3 10
```

#### Output

```text
5
1
1
2
```
